import streamlit as st
import pandas as pd
import joblib

model = joblib.load('churn_model.pkl')

st.title("Bank Churn Prediction")

credit_score = st.number_input("Credit Score", 300, 850, 600)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", 18, 100, 35)
tenure = st.slider("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
num_of_products = st.selectbox("NumOfProducts", [1, 2, 3, 4])
has_cr_card = st.selectbox("HasCrCard", [0, 1])
is_active_member = st.selectbox("IsActiveMember", [0, 1])
estimated_salary = st.number_input("EstimatedSalary", 0.0, 200000.0, 50000.0)

if st.button("Predict"):
    
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary]
    })

    input_data['BalanceSalaryRatio'] = input_data['Balance'] / input_data['EstimatedSalary']
    input_data['TenureByAge'] = input_data['Tenure'] / input_data['Age']
    input_data['CreditScoreGivenAge'] = input_data['CreditScore'] / input_data['Age']

    input_data['Geography_Germany'] = 1 if geography == 'Germany' else 0
    input_data['Geography_Spain'] = 1 if geography == 'Spain' else 0
    input_data['Gender_Male'] = 1 if gender == 'Male' else 0
    
    expected_columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 
                        'IsActiveMember', 'EstimatedSalary', 'BalanceSalaryRatio', 'TenureByAge', 
                        'CreditScoreGivenAge', 'Geography_Germany', 'Geography_Spain', 'Gender_Male']
    
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[expected_columns]

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"Churn Prediction: YES (Probability: {probability:.2f})")
    else:
        st.success(f"Churn Prediction: NO (Probability: {probability:.2f})")