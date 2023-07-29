#importing all the required libraries
import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random as rd
from tensorflow import keras


model = keras.models.load_model('myModel.model')

st.title("Real-Time Object ")

dummy1 = pd.DataFrame()
dummy2 = pd.DataFrame()

dummy1['Value'] = []
dummy2['Value'] = []

dummy1['Time'] = []
dummy2['Time'] = []


plot_spot = st.empty()
text_box_info = st.empty()
Status = st.empty()

def make_chart(df1, df2, df3, df4, df5, df6, df7 ,df8, df9 , df10, df11,df12):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df1['Time'], y=df1['Value'],   mode='lines+markers' , name='P1'))
    
    fig.update_layout(width=900, height=570, xaxis_title='time',
    yaxis_title='Value')

    fig.add_trace(go.Scatter(x=df2['Time'], y=df2['Value'],   mode='lines+markers' , name='P2'))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')

    fig.add_trace(go.Scatter(x=df3['Time'], y=df3['Value'],   mode='lines+markers', name='P3'))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')

    fig.add_trace(go.Scatter(x=df4['Time'], y=df4['Value'],   mode='lines+markers' , name='P4'))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')

    fig.add_trace(go.Scatter(x=df5['Time'], y=df5['Value'],   mode='lines+markers' , name='G1'))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')

    fig.add_trace(go.Scatter(x=df6['Time'], y=df6['Value'],   mode='lines+markers' , name='G2'))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')

    fig.add_trace(go.Scatter(x=df7['Time'], y=df7['Value'],   mode='lines+markers' , name='G3'))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')

    fig.add_trace(go.Scatter(x=df8['Time'], y=df8['Value'],   mode='lines+markers' , name='G4'))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')


    fig.add_trace(go.Scatter(x=df9['Time'], y=df9['Value'],   mode='lines+markers', name="Tau1"))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')


    fig.add_trace(go.Scatter(x=df10['Time'], y=df10['Value'],   mode='lines+markers', name="Tau2"))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')


    fig.add_trace(go.Scatter(x=df11['Time'], y=df11['Value'],   mode='lines+markers', name="Tau3"))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')


    fig.add_trace(go.Scatter(x=df12['Time'], y=df12['Value'],   mode='lines+markers', name="Tau4"))
    
    fig.update_layout(width=800, height=550, xaxis_title='time',
    yaxis_title='Value')

    st.write(fig)


tau1 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.5,10) for i in range(100000)]})
tau2 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.5,10) for i in range(100000)]})
tau3 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.5,10) for i in range(100000)]})
tau4 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.5,10) for i in range(100000)]})

p1 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(-2,-0.5) for i in range(100000)]})
p2 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(-2,-0.5) for i in range(100000)]})
p3 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(-2,-0.5) for i in range(100000)]})
p4 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(-2,-0.5) for i in range(100000)]})

g1 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.05, 1.00) for i in range(100000)]})
g2 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.05, 1.00) for i in range(100000)]})
g3 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.05, 1.00) for i in range(100000)]})
g4 = pd.DataFrame({'Time' : [i for i in range(100000)] , "Value" :  [rd.uniform(0.05, 1.00) for i in range(100000)]})


counter = 0

start = 0
end = 10
for i in range(10000):
    
    with plot_spot:
        make_chart(p1[start +counter : end + counter],
                    p2[start +counter : end + counter],
                    p3[start +counter : end + counter],
                    p4[start +counter : end + counter],
                    g1[start +counter : end + counter],
                    g2[start +counter : end + counter],
                    g3[start +counter : end + counter],
                    g4[start +counter : end + counter],
                    tau1[start +counter : end + counter],
                    tau2[start +counter : end + counter],
                    tau3[start +counter : end + counter],
                    tau4[start +counter : end + counter])
        
    CurrentText = f''' 

    Reaction Time:
    The reaction time of Generation Node: {tau1['Value'][counter]}
    The reaction time of participant 1: {tau2['Value'][counter]}
    The reaction time of participant 2: {tau3['Value'][counter]}
    The reaction time of participant 3: {tau4['Value'][counter]}
    
    Nominal Power Produced:
    Nominal Power Produced by Generation Node: {p1['Value'][counter]}
    Nominal Power Produced participant 1: {p2['Value'][counter]}
    Nominal Power Produced participant 2: {p3['Value'][counter]}
    Nominal Power Produced participant 3: {p4['Value'][counter]}

    Price elasticity coefficien:
    Price elasticity coefficient for each network Generation Node: {g1['Value'][counter]}
    Price elasticity coefficient for each network participant 1: {g2['Value'][counter]}
    Price elasticity coefficient for each network participant 2: {g3['Value'][counter]}
    Price elasticity coefficient for each network participant 3: {g4['Value'][counter]}
    '''
        
    with Status:
        y_pred = model.predict(
            [[ tau1['Value'][counter], tau2['Value'][counter], tau3['Value'][counter], tau4['Value'][counter],
              p1['Value'][counter], p2['Value'][counter], p3['Value'][counter], p4['Value'][counter],
              g1['Value'][counter], g2['Value'][counter], g3['Value'][counter], g4['Value'][counter] ]]
            )[0][0]
        if y_pred == 0:
            st.warning(f'Current ID: {round(rd.random()*10000)} \n Your grid is currently stable 🔥')
        else:
            st.success(f'Current ID: {round(rd.random()*10000)} \n Your grid currently unstable 🔑')


    with text_box_info:
        st.write("Current Parameter Values",CurrentText)


    
    counter = counter + 1

    time.sleep(0.5)