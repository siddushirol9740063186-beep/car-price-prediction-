import streamlit as st
import numpy as np
import pickle

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Car Price Prediction", layout="centered")

# -------------------- CUSTOM CSS (Dark UI like your image) --------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.stApp {
    background-color: #0e1117;
    color: white;
}
h1, h2, h3, h4 {
    color: white;
}
.stSlider label, .stSelectbox label {
    color: white !important;
}
.stButton>button {
    background-color: #1f2937;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOAD MODEL --------------------
model = pickle.load(open("model.pkl", "rb"))

# -------------------- HEADER --------------------
st.markdown("## 🚗 Car Price Prediction")
st.write("Predict the resale price of a car based on details")

st.markdown("### Enter Input Values")

# -------------------- INPUTS --------------------
year = st.slider("Year of Purchase", 2000, 2025, 2015)

present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0, 5.0)

kms_driven = st.number_input("Kilometers Driven", 0, 300000, 50000)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

# -------------------- ENCODING --------------------
fuel_petrol = 1 if fuel_type == "Petrol" else 0
fuel_diesel = 1 if fuel_type == "Diesel" else 0

seller_individual = 1 if seller_type == "Individual" else 0
transmission_manual = 1 if transmission == "Manual" else 0

car_age = 2025 - year

# -------------------- PREDICT --------------------
if st.button("Predict"):
    input_data = np.array([[present_price, kms_driven, owner,
                            car_age, fuel_diesel, fuel_petrol,
                            seller_individual, transmission_manual]])

    prediction = model.predict(input_data)

    st.success(f"Estimated Car Price: ₹ {round(prediction[0], 2)} Lakhs")

# -------------------- FOOTER --------------------
st.markdown("---")
st.write("Built with ❤️ using Machine Learning & Streamlit")
