import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing

def get_plot_correlation(corr):
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='crest', linewidths=.5)
    plt.title('Correlation Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    return plt

def get_plot_histogram(df,selected_column,bins):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df.filter([selected_column]), bins=bins, kde=True)
    plt.title('Histogram Plot')
    return plt

# Load the California Housing dataset
data = fetch_california_housing(as_frame=True)
df = data['frame']
corr = df.corr()
get_plot_correlation(corr)
# Streamlit interface setup
st.title('California Housing Dataset Exploration')

# Sidebar with options
st.sidebar.title('Options')
view_data = st.sidebar.checkbox('View Dataset')
plot_histogram = st.sidebar.checkbox('Plot Histograms')
plot_correlation = st.sidebar.checkbox('Plot Correlation Heatmap')
get_plot_correlation(corr)
# Display the dataset
if view_data:
    st.subheader('California Housing Dataset')
    st.write(df)

# Plot histograms
if plot_histogram:
    st.subheader('Histograms of Features')
    bins = st.sidebar.slider('Number of bins:', min_value=5, max_value=50, value=20)
    columns = df.columns.tolist()
    selected_column = st.selectbox('Select a feature for histogram:', columns)
    if selected_column:
        st.pyplot(get_plot_histogram(df, selected_column,bins))

# Plot correlation heatmap
if plot_correlation:
    st.subheader('Correlation Heatmap')
    corr = df.corr()
    st.write(corr)
    st.pyplot(get_plot_correlation(corr))