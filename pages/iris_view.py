import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris  # Utilizzo di un dataset predefinito come esempio

# Function to load the saved model
def load_model():
    with open('model/iris_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load model (assuming it's a RandomForestClassifier)
model = load_model()

# Load sample data to fit PCA
iris = load_iris()
species = ['Setosa', 'Versicolor', 'Virginica']

X = iris.data
y = iris.target  # True labels for the Iris dataset

# Fit the PCA on the dataset
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)  # Fit and transform the dataset with PCA

# Streamlit interface setup
st.title('Iris Flower Prediction')
st.write('Please enter the following features to predict the Iris flower type:')

# Input fields for user to provide feature values
input_sepal_length = st.slider('Sepal Length', 0.0, 10.0, 5.0)
input_sepal_width = st.slider('Sepal Width', 0.0, 10.0, 3.0)
input_petal_length = st.slider('Petal Length', 0.0, 10.0, 2.0)
input_petal_width = st.slider('Petal Width', 0.0, 10.0, 1.0)

# Function to predict Iris class based on user input
def predict_iris_class(sepal_length, sepal_width, petal_length, petal_width):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    return prediction

# Button to trigger the prediction for Iris class
if st.button('Predict'):
    prediction = predict_iris_class(input_sepal_length, input_sepal_width, input_petal_length, input_petal_width)[0]
    st.write(f'Predicted Iris Species ({prediction}): {species[int(prediction)]}')

# Button to trigger the PCA plot visualization
if st.button('Predict Group'):
    # Prepare the input array
    input_data = np.array([[input_sepal_length, input_sepal_width, input_petal_length, input_petal_width]])
    
    # Predict the class (not clusters) and assign the prediction as the cluster label
    cluster = model.predict(input_data)
    
    # Project the input data to the PCA space
    input_data_pca = pca.transform(input_data)

    # Create a DataFrame for the PCA results using true class labels
    df_pca = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
    df_pca['True Class'] = y  # Assign true labels for color coding

    # Plot the PCA results
    plt.figure(figsize=(8, 6))
    plt.scatter(df_pca['PCA1'], df_pca['PCA2'], c=df_pca['True Class'], cmap='viridis', marker='o', alpha=0.5)
    plt.scatter(input_data_pca[0, 0], input_data_pca[0, 1], color='red', marker='X', s=200, label='New Sample')
    plt.title('PCA of Iris Dataset with True Labels')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.legend()
    
    # Show the plot in Streamlit
    st.pyplot(plt)
    
    # Display the predicted cluster (class in this context)
    st.write(f"The predicted class for the input Iris flower is: **{species[int(cluster[0])]}**")