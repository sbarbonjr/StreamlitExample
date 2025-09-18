import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model/iris_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Streamlit interface setup
st.title('Iris Flower Prediction')
st.write('Please enter the following features to predict the Iris flower type:')

# Input fields for user to provide feature values
input_sepal_length = st.slider('Sepal Length', 0.0, 10.0, 5.0)
input_sepal_width = st.slider('Sepal Width', 0.0, 10.0, 3.0)
input_petal_length = st.slider('Petal Length', 0.0, 10.0, 2.0)
input_petal_width = st.slider('Petal Width', 0.0, 10.0, 1.0)

def predict_iris_class(sepal_length, sepal_width, petal_length, petal_width):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    return prediction

# Button to trigger the prediction
if st.button('Predict'):
    prediction = predict_iris_class(input_sepal_length, input_sepal_width, input_petal_length, input_petal_width)[0]
    species = ['Setosa', 'Versicolor', 'Virginica']
    st.write(f'Predicted Iris Species ({prediction}): {species[int(prediction)]}')

