import streamlit as st
import pickle
import numpy as np
import gzip



with gzip.open("bangalore_house_model.pkl.gz", "rb") as f:
    rf = pickle.load(f)

st.title("Bangalore House Price Prediction")

area_type = st.number_input("Area Type")
availability = st.number_input("Availability")
location = st.number_input("Location")
society = st.number_input("Society")
total_sqft = st.number_input("Total Sqft")
bath = st.number_input("Bathrooms")
balcony = st.number_input("Balconies")
bhk = st.number_input("BHK")

if st.button("Predict Price"):
    
    prediction = rf.predict([[area_type,availability,location,society,total_sqft,bath,balcony,bhk]])
    
    st.success(f"Estimated House Price: ₹ {prediction[0]} Lakhs")
