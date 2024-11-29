import streamlit as st
import datetime
from random import random

st.set_page_config(page_title="UniTS - MLOps",
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

st.title("Streamlit: MLOps")
st.header(":green[Example 3]")

with st.form("my_form"):
    st.subheader("Input Data")
    feature_1 = st.text_input("Feature 1")
    feature_2 = st.date_input("Feature 2", value=datetime.datetime(2023, 12, 1))
    feature_3 = st.slider("Feature 3", 1, 15)
    feature_4 = st.radio("Feature 4", ("Value 1", "Value 2"))

    submitted = st.form_submit_button("Predict")

if submitted:
    st.success("Success!")
    output = random()
    st.write("The predicted value is ", output)






