import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Marvellous Infosystems Dashboard")

st.title("Marvellous Infosystems By Piyush Khairnar") 
st.header("Customer Prediction Churn")
st.write("Machine Learning Application Dashboard")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "Marvellous_ML_Customer_Churn.pkl")

model = joblib.load(MODEL_PATH)

st.subheader("Enter Customer Details")

age = st.number_input("Customer Age", min_value=1)
tenure = st.number_input("Tenure (Months)", min_value=0)
charges = st.number_input("Monthly Charges", min_value=0)
calls = st.number_input("Support Calls", min_value=0)

if st.button("Predict Churn"):
    new_customer = pd.DataFrame({
    "Age" : [age],
    "Tenure" : [tenure],
    "MonthlyCharges" : [charges],
    "SupportCalls" : [calls]
    })

    prediction = model.predict(new_customer)[0]

    if prediction == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is unlikely to churn")

st.divider()

st.caption("Marvellous Infosystem Dashboard")
