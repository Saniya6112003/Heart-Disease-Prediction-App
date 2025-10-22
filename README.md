

# 💓 HeartWise: Heart Disease Risk Predictor

## Live Application
Experience the app live: https://heart-disease-prediction-app-by-saniya.streamlit.app/

## 🌟 Overview

 HeartWise is a user-friendly, interactive web application built with Streamlit and Machine Learning to provide a preliminary assessment of heart disease risk. By analyzing 13 key clinical features (derived from the UCI Heart Disease dataset), the app helps individuals and healthcare professionals quickly visualize data and estimate a patient's likelihood of having heart disease.

This tool aims to offer an accessible way to understand individual risk factors and serves as a powerful demonstration of predictive analytics in a public health context.

## ✨ Features

Prediction Model: Use an integrated Logistic Regression Model to generate a risk prediction (Positive/Negative) and a continuous Risk Score (percentage).

Interactive Input: A clean, multi-column Streamlit interface allows users to input various health metrics via sliders, number inputs, and dropdowns.

Data Visualization: The Dashboard section provides key Exploratory Data Analysis (EDA) charts to understand the dataset's characteristics, including:

Target Distribution (showing the data is balanced).

Age Distribution histogram.

Scatter plots of Resting Blood Pressure vs. Cholestrol, and Max Heart Rate vs. Resting BP.

Creative UI/UX: Uses custom components like streamlit-lottie for engaging animations and streamlit-option-menu for sleek sidebar navigation.

## 🛠️ Model and Technical Details 

Machine Learning Model

Algorithm: Logistic Regression

Model Training: The model was trained using a standard 70/30 split of the cleaned data, and the class_weight was set to 'balanced' to handle potential class imbalance (though the EDA shows the data is balanced).

Training Accuracy: $87.20\%$

Testing Accuracy: $83.52\%$

F1 Score (Test): $84.54\%$

Model Persistence: The trained Logistic Regression model is saved as a serialized file, Log_model.pkl, for deployment.

## 🤝 Connect & Collaborate
I'm Saniya, the developer behind this project! I'm passionate about deploying useful machine learning tools and welcome your engagement.

Developer: Saniya

Contribute: Found a bug or have an idea for a feature? Please don't hesitate to open an Issue or submit a Pull Request right here in the repository!

## Let's Connect:
LinkedIn : https://www.linkedin.com/in/saniya-randive374628/
