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

    with st.form(key="empForm"):

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

        #empForm = st.empForm(key="empForm")
        firstName, emplDept, emplSal = st.beta_columns([2,2,2])
        names = firstName.text_input("Name:") 
        dept = emplDept.text_input("Department:")
        salary = emplSal.text_input("Salary:")

        empForm = st.form_submit_button(label='Submit')

        if empForm:
            db.add(Employee(id, names, dept, salary))
            st.success("Employee added!")
            st.write(db)
