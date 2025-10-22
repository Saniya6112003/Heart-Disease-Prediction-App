import pickle
import json
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Heart Disease predictor",page_icon='💓',
                   layout='wide',initial_sidebar_state='expanded')
#load the data
df = pd.read_csv("cleaned.csv")
df = df.drop("Unnamed: 0",axis=1)

#load the model
with open("Log_model.pkl",'rb') as  file:
    model = pickle.load(file)

#load the anime
def load_anime():
    with open("Heart_beat_anime.json",'rb') as f:
        anime = json.load(f)
        return anime
    
with st.sidebar:
    st.subheader("Heart Disease Predictor")
    option = option_menu(menu_title=None,options=["Home","Predict Disease","Dashboard","Sample Data"],icons=["house","activity","bar-chart","folder"])

if option == 'Home':
    col1,col2 = st.columns(2)
    with col1:
        anime = load_anime()
        st_lottie(anime,width=300)
    with col2:
        with st.container(border=True,height=300):
            st.markdown('''
                        🫀 About This App:

    Heart Disease Prediction App is a user-friendly web application developed using Streamlit and Machine Learning. It is designed to help individuals and healthcare professionals assess the likelihood of heart disease based on input features derived from the UCI Heart Disease dataset.

    📊 Dataset Information:

    This app is based on the publicly available UCI Heart Disease dataset, which contains medical data from real patients. The dataset includes attributes like:

    Age

    Gender

    Chest pain type

    Resting blood pressure

    Cholesterol levels

    Fasting blood sugar

    Electrocardiographic results

    Maximum heart rate achieved

    Exercise-induced angina

    ST depression

    Number of major vessels

    Thalassemia results

    These features are commonly used by cardiologists for diagnosis.
                        
                        ''')
elif option == 'Predict Disease':
    pass
elif option == 'Dashboard':
    with st.container(border=True,height=370):
        a1,a2 = st.columns(2,border=True)
        b1,b2 = st.columns(2,border=True)
        color_code = '#FF4B4B'
        count = df.groupby('target')['target'].count()
        count  = pd.DataFrame(count).rename(columns = {'target':'count'}).reset_index()
        a1.bar_chart(x='target',data=count,color=[color_code],y_label="count",height=300)

        fig = px.histogram(df,x='age',color_discrete_sequence=[color_code],height=300)
        a2.plotly_chart(fig)

        b1.scatter_chart(x='resting_bp',y='cholestrol',data=df,color=[color_code],height=300)

        b2.scatter_chart(x='max_heart_rate',y='resting_bp',data=df,color=[color_code],height=300)
elif option == 'Sample Data':
    st.dataframe(df.sample(50),hide_index=True)