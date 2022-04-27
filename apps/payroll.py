import streamlit as st
import pandas as pd
import numpy as np

from objects.Employee import Employee
from objects.Manager import Manager
from objects.Executive import Executive
from objects.DataBag import DataBag

def app():

    list_all, pay_emp, pay_man, pay_exec = st.columns([1.5, 2, 2, 2])
    run_all, max_paid, list_name, list_salary = st.columns([1.5, 2, 2, 2])
    load_data, clear_page, exit_app = st.columns([2 , 1.5, 1.5])

    with list_all:
        list_all = st.button("List All")

    with pay_emp:   
        pay_emp = st.button("Pay Employees")

    with pay_man:
        pay_man = st.button("Pay Managers")

    with pay_exec:
        pay_exec = st.button("Pay Executives")

    with run_all:
        run_all = st.button("Pay All")

    with max_paid:
        max_paid = st.button("Highest Earner")

    with list_name:
        list_name = st.button("List by Name")

    with list_salary:
        list_salary = st.button("List by Salary")

    with load_data:
        load_data = st.button("Load DataBag")

    with clear_page:
        clear_page = st.button("Clear")

    with exit_app:
        exit_app = st.button("Exit")

    
    if list_all:

        ### initialize arrays for input into Pandas DataFrame
        id = []
        names = []
        dept = []
        salary = []
        bonus = []

        ### read Employees from DataBag stored in session state key
        for i in st.session_state.key:
            if i.getType() == "Employee" or i.getType() == "Manager":
                id.append(i.getID())
                names.append(i.getName())
                dept.append(i.getDept())
                salary.append(i.getSalary())
                bonus.append(0)
                
            else:
                id.append(i.getID())
                names.append(i.getName())
                dept.append(i.getDept())
                salary.append(i.getSalary())
                bonus.append(i.getBonus())
                
        ### add values to Pandas DataFrame
        data = pd.DataFrame({
        'ID': id,
        'Employee Name': names,
        'Department': dept,
        'Salary': salary,
        'Bonus': bonus})

        st.success("Data Loaded")
        st.dataframe(data=data, width=577, height=500)

    if pay_emp:
        pass

    if pay_man:
        pass

    if pay_exec:
        pass

    if run_all:
        pass

    if max_paid:
        pass

    if list_name:
        pass

    if list_salary:
        pass

    if load_data:
        pass

    if clear_page:
        pass

    if exit_app:
        pass