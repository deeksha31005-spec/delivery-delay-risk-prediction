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
st.header("📦 Enter Delivery Details")
distance_km = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=10.0
)

warehouse_load = st.number_input(
    "Warehouse Load",
    min_value=0.0,
    value=3.0
)

order_hour = st.number_input(
    "Order Hour",
    min_value=0.0,
    max_value=23.0,
    value=3.0
)
items_count = st.number_input(
    "Number of Items",
    min_value=0.0,
    value=3.0
)

weather_risk = st.number_input(
    "Weather Risk (1–5)",
    min_value=1.0,
    max_value=5.0,
    value=3.0
)

carrier_delay_rate = st.number_input(
    "Carrier Delay Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)
