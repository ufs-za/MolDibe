# Purchase Intention Prediction App

This app is a **Machine Learning-powered tool for predicting purchase intention** based on various user inputs. Built with Streamlit, this app uses a pre-trained Random Forest model to evaluate user responses on multiple factors such as customer trust, price sensitivity, perceived product quality, perceived value, shopping frequency, and store layout. The prediction provides insight into the likelihood of a purchase intention, with an accompanying confidence score.

## Features

- **Prediction of Purchase Intention**: The app predicts whether a customer is likely to have high or low purchase intention based on user input.
- **Feedback Mechanism**: After receiving a prediction, users can submit feedback on the accuracy of the prediction, allowing continuous improvement.
- **Interactive Input Forms**: Users input information on various factors like customer trust, price sensitivity, perceived product quality, and more.
- **User-Friendly Interface**: The app is built with a clean layout using Streamlit, featuring custom styling to enhance the visual appeal and hide extraneous elements.

## How It Works

The app uses a pre-trained Random Forest model (`random_forest_model.pkl`) to make predictions. Here’s an outline of its workflow:

1. **User Inputs**: The user enters responses to various questions relating to their perception and experience with a grocery store.
2. **Prediction**: When the "Predict Purchase Intention" button is clicked, the app takes the inputs, processes them through the Random Forest model, and displays a prediction with a confidence score.
3. **Feedback**: After viewing the prediction, the user has the option to provide feedback, which can be used to further refine the model.

## Installation

To run the app locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>

pip install -r requirements.txt

streamlit run streamlit_app.py

## Required Packages
streamlit

pandas

numpy

scikit-learn


