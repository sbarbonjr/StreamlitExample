import streamlit as st

st.set_page_config(page_title="UniTS - MLOps",
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

st.title("Streamlit: MLOps")
st.header(":green[Example 2]")

algorithms_list_1 = ["Random Forest", "Support Vector Machine", "Multilayer Perceptron"]
algorithms_list_2 = ["Decision Tree", "K-nn"]

if st.button("Algorithms 1", type="primary"):
    st.write(algorithms_list_1)

if st.button("Algorithms 2", type="secondary"):
    st.write(algorithms_list_2)






