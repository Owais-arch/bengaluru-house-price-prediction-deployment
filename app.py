import streamlit as st
import numpy as np
import json
import pickle
import gzip

# Load model
with gzip.open("bangalore_house_model.pkl.gz", "rb") as f:
    model = pickle.load(f)

# Load column information
with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

# Extract location names
locations = [col.replace("location_", "") for col in data_columns if "location_" in col]

# Streamlit UI
st.title("🏠 Bengaluru House Price Prediction")

st.write("Enter house details to estimate price")

sqft = st.number_input("Total Square Feet", min_value=300)
bath = st.number_input("Bathrooms", min_value=1)
bhk = st.number_input("BHK", min_value=1)

location = st.selectbox("Location", locations)

if st.button("Predict Price"):

    x = np.zeros(len(data_columns))

    # numeric features
    if "total_sqft" in data_columns:
        x[data_columns.index("total_sqft")] = sqft

    if "bath" in data_columns:
        x[data_columns.index("bath")] = bath

    if "bhk" in data_columns:
        x[data_columns.index("bhk")] = bhk

    # location encoding
    loc_col = "location_" + str(location)

    if loc_col in data_columns:
        x[data_columns.index(loc_col)] = 1

    prediction = model.predict([x])[0]

    st.success(f"Estimated House Price: ₹ {round(prediction,2)} Lakhs")
