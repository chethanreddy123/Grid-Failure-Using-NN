#importing all the required libraries
import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random as rd

#reading data
df = pd.read_csv('DailyDelhiClimateTrain.csv')
df['date'] = pd.to_datetime(df['date'])


add_selectbox = st.sidebar.selectbox(
    "Please do select the options below",
    ("Home Page" , "Manual Prediction" , "Live Prediction")
)

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Learn Start Up Management Project")
st.sidebar.image("sideBar.jpeg", use_column_width=True)

#defining containers
header = st.container()
select_param = st.container()
plot_spot = st.empty()

#title
with header:
    st.title("Delhi Daily Weather Dashboard")
#select parmeter drop down
with select_param:
    param_lst = list(df.columns)
    param_lst.remove('date')
    select_param = st.selectbox('Select a Weather Parameter',   param_lst)


#function to make chart
def make_chart(df, y_col, ymin, ymax, const):
    fig = go.Figure(layout_yaxis_range=[ymin, ymax])
    fig.add_trace(go.Scatter(x=df['date'], y=df[y_col],   mode='lines+markers'))
    
    fig.update_layout(width=900, height=570, xaxis_title='time',
    yaxis_title=y_col)

    fig.add_trace(go.Scatter(x=df['date'], y=df[y_col] + rd.randint(1,10),   mode='lines+markers'))
    
    fig.update_layout(width=900, height=570, xaxis_title='time',
    yaxis_title=y_col)
    st.write(fig)


#func call
n = len(df)
ymax = max(df[select_param])+5
ymin = min(df[select_param])-5

for i in range(0, n-30, 1):
    df_tmp = df.iloc[i:i+30, :]
    with plot_spot:
        make_chart(df_tmp, select_param, ymin, ymax, 3)
    time.sleep(1)
    






