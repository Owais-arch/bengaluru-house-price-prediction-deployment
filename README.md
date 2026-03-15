# bengaluru-house-price-prediction-deployment
Machine Learning project to predict house prices in Bengaluru using regression models.
# 🏠 Bengaluru House Price Prediction

## 📌 Project Overview

This project predicts house prices in Bengaluru using Machine Learning techniques.
The goal is to build a regression model that estimates the price of a house based on features such as square footage, number of bedrooms, bathrooms, and location.

This project demonstrates a complete **end-to-end Data Science workflow**, including data cleaning, feature engineering, model training, and deployment using Streamlit.

---

## 📊 Dataset

The dataset contains information about residential properties in Bengaluru.

### Features used in the dataset:

* **location** – Area in Bengaluru
* **total_sqft** – Total area of the house in square feet
* **bath** – Number of bathrooms
* **bhk** – Number of bedrooms
* **price** – Target variable (house price in lakhs)

---

## ⚙️ Project Workflow

 Data Collection
 Data Cleaning
 Feature Engineering
 One-Hot Encoding for categorical variables
 Model Training using Regression Algorithms
 Model Evaluation
 Model Deployment using Streamlit

---

## 🤖 Machine Learning Model

The following algorithms were explored:

* Linear Regression
* Random Forest Regressor

Linear Regression was used as the final model for prediction.

---

## 📈 Model Evaluation

The model performance was evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
bengaluru-house-price-prediction
│
├── Bengaluru_House_Data.csv
├── house_price_prediction.ipynb
├── bangalore_house_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/bengaluru-house-price-prediction.git
```

2️⃣ Install dependencies

```
pip install -r requirements.txt
```

3️⃣ Run the Streamlit app

```
streamlit run app.py
```

The app will open in your browser.

---

## 📷 Application Preview

The Streamlit app allows users to input house details such as:

* Square Feet
* Number of Bathrooms
* Number of Bedrooms

It then predicts the **estimated house price in Bengaluru**.

---

## 📚 Learning Outcomes

Through this project I learned:

* Data preprocessing and cleaning
* Handling missing values
* Feature engineering techniques
* Regression modeling
* Model deployment using Streamlit

---

## 👨‍💻 Author

**Mohammed Owais Bangi**

Aspiring Data Scientist

---

## ⭐ If you like this project

Give it a star on GitHub!
