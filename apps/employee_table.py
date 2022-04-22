import streamlit as st
import pandas as pd
import numpy as np

from objects.Employee import Employee
from objects.DataBag import DataBag
from objects.sourceData import loadData

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

        db = DataBag()
        db = loadData()
        id = []
        names = []
        dept = []
        salary = []

        for i in db:
            if i.getType() == "Employee":
                id.append(i.getID())
                names.append(i.getName())
                dept.append(i.getDept())
                salary.append(i.getSalary())

        data = pd.DataFrame({
        'ID': id,
        'Employee Name': names,
        'Department': dept,
        'Salary': salary})
        
        st.table(data)

        firstname, emplSal = st.columns([2,2])
        firstname.text_input("Name:") 
        emplSal.text_input("Salary:")

        submit_empl = st.form_submit_button("Submit")


        if submit_empl:
            st.success("Employee data was submitted!")