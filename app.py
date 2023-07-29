# !pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
import random as rd

model = keras.models.load_model('myModel.model')

st.title('Power Grid Stability Analysis with Deep Learning')



add_selectbox = st.sidebar.selectbox(
    "Please do select the options below",
    ("Home Page" , "Manual Prediction" , "Live Prediction")
)

st.sidebar.title('Developer\'s Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.sidebar.success("Learn Start Up Management Project")



# 'tau1' to 'tau4': the reaction time of each network participant, a real value within the range 0.5 to 10 ('tau1' corresponds to the supplier node, 'tau2' to 'tau4' to the consumer nodes);
# 'p1' to 'p4': nominal power produced (positive) or consumed (negative) by each network participant, a real value within the range -2.0 to -0.5 for consumers ('p2' to 'p4'). As the total power consumed equals the total power generated, p1 (supplier node) = - (p2 + p3 + p4);
# 'g1' to 'g4': price elasticity coefficient for each network participant, a real value within the range 0.05 to 1.00 ('g1' corresponds to the supplier node, 'g2' to 'g4' to the consumer nodes; 'g' stands for 'gamma');

if add_selectbox == "Manual Prediction":
    st.sidebar.image("sideBar.jpeg", use_column_width=True)
    with st.form("my_form"):
        st.subheader("Put your parameters here to predict")
        tau1 = float(st.text_input("The reaction time of Generation Node" , rd.uniform(0.5,10)))
        tau2 = float(st.text_input("The reaction time of participant 1" , rd.uniform(0.5,10)))
        tau3 = float(st.text_input("The reaction time of participant 2" , rd.uniform(0.5,10)))
        tau4 = float(st.text_input("The reaction time of participant 3" , rd.uniform(0.5,10)))

        p1 = float(st.text_input('Nominal Power Produced (positive) or consumed (negative) by Generation Node',rd.uniform(-2,-0.5)))
        p2 = float(st.text_input('Nominal Power Produced (positive) or consumed (negative) by participant 1',rd.uniform(-2,-0.5)))
        p3 = float(st.text_input('Nominal Power Produced (positive) or consumed (negative) by participant 2',rd.uniform(-2,-0.5)))
        p4 = float(st.text_input('Nominal Power Produced (positive) or consumed (negative) by participant 3',rd.uniform(-2,-0.5)))

        g1 = float(st.text_input('Price elasticity coefficient for each network Generation Node',rd.uniform(0.05, 1)))
        g2 = float(st.text_input('Price elasticity coefficient for each network participant 1',rd.uniform(0.05, 1)))
        g3 = float(st.text_input('Price elasticity coefficient for each network participant 2',rd.uniform(0.05, 1)))
        g4 = float(st.text_input('Price elasticity coefficient for each network participant 3',rd.uniform(0.05, 1)))


        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
                y_pred = model.predict([[tau1,tau2,tau3,tau4,p1,p2,p3,p4,g1,g2,g3,g4]])[0][0]
                if y_pred == 0:
                    st.warning('Your grid is currenly unstable')
                else:
                    st.success('Your grid is currenly stable')

elif add_selectbox == "Live Prediction":
    st.subheader('Real-Time Grid Stability Detection')
    st.sidebar.image("LivePredImage.jpeg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    #importing all the required libraries
    import streamlit as st
    import time
    import plotly.graph_objects as go
    import pandas as pd
    import numpy as np
    import random as rd
    from tensorflow import keras


    model = keras.models.load_model('myModel.model')

    dummy1 = pd.DataFrame()
    dummy2 = pd.DataFrame()

    dummy1['Value'] = []
    dummy2['Value'] = []

    dummy1['Time'] = []
    dummy2['Time'] = []


    plot_spot = st.empty()
    text_box_info = st.empty()
    Status = st.empty()
    RadarPlot = st.empty()

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
        with text_box_info:
            st.write("Current Parameter Values",CurrentText)

        with Status:
            y_pred = model.predict(
                [[ tau1['Value'][counter], tau2['Value'][counter], tau3['Value'][counter], tau4['Value'][counter],
                p1['Value'][counter], p2['Value'][counter], p3['Value'][counter], p4['Value'][counter],
                g1['Value'][counter], g2['Value'][counter], g3['Value'][counter], g4['Value'][counter] ]]
                )[0][0]
            if y_pred == 0:
                st.warning(f'Current ID: {round(rd.random()*10000)} \n Your grid is currently unstable 🔥')
                
            else:
                st.success(f'Current ID: {round(rd.random()*10000)} \n Your grid currently stable 🔑 , Your Grid will be stable for next 45 mins')
    
            



        


        
        counter = counter + 1
        

        time.sleep(0.5)

elif add_selectbox == "Home Page":
    st.image("MainHome.jpeg", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.sidebar.image("sideImage.jpeg", use_column_width=True)
    st.subheader('4-node star architecture')

    st.caption('''
    
        4-node star architecture, comprising one power source (a centralized generation node) supplying energy to three consumption nodes. The model takes into consideration inputs (features) related to:

        1. The total power balance (nominal power produced or consumed at each grid node)
        2. The response time of participants to adjust consumption and/or production in response to price changes (referred to as "reaction time);
        3. energy price elasticity.

        ''')
    
    st.image("https://i.imgur.com/hvmW0cg.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    st.subheader('Data-Set')

    st.caption('''

     "Electrical Grid Stability Simulated Dataset", created by Vadim Arzamasov (Karlsruher Institut für Technologie, Karlsruhe, Germany) and 
      donated to the University of California (UCI) Machine Learning Repository (link here), where it is currently hosted.

    ''')

    st.caption('''

        The original dataset contains 10,000 observations. As the reference grid is symetric, the dataset can be augmented in 3! (3 factorial) times, or 6 times, representing a permutation of the three consumers occupying three consumer nodes. The augmented version has then 60,000 observations. It also contains 12 primary predictive features and two dependent variables.

        Predictive features:

        1. 'tau1' to 'tau4': the reaction time of each network participant, a real value within the range 0.5 to 10 ('tau1' corresponds to the supplier node, 'tau2' to 'tau4' to the consumer nodes);
        2. 'p1' to 'p4': nominal power produced (positive) or consumed (negative) by each network participant, a real value within the range -2.0 to -0.5 for consumers ('p2' to 'p4'). As the total power consumed equals the total power generated, p1 (supplier node) = - (p2 + p3 + p4);
        3. 'g1' to 'g4': price elasticity coefficient for each network participant, a real value within the range 0.05 to 1.00 ('g1' corresponds to the supplier node, 'g2' to 'g4' to the consumer nodes; 'g' stands for 'gamma');
        
        Dependent variables:

        1. 'stab': the maximum real part of the characteristic differentia equation root (if positive, the system is linearly unstable; if negative, linearly stable);
        2. 'stabf': a categorical (binary) label ('stable' or 'unstable').

    ''')
   
    st.subheader('Sample of Dataset')
    data = pd.read_csv('smart_grid_stability_augmented.csv')
    st.dataframe(data)
    
