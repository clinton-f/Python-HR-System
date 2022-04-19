import streamlit as st
import pandas as pd
import numpy as np

def app():
    #st.title("Employee data goes under here.")

    # Info Alert
    #st.info("Some info!")

    # Warning Alert
    #st.warning("Text warning!")

    
    st.subheader("Executive Table:")

    
    with st.form(key="form3"):

        #st.write(pd.DataFrame({
        #'ID': [1, 2, 3, 4],
        #'Employee': [10, 20, 30, 40],
        #'Salary': [10, 20, 30, 40]}))

        data = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Employee Name': ['Sam', 'Shawn', 'Brook', 'Lucy'],
        'Salary': [1021234, 222343, 32222, 42123],
        'Deparment': ['CSC', 'CSC', 'CSC', 'CSC'],
        'Bonus': ['5000', '4500', '1000', '7300']})
        
        st.table(data)

        firstname, emplSal, dept, bonus = st.beta_columns([2,2,2,2])
        firstname.text_input("Name:") 
        emplSal.text_input("Salary:")
        dept.text_input("Department:")
        bonus.text_input("Bonus:")
        
        submit_exec = st.form_submit_button("Submit")

        if submit_exec:
            st.success("Executive data was submitted!")


