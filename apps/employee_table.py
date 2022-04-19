import streamlit as st
import pandas as pd
import numpy as np



def app():
    #st.title("Employee data goes under here.")

    # Info Alert
    #st.info("Some info!")

    # Warning Alert
    #st.warning("Text warning!")

    
    st.subheader("Employee Table:")

    
    with st.form(key="form1"):

        #st.write(pd.DataFrame({
        #'ID': [1, 2, 3, 4],
        #'Employee': [10, 20, 30, 40],
        #'Salary': [10, 20, 30, 40]}))

        data = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Employee Name': ['Sam', 'Shawn', 'Brook', 'Lucy'],
        'Salary': [1021234, 222343, 32222, 42123]})
        
        st.table(data)

        firstname, emplSal = st.beta_columns([2,2])
        firstname.text_input("Name:") 
        emplSal.text_input("Salary:")

        submit_empl = st.form_submit_button("Submit")


        if submit_empl:
            st.success("Employee data was submitted!")