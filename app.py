import streamlit as st
import pickle
import json
import numpy as np

# Load model
model = pickle.load(open("bangalore_house_model.pkl","rb"))

# Load feature columns
with open("columns.json","r") as f:
    data_columns = json.load(f)["data_columns"]

# Extract categories
locations = [col.replace("location_","") for col in data_columns if col.startswith("location_")]
area_types = [col.replace("area_type_","") for col in data_columns if col.startswith("area_type_")]
availability_types = [col.replace("availability_","") for col in data_columns if col.startswith("availability_")]
societies = [col.replace("society_","") for col in data_columns if col.startswith("society_")]

st.title("🏠 Bengaluru House Price Prediction")

st.write("Enter house details")

# Numeric inputs
sqft = st.number_input("Total Square Feet", min_value=300)
bath = st.number_input("Bathrooms", min_value=1)
balcony = st.number_input("Balcony", min_value=0)
bhk = st.number_input("BHK", min_value=1)

# Categorical inputs
location = st.selectbox("Location", locations)
area_type = st.selectbox("Area Type", area_types)
availability = st.selectbox("Availability", availability_types)
society = st.selectbox("Society", societies)

if st.button("Predict Price"):

    x = np.zeros(len(data_columns))

    x[data_columns.index("total_sqft")] = sqft
    x[data_columns.index("bath")] = bath
    x[data_columns.index("balcony")] = balcony
    x[data_columns.index("bhk")] = bhk

    # location encoding
    loc_col = "location_" + location
    if loc_col in data_columns:
        x[data_columns.index(loc_col)] = 1

    # area_type encoding
    area_col = "area_type_" + area_type
    if area_col in data_columns:
        x[data_columns.index(area_col)] = 1

    # availability encoding
    avail_col = "availability_" + availability
    if avail_col in data_columns:
        x[data_columns.index(avail_col)] = 1

    # society encoding
    soc_col = "society_" + society
    if soc_col in data_columns:
        x[data_columns.index(soc_col)] = 1

    prediction = model.predict([x])[0]

    st.success(f"Estimated House Price: ₹ {round(prediction,2)} Lakhs")
