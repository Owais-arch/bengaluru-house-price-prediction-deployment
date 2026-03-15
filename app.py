import streamlit as st
import pickle
import json
import numpy as np

# -----------------------------
# Load model and columns
# -----------------------------
import gzip


with gzip.open("bangalore_house_model.pkl.gz", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

# -----------------------------
# Extract categorical options
# -----------------------------
locations = [col.replace("location_", "") for col in data_columns if col.startswith("location_")]
area_types = [col.replace("area_type_", "") for col in data_columns if col.startswith("area_type_")]
availability_types = [col.replace("availability_", "") for col in data_columns if col.startswith("availability_")]
societies = [col.replace("society_", "") for col in data_columns if col.startswith("society_")]

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏠 Bengaluru House Price Prediction")

st.write("Fill the details below to estimate house price")

sqft = st.number_input("Total Square Feet", min_value=300)
bath = st.number_input("Number of Bathrooms", min_value=1)
balcony = st.number_input("Number of Balconies", min_value=0)
bhk = st.number_input("BHK", min_value=1)

location = st.selectbox("Location", locations)
area_type = st.selectbox("Area Type", area_types)
availability = st.selectbox("Availability", availability_types)
society = st.selectbox("Society", societies)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    x = np.zeros(len(data_columns))

    # numeric features
    if "total_sqft" in data_columns:
        x[data_columns.index("total_sqft")] = sqft

    if "bath" in data_columns:
        x[data_columns.index("bath")] = bath

    if "balcony" in data_columns:
        x[data_columns.index("balcony")] = balcony

    if "bhk" in data_columns:
        x[data_columns.index("bhk")] = bhk

    # categorical encoding
    loc_col = "location_" + location
    if loc_col in data_columns:
        x[data_columns.index(loc_col)] = 1

    area_col = "area_type_" + area_type
    if area_col in data_columns:
        x[data_columns.index(area_col)] = 1

    avail_col = "availability_" + availability
    if avail_col in data_columns:
        x[data_columns.index(avail_col)] = 1

    soc_col = "society_" + society
    if soc_col in data_columns:
        x[data_columns.index(soc_col)] = 1

    prediction = model.predict([x])[0]

    st.success(f"Estimated House Price: ₹ {round(prediction,2)} Lakhs")
