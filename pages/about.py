import streamlit as st

st.set_page_config(page_title="UniTS - MLOps",
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items={"About": "# *Just a message*"}
                   )

st.title("Streamlit: MLOps")
st.header(":blue[Header Examples]")
st.subheader(":red[Sub Header]")
st.text("This is a text component")
st.write(st.__version__)