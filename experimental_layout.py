
from enum import unique
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go
import time # to simulate a real time data, time loop
st.set_page_config(page_title='Live Machine Performance Dashboard',layout='wide')
option = st.selectbox('MACHINE LEVEL',('STAMPER', 'BOSCH1','BOSCH2', 'CPM1','CPM2'))
from datetime import datetime

placeholder_container1 = st.empty()

for seconds in range(200):
#while True: 
    
 

    with placeholder_container1.container():
        df_stamper= pd.read_csv("L4Stamper.csv")
        df_stamper_without_dash = df_stamper.iloc[1:]
                
                
        df_CPM1= pd.read_csv("L4CPM1.csv")
        df_CPM1_without_dash = df_CPM1.iloc[1:]
        
        df_CPM2= pd.read_csv("L4CPM2.csv")
        df_CPM2_without_dash = df_CPM2.iloc[1:]

        df_BOSCH1= pd.read_csv("L4BOSCH1.csv")
        df_BOSCH1_without_dash = df_BOSCH1.iloc[1:]
        
        df_BOSCH2= pd.read_csv("L4BOSCH2.csv")
        df_BOSCH2_without_dash = df_BOSCH2.iloc[1:]
      

        # create two columns for charts 

        fig_col1, fig_col2, fig_col3 = st.columns([0.75,2,2])
        with fig_col1:
            
            # data
            def line_oee(oee):
                lizard_007 = go.Figure(go.Indicator(
                domain = {'x': [0, 1], 'y': [0, 1]},
                value = oee*100, #put line OEE here. 
                mode = "gauge+number+delta",
                title = {'text': "LINE OEE"},
                delta = {'reference': 70},
                gauge = {'axis': {'range': [0, 100]},

                         'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 70}}))
                lizard_007.update_layout(
                autosize=False,
               
                width=320,
                height=320,
                margin_l=0
               
                
            )

                st.write(lizard_007)
            line_csv = pd.read_csv("Line.csv")
            line_csv_without_dash = line_csv.iloc[1:,:]
            dt3 = datetime.strptime('2021-10-20 06:00:48.00000', "%Y-%m-%d %H:%M:%S.%f")
            dt_line =line_csv_without_dash._get_value(1,0, takeable = True)
            line_time = datetime.strptime(dt_line, "%Y-%m-%d %H:%M:%S.%f")
            
            line_time_diff=round(((line_time-dt3).seconds)/60)
            if line_time_diff<480:
                fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                fbc = float(fbc)
                oee=(fbc*84)/(500*line_time_diff)
                line_oee(oee)







            if line_time_diff>480 and line_time_diff<960:
                fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                fbc = float(fbc)
                oee=(fbc*84)/(500*(line_time_diff-480))
                line_oee(oee)



            if line_time_diff>960:
                fbc= line_csv_without_dash._get_value(1,3, takeable = True)
                fbc = float(fbc)
                oee=(fbc*84)/(500*(line_time_diff-960))
                line_oee(oee)
            

            
            st.write("Breakdown")
            
            
            
##################################################################################################################################################################################################################################################
            #fig_bar = go.Figure([go.Bar(x=oee, y=[20, 14, 23])])
            
            


            
            
            
        with fig_col2:
                st.write("Stamper Loss Capturing")
                # Creating dataset
                labels = ['Stamper', 'Bosch1',  'Bosch2', 'CPM1','CPM2','Mixer']
                values2 = [72.8, 7.2, 14.7, 5.3,18,20]
                fig2 = px.pie(labels, values = values2, names = labels,width=400, height=400)
                fig2.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1))
                st.write(fig2)
                #This is the Line Chart
                
                
                if option == "STAMPER":

                    
                    figl = go.Figure(data=go.Scatter(x=df_stamper_without_dash['DateAndTime            '],y=pd.to_numeric(df_stamper_without_dash["Stamper_Present_Speed   "].iloc[1:481])))
                    figl.update_layout(
                    title="Stamper Speed")
                    
                    st.write(figl)
                ####THis is the live data barplot
                
                if option == "BOSCH1":
                    
                    
                    figl_BOSCH1_speed = go.Figure(data=go.Scatter(x=df_BOSCH1_without_dash['DateAndTime            '],y=pd.to_numeric(df_BOSCH1_without_dash["Bosch_01_Actual_speed   "].iloc[1:481])))
                    figl_BOSCH1_speed.update_layout(
                    title="BOSCH1 Speed")
                    st.write(figl_BOSCH1_speed)
                if option == "BOSCH2":
                    
                    
                    figl_BOSCH2_speed = go.Figure(data=go.Scatter(x=df_BOSCH1_without_dash['DateAndTime            '],y=pd.to_numeric(df_BOSCH2_without_dash["BOSCH_2_Speed           "].iloc[1:481])))
                    figl_BOSCH2_speed.update_layout(
                    title="BOSCH2 Speed")
                     
                    st.write(figl_BOSCH2_speed)
                if option == "CPM1":
                    
                    figl_CPM1_speed =  go.Figure(data=go.Scatter(x=df_CPM1_without_dash['DateAndTime            '],y=pd.to_numeric(df_CPM1_without_dash["CPM_1_Actual_Speed      "].iloc[1:481])))
                    figl_CPM1_speed.update_layout(
                    title="CPM1 Speed")
                if option == "CPM2":
                    
                    
                    figl_CPM2_speed = go.Figure(data=go.Scatter(x=df_CPM2_without_dash['DateAndTime            '],y=pd.to_numeric(df_CPM2_without_dash["CPM_2_Actual_Speed      "].iloc[1:481])))
                    figl_CPM2_speed.update_layout(
                    title="CPM2 Speed")
                     
                    st.write(figl_CPM2_speed)
        
                    
                df_stamper_without_dash_for_machine_status = df_stamper.iloc[1:480,:]
                stamper_runmode = pd.to_numeric(df_stamper_without_dash_for_machine_status["Stamper_In_Run_mode     "])
                stamper_runmode.replace(to_replace={1:0, 0:1}, inplace= True)

###########################################################################################################################################
# This is the machine Running Status
                fig_stamper_runmode = go.Figure()

                fig_stamper_runmode.add_trace(go.Bar(
                    x=df_stamper_without_dash_for_machine_status['DateAndTime            '],
                    y=stamper_runmode,
                    name='Primary Product',
                    marker_color='red',
                    
                    ))
                fig_stamper_runmode.update_layout( bargap=0,title= "Stamper Run Mode")
                st.write(fig_stamper_runmode)
                    
                    
        with fig_col3:
            def fault_time(file_name):
                    cpm1_fault = pd.read_csv(file_name)
                    top5_fault = cpm1_fault.iloc[1:6,3:4]
                    fault_freq = cpm1_fault.iloc[1:6,4:5]
                    figT= go.Figure(data= go.Table(header=dict(values=['Minor Stop Details', 'Time in Minutes']),cells=dict(values=[top5_fault,fault_freq])))
                    st.write(figT)
            if option == "CPM1":
                fault_time("CPM1faulttime.csv")
            
            ## This is the table for the Downstream and upstream block
            df_bosch_without_dash_for_block = df_BOSCH1.iloc[1:480,:]
            bosch1_upstream_block_count=df_bosch_without_dash_for_block['Bosch_01_Waiting_For_Upstream'].value_counts()[1]
            stop_type= ['Downstream Block','Upstream Block']

            bosch1_downstream_block_count=df_bosch_without_dash_for_block['Bosch_01_Downstream_Not_Ready'].value_counts()[1]
            figT2= go.Figure(data= go.Table(header=dict(values=['', 'Block in minutes']),cells=dict(values=[stop_type,[bosch1_downstream_block_count,bosch1_upstream_block_count]])))

            st.write(figT2)
        
        time.sleep(1)
    #placeholder.empty()