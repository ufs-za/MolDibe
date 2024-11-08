import subprocess
import sys

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install necessary packages
try:
    import sklearn
except ImportError:
    install("scikit-learn")

import pandas as pd
import streamlit as st
import numpy as np

# Load the Random Forest model from the Pickle file
model = pd.read_pickle("random_forest_model.pkl")

# Define the function for predicting Purchase Intention
def predict_purchase_intention(inputs):
    prediction = model.predict([inputs])
    prediction_proba = model.predict_proba([inputs])
    confidence = np.max(prediction_proba)
    return prediction, confidence

# Create styling to hide menu options and "made by streamlit" as well as making background white
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    textarea {
        background-color: white !important;
        color: black !important;
    }
    .big-font {
        font-size:20px !important;
    }
</style>
"""

# We set the page configuration to change the title and image of the page and set the layout to wide
st.set_page_config(page_title ='Purchase Intention Prediction')

# Inject the custom CSS into the Streamlit app
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set up the Streamlit app title
st.title("Purchase Intention Prediction App")

# Create a header
st.header("Please input the following information:")

# Initialize session state variables for feedback flow if not already initialized
if 'show_feedback' not in st.session_state:
    st.session_state['show_feedback'] = False
if 'show_feedback_box' not in st.session_state:
    st.session_state['show_feedback_box'] = False

# Define additional inputs from the SECOND CODE
st.write("**CUSTOMER TRUST**")
question_1 = st.number_input("The grocery store’s offerings are worth the money I spend", 1, 5)
question_2 = st.number_input("The grocery store helps me save time", 1, 5)

st.write("**PRICE SENSITIVITY**")
question_3 = st.number_input("I am willing to pay a higher price for the benefit of having the grocery store located close to me", 1, 5)
question_4 = st.number_input("The grocery store’s environment feels safe and secure", 1, 5)

st.write("**PERCEIVED PRODUCT QUALITY**")
question_5 = st.number_input("The overall quality of products I buy from the grocery store is good", 1, 5)
question_6 = st.number_input("The quality of in-store bakery is good", 1, 5)

st.write("**PERCEIVED VALUE**")
question_7 = st.number_input("The grocery store products are affordable", 1, 5)
question_8 = st.number_input("In this grocery store, compared to other stores outside the township, I can save money", 1, 5)

st.write("**SHOPPING FREQUENCY**")
question_9 = st.number_input("How often do customers shop", 1, 5)

st.write("**STORE LAYOUT**")
question_10 = st.number_input("The overall layout of the store", 1, 5)

# Prepare the user inputs for prediction (no scaling)
user_input = np.array([
    question_1, question_2, question_3, question_4, question_5, question_6, 
    question_7, question_8, question_9, question_10
])

# A prediction is made when the user clicks the "Predict Purchase Intention" button
if st.button('Predict Purchase Intention'):
    prediction, confidence = predict_purchase_intention(user_input)
    st.subheader(f"Predicted Purchase Intention Level: {prediction[0]}")
    st.write(f"Prediction Confidence: {confidence * 100:.2f}%")

    # Reveal "Give Feedback" link
    st.session_state['show_feedback'] = True

# Show feedback link if predictions are made
if st.session_state['show_feedback']:
    if st.button("Give Feedback"):
        st.session_state['show_feedback_box'] = True

# Show feedback box if give feedback is clicked for user to input feedback
if st.session_state['show_feedback_box']:
    feedback = st.text_area("Provide feedback on the prediction:")

    if st.button("Submit Feedback"):     
        # Store the feedback in session state
        st.session_state['feedback'] = feedback

        # Immediately close the feedback dialog after submitting
        st.session_state['show_feedback_box'] = False
        st.session_state['show_feedback'] = False
        
        # Optionally show feedback confirmation
        st.success("Thank you for your feedback!")

        # Rerun the app after submission to reset the button
        st.rerun()
