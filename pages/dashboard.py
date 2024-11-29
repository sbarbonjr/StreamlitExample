import streamlit as st

st.set_page_config(page_title="UniTS - MLOps",
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

st.title("Test")

if st.button("Click!!!"):
    st.markdown("Clicked!")
