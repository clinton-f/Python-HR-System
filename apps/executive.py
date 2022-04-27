import streamlit as st
import pandas as pd
import numpy as np

from objects.Employee import Employee
from objects.DataBag import DataBag
from objects.Executive import Executive

def app():

    ### initialize arrays for input into Pandas DataFrame
    id = []
    names = []
    dept = []
    salary = []
    bonus = []
    amt = 0

    ### read Employees from DataBag stored in session state key
    for i in st.session_state.key:
        if i.getType() == "Executive":
            id.append(i.getID())
            names.append(i.getName())
            dept.append(i.getDept())
            salary.append(i.getSalary())
            bonus.append(i.getBonus())
            amt += 1

    ### add values to Pandas DataFrame
    data = pd.DataFrame({
    'ID': id,
    'Executive Name': names,
    'Department': dept,
    'Salary': salary,
    'Bonus': bonus})
    
    ### create columns and buttons for layout of UI
    empID, empName = st.columns([2,2])
    inID = empID.text_input("ID:")
    inName = empName.text_input("Name:") 

    empDept, emplSal, emplBonus = st.columns([2,2,2])
    inDept = empDept.text_input("Department:")
    inSal = emplSal.text_input("Salary:")
    inBonus = emplBonus.text_input("Bonus:")

    add_empl, update_empl, delete_empl = st.columns([.5,.5,.5])

    with add_empl:
        add_empl = st.button("Add New")

    with update_empl:   
        update_empl = st.button("Update")

    with delete_empl:
        delete_empl = st.button("Delete by ID")

    ### load and initialize Streamlit dataframe with Pandas DataFrame
    frame = st.dataframe(data=data, width=550, height=500)

    if add_empl:
        ### add Employee to DataBag in session state
        st.session_state.key.add(Executive(len(st.session_state.key), inName, inDept, int(inSal), int(inBonus)))

        ### create second Pandas DataFrame to add new elements to table
        data2 = pd.DataFrame({
            'ID': [len(st.session_state.key)],
            'Executive Name': [inName],
            'Department': [inDept],
            'Salary': [int(inSal)],
            'Bonus': [int(inBonus)]
            })
        
        ### concat the two DataFrames
        data = pd.concat([data, data2], ignore_index=True)

        st.success("Executive Added")

        ### clear the Streamlit dataframe and add the new data
        frame.empty()
        frame = st.dataframe(data=data, width=550, height=500)

    if delete_empl:
        ### find Employee in DataBag where ID is matching
        found = False
        for i in st.session_state.key:
            if i.getID() == int(inID):

                ### removed Employee from the DataBag
                st.session_state.key.remove(i)

                st.success("Employee Deleted")

                ### create new Pandas DataFrame and add values in
                id = []
                names = []
                dept = []
                salary = []
                bonus = []

                for i in st.session_state.key:
                    if i.getType() == "Executive":
                        id.append(i.getID())
                        names.append(i.getName())
                        dept.append(i.getDept())
                        salary.append(i.getSalary())
                        bonus.append(i.getBonus())

                data = pd.DataFrame({
                    'ID': id,
                    'Executive Name': names,
                    'Department': dept,
                    'Salary': salary,
                    'Bonus': bonus})

                ### clear Streamlit dataframe and replace with new data
                frame.empty()
                frame = st.dataframe(data=data, width=577, height=500)
                
                ### indicate that the Employee was found
                found = True

        ### alert the user if Employee ID cannot be found    
        if not found: st.warning("ID cannot be found")