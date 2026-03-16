import streamlit as st
import pickle
import pandas as pd
import numpy as np

# load model
rf = pickle.load(open("bangalore_house_model.pkl.gz", "rb"))

st.title("Bangalore House Price Prediction")

st.write("Enter house details")

# user inputs
area_type = st.number_input("Area Type", min_value=0)
availability = st.number_input("Availability", min_value=0)
society = st.number_input("Society", min_value=0)
total_sqft = st.number_input("Total Sqft", min_value=300)
bath = st.number_input("Bathrooms", min_value=1)
balcony = st.number_input("Balcony", min_value=0)
bhk = st.number_input("BHK", min_value=1)

bath_per_bhk = bath / bhk if bhk != 0 else 0

# location input
location_number = st.number_input("Location Number (1-1220)", min_value=1, max_value=1220)

if st.button("Predict Price"):

    # create empty dataframe with all columns
    columns = [
        'area_type','availability','society','total_sqft',
        'bath','balcony','bhk','bath_per_bhk'
    ]

    # add location columns
    for i in range(1,1221):
        columns.append(f'location_{i}')

    input_data = pd.DataFrame(np.zeros((1,len(columns))), columns=columns)

    # fill values
    input_data['area_type'] = area_type
    input_data['availability'] = availability
    input_data['society'] = society
    input_data['total_sqft'] = total_sqft
    input_data['bath'] = bath
    input_data['balcony'] = balcony
    input_data['bhk'] = bhk
    input_data['bath_per_bhk'] = bath_per_bhk

    # set selected location
    input_data[f'location_{location_number}'] = 1

    prediction = rf.predict(input_data)

    st.success(f"Estimated House Price: ₹ {prediction[0]:.2f} Lakhs")
