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

    
    st.subheader("Employee Table:")

    with st.form(key="empForm"):

        #st.write(pd.DataFrame({
        #'ID': [1, 2, 3, 4],
        #'Employee': [10, 20, 30, 40],
        #'Salary': [10, 20, 30, 40]}))

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
        
        #st.table(data)
        st.dataframe(data=data, width=650, height=500)

<<<<<<< HEAD
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
=======
        empID, empName = st.columns([2,2])
        inID = empID.text_input("ID:")
        inName = empName.text_input("Name:") 

        empDept, emplSal = st.columns([2,2])
        inDept = empDept.text_input("Department:")
        inSal = emplSal.text_input("Salary:")

        add_empl, update_empl, delete_empl = st.columns([.5,.5,.5])

        with add_empl:
            add_empl = st.form_submit_button("Add New")

        with update_empl:   
            update_empl = st.form_submit_button("Update")

        with delete_empl:
            delete_empl = st.form_submit_button("Delete")


        if add_empl:
<<<<<<< HEAD
            st.success(name)
>>>>>>> 32798dd1cbf505b78500bad7ba5f52a2c30a814f
=======
            st.session_state.key.add(Employee(len(st.session_state.key) + 1, inName, inDept, int(inSal)))
            st.success("Employee Added")

        #if update_empl:
        #    for i in db:
        #        if i.getID() == id:
        #            st.success("yes")

        if delete_empl:
            for i in st.session_state.key:
                if i.getID() == inID:
                    st.success("finally")
                
>>>>>>> ee17b22401ae999a6c30f750e88c708d68294c99
