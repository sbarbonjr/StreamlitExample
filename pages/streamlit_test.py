import streamlit as st
import numpy as np

if "list_numbers" not in st.session_state:
    st.session_state["list_numbers"] = [0]

st.write("Dealing with numbers!")

tab_navigation = st.tabs(["New Number", "Data", "Statistics"])

with tab_navigation[0]:
    value = np.round(st.number_input("Insert a nunber"),2)
    st.write("My number is ", value)
    if st.button("Add Number"):
        st.session_state["list_numbers"].append(value)
with tab_navigation[1]:
    st.dataframe(st.session_state["list_numbers"], use_container_width=True)
with tab_navigation[2]:
    max_value = str(np.max(st.session_state["list_numbers"]))
    min_value = str(np.min(st.session_state["list_numbers"]))
    
    st.markdown("**Mean Value**: :red[" + str(np.round(np.mean(st.session_state["list_numbers"]),2))+"]")
    st.markdown("**Std. Deviation**: :red["+str(np.round(np.std(st.session_state["list_numbers"]),2))+"]")
    st.write("**Min. Value**: "+min_value)
    st.markdown("**Max. Value**:"+max_value)

