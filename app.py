import streamlit as st

st.set_page_config(
    page_title="Delivery Delay Risk Prediction",
    page_icon="🚚",
    layout="wide"
)

st.title("🚚 Delivery Delay Risk Prediction")

st.write(
    "Predict whether a delivery is at risk of being delayed "
    "using Logistic Regression."
)
