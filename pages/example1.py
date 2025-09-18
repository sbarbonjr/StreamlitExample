import streamlit as st

st.set_page_config(page_title="UEL - MLOps",
                   page_icon=None,
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

st.title("Streamlit: MLOps")
st.header(":red[Example 1]")

html_string = ("<p> " +
               "<ul>" +
               "    <li>Item 1</li>" +
               "    <li>Item 2</li>" +
               "    <li>Item 3</li>" +
               "</ul>"+
               "</p>")

st.write(html_string, unsafe_allow_html=True)



