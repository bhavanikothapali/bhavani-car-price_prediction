import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Car Price Prediction")

# Inputs
year = st.number_input("Car Year", 2000, 2025)

present_price = st.number_input("Present_Price")

kms_driven = st.number_input("Driven_kms")

Fuel_Type = st.selectbox(
    "Fuel Type",
    ['Petrol', 'Diesel', 'CNG']
)

Selling_type = st.selectbox(
    "Selling_type",
    ['Dealer', 'Individual']
)

Transmission = st.selectbox(
    "Transmission",
    ['Manual', 'Automatic']
)

Owner = st.number_input("Number of Previous Owners", 0, 5)

# Encoding
fuel_type = 0 if fuel_type == 'Petrol' else 1

seller_type = 0 if seller_type == 'Dealer' else 1

transmission = 0 if transmission == 'Manual' else 1

# Prediction
if st.button("Predict Price"):

    features = np.array([[
        year,
        present_price,
        kms_driven,
        fuel_type,
        seller_type,
        transmission,
        owner
    ]])

    prediction = model.predict(features)

    st.success(
        f"Predicted Car Price: {prediction[0]:.2f} Lakhs"
    )
