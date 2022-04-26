import streamlit as st
import pandas as pd
import numpy as np

from objects.Employee import Employee
from objects.DataBag import DataBag

def app():
    #st.title("Employee data goes under here.")

    # Info Alert
    #st.info("Some info!")

    # Warning Alert
    #st.warning("Text warning!")

    id = []
    names = []
    dept = []
    salary = []
    amt = 0

    for i in st.session_state.key:
        if i.getType() == "Employee":
            id.append(i.getID())
            names.append(i.getName())
            dept.append(i.getDept())
            salary.append(i.getSalary())
            amt += 1

    data = pd.DataFrame({
    'ID': id,
    'Employee Name': names,
    'Department': dept,
    'Salary': salary})
    
    #st.table(data)
    
    empID, empName = st.columns([2,2])
    inID = empID.text_input("ID:")
    inName = empName.text_input("Name:") 

    empDept, emplSal = st.columns([2,2])
    inDept = empDept.text_input("Department:")
    inSal = emplSal.text_input("Salary:")

    add_empl, update_empl, delete_empl = st.columns([.5,.5,.5])

    with add_empl:
        add_empl = st.button("Add New")

    with update_empl:   
        update_empl = st.button("Update")

    with delete_empl:
        delete_empl = st.button("Delete by ID")

    frame = st.dataframe(data=data, width=577, height=500)

    if add_empl:
        st.session_state.key.add(Employee(len(st.session_state.key) + 1, inName, inDept, int(inSal)))

        data2 = pd.DataFrame({
            'ID': [len(st.session_state.key)],
            'Employee Name': [inName],
            'Department': [inDept],
            'Salary': [int(inSal)]})
        
        data = pd.concat([data, data2], ignore_index=True)

        st.success("Employee Added")

        frame.empty()
        frame = st.dataframe(data=data, width=577, height=500)

    if delete_empl:
        for i in st.session_state.key:
            if i.getID() == int(inID):

                st.session_state.key.remove(i)

                st.success("Employee Deleted")

                id = []
                names = []
                dept = []
                salary = []

                for i in st.session_state.key:
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

                frame.empty()
                frame = st.dataframe(data=data, width=577, height=500)

                found = True
            
        if not found: st.warning("Text warning!")