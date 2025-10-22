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
    st.title("🩺 Heart Disease Prediction")
    st.markdown("---")

    # --- INPUT FORM SETUP ---
    # Create containers for a clean, two-column layout
    col1, col2 = st.columns(2)

    # --- Demographic and Core Vitals (Column 1) ---
    with col1:
        st.subheader("Patient Vitals")
        
        # Age Slider
        age = st.slider("Age (in years)", min_value=29, max_value=77, value=50, step=1)
        
        # Sex Radio Button (1=Male, 0=Female)
        sex_map = {"Male": 1, "Female": 0}
        sex_label = st.radio("Sex", options=list(sex_map.keys()), index=0)
        sex = sex_map[sex_label]

        # Resting Blood Pressure (trestbps)
        resting_bp = st.number_input("Resting Blood Pressure (trestbps) in mmHg", min_value=94, max_value=200, value=130, step=1)

        # Serum Cholestrol (cholestrol)
        cholestrol = st.number_input("Serum Cholestrol (chol) in mg/dl", min_value=126, max_value=564, value=240, step=1)

    # --- Cardiac Data and Other Risk Factors (Column 2) ---
    with col2:
        st.subheader("Cardiac Risk Factors")

        # Chest Pain Type (cp) - Categorical
        cp_map = {"Typical Angina (Type 0)": 0, "Atypical Angina (Type 1)": 1, "Non-Anginal Pain (Type 2)": 2, "Asymptomatic (Type 3)": 3}
        cp_label = st.selectbox("Chest Pain Type (cp)", options=list(cp_map.keys()), index=2)
        chest_pain_type = cp_map[cp_label]

        # Fasting Blood Sugar (fbs) - Binary
        fbs_map = {"> 120 mg/dl (1)": 1, "<= 120 mg/dl (0)": 0}
        fbs_label = st.radio("Fasting Blood Sugar > 120 mg/dl?", options=list(fbs_map.keys()), index=1)
        fasting_blood_sugar = fbs_map[fbs_label]
        
        # Resting ECG (restecg) - Categorical
        restecg_map = {"Normal (0)": 0, "ST-T Wave Abnormality (1)": 1, "Left Ventricular Hypertrophy (2)": 2}
        restecg_label = st.selectbox("Resting Electrocardiographic Results (restecg)", options=list(restecg_map.keys()), index=1)
        resting_ecg = restecg_map[restecg_label]
        
        # Max Heart Rate (thalach)
        max_heart_rate = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=71, max_value=202, value=153, step=1)
        
        # Exercise Induced Angina (exang) - Binary
        exang_map = {"Yes (1)": 1, "No (0)": 0}
        exang_label = st.radio("Exercise Induced Angina (exang)", options=list(exang_map.keys()), index=1)
        exercise_induced_angina = exang_map[exang_label]

    # --- Additional Data (Full Width) ---
    st.markdown("---")
    st.subheader("Stress and Blood Flow")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        # ST depression induced by exercise relative to rest (oldpeak)
        oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=6.2, value=0.8, step=0.1)

    with col4:
        # The slope of the peak exercise ST segment (slope)
        slope_map = {"Upsloping (0)": 0, "Flat (1)": 1, "Downsloping (2)": 2}
        slope_label = st.selectbox("Peak Exercise ST Segment Slope (slope)", options=list(slope_map.keys()), index=2)
        slope = slope_map[slope_label]

    with col5:
        # Number of major vessels (ca) and Thalassemia (thal) - The model only uses a renamed 'ca' and 'thalassemia' as per analysis.
        ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", options=[0, 1, 2, 3, 4], index=0)
        
        thalassemia_map = {"Normal (1)": 1, "Fixed Defect (2)": 2, "Reversible Defect (3)": 3}
        thalassemia_label = st.selectbox("Thalassemia (thalassemia)", options=list(thalassemia_map.keys()), index=1)
        thalassemia = thalassemia_map[thalassemia_label]
        

    # --- PREDICTION BUTTON & LOGIC ---
    st.markdown("---")
    
    if st.button("Analyze Risk", use_container_width=True, type="primary"):
        # 1. Create a DataFrame from user inputs
        user_data = pd.DataFrame([[age, sex, chest_pain_type, resting_bp, cholestrol, fasting_blood_sugar, 
                                    resting_ecg, max_heart_rate, exercise_induced_angina, oldpeak, 
                                    slope, ca, thalassemia]],
                                  columns=['age', 'sex', 'chest_pain_type', 'resting_bp', 'cholestrol', 
                                           'fasting_blood_sugar', 'resting_ecg', 'max_heart_rate', 
                                           'exercise_induced_angina', 'oldpeak', 'slope', 'ca', 'thalassemia'])

        # 2. Make Prediction and Get Probability
        prediction = model.predict(user_data)[0]
        # Get probability for class 1 (Heart Disease) - this provides a risk score
        prediction_proba = model.predict_proba(user_data)[0][1] 
        
        # 3. Determine Risk Level
        risk_percentage = prediction_proba * 100
        
        if prediction == 1:
            st.success("✅ **Prediction: High Likelihood of Heart Disease**")
            st.warning(f"⚠️ **Risk Score: {risk_percentage:.2f}%**")
            
            if risk_percentage > 75:
                 risk_message = "This risk level is very high. Immediate consultation with a cardiologist is strongly recommended."
            else:
                 risk_message = "The model indicates a significant likelihood of heart disease. Please seek professional medical advice for confirmation and guidance."
            
            st.markdown(f"<p style='color: red; font-weight: bold;'>{risk_message}</p>", unsafe_allow_html=True)
            
        else:
            st.success("🎉 **Prediction: Low Likelihood of Heart Disease**")
            st.info(f"⬇️ **Risk Score: {risk_percentage:.2f}%**")

            if risk_percentage < 25:
                 risk_message = "Maintain a healthy lifestyle, but the current data suggests a low risk."
            else:
                 risk_message = "The likelihood is low, but a small risk remains. Consider general wellness checkups."
                 
            st.markdown(f"<p style='color: green;'>{risk_message}</p>", unsafe_allow_html=True)

        st.markdown("---")
        st.caption("*Disclaimer: This is a machine learning prediction and not a substitute for professional medical diagnosis.*")
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
