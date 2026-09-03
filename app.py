import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Delivery Delay Risk Prediction",
    page_icon="🚚",
    layout="wide"
)
model = joblib.load("models/delivery_delay_model.pkl")
scaler = joblib.load("models/delivery_delay_scaler.pkl")

st.title("🚚 Delivery Delay Risk Prediction")

st.write(
    "Predict whether a delivery is at risk of being delayed "
    "using Logistic Regression."
)
