%%writefile app.py
import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('linear_regression_model.sav')

st.title('Sales Prediction App')
st.write('Enter the advertising budgets to predict sales.')

# Input fields for features
tv_budget = st.number_input('TV Advertising Budget', min_value=0.0, max_value=300.0, value=150.0, step=0.1)
radio_budget = st.number_input('Radio Advertising Budget', min_value=0.0, max_value=50.0, value=25.0, step=0.1)
newspaper_budget = st.number_input('Newspaper Advertising Budget', min_value=0.0, max_value=120.0, value=30.0, step=0.1)


if st.button('Predict Sales'):
    # Create a DataFrame for prediction (model was trained with feature names)
    input_data = pd.DataFrame([{
        'TV': tv_budget,
        'Radio': radio_budget,
        'Newspaper': newspaper_budget
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success(f'Predicted Sales: {prediction:.2f}')
