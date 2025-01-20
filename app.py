import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('credit_card_fraud_detection.pkl')

# Function to make predictions
def predict(features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit UI
st.title('Fraud Detection Model')

# Add an option to select the input mode
input_mode = st.sidebar.selectbox("Select Input Mode", ["Manual Input", "Automatic Generation"])

# Initialize an empty list for features
features = []

if input_mode == "Manual Input":
    st.sidebar.header('Enter the transaction details')
    
    # Collect 28 feature inputs from the user
    for i in range(29):  # Assuming 28 features in your dataset
        feature = st.sidebar.number_input(f'Feature {i+1}', min_value=-10.0, max_value=10.0, value=0.0)
        features.append(feature)

elif input_mode == "Automatic Generation":
    st.sidebar.write("Randomly generated values for the features:")

    # Generate random values for the 28 features (values between -10 and 10)
    features = np.random.uniform(-10.0, 10.0, 29).tolist()  # Generate random numbers for 28 features
    st.sidebar.write(features)  # Show the generated features in the sidebar

# Prediction button
if st.sidebar.button('Predict'):
    prediction = predict(features)

    # Show prediction result
    if prediction == 1:
        st.write("Prediction: Fraudulent Transaction")
    else:
        st.write("Prediction: Non-Fraudulent Transaction")
