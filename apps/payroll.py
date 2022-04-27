import streamlit as st
import pandas as pd
import numpy as np

from objects.Employee import Employee
from objects.Manager import Manager
from objects.Executive import Executive
from objects.DataBag import DataBag
from objects.sourceData import loadData

def app():

    frame = st.empty()

    list_all, pay_emp, pay_man, pay_exec = st.columns([1.5, 2, 2, 2])
    run_all, max_paid, list_name, list_salary = st.columns([1.5, 2, 2, 2])
    load_data, clear_page = st.columns([.5 , 1])

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
    
    if list_all:
        frame.empty()

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
        frame = st.dataframe(data=data, width=577, height=500)

    if pay_emp:
        frame.empty()

        for i in st.session_state.key:
            if i.getType() == "Employee":
                st.write(i.toString() + "  paid: " + str(i.getSalary()))
        
    if pay_man:
        frame.empty()
        
        for i in st.session_state.key:
            if i.getType() == "Manager":
                st.write(i.toString() + "  paid: " + str(i.getSalary()))

    if pay_exec:
        frame.empty()
        
        for i in st.session_state.key:
            if i.getType() == "Executive":
                st.write(i.toString() + "  paid: " + str(i.getSalary() + i.getBonus()))


    if run_all:
        frame.empty()

        for i in st.session_state.key:
            if i.getType() == "Employee" or i.getType() == "Manager":

                st.write(i.toString() + "  paid: " + str(i.getSalary()))
                
            else:
                st.write(i.toString() + "  paid: " + str(i.getSalary() + i.getBonus()))

    if max_paid:
        frame.empty()

        temp = []

        for i in st.session_state.key:
            if len(temp) == 0:
                temp.append(i)
            else:
                if i.getMeasure() > temp[0].getMeasure():
                    temp.pop(0)
                    temp.append(i)
        
        st.write(temp.pop(0).toString())

    if list_name:
        frame.empty()

        a = st.session_state.key.sortByName()

        ### initialize arrays for input into Pandas DataFrame
        id = []
        names = []
        dept = []
        salary = []
        bonus = []

        ### read Employees from DataBag stored in session state key
        for i in a:
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

        st.success("Sorted by Name")
        frame = st.dataframe(data=data, width=577, height=500)

    if list_salary:
        frame.empty()
        
        a = st.session_state.key.sortBySalary()

        ### initialize arrays for input into Pandas DataFrame
        id = []
        names = []
        dept = []
        salary = []
        bonus = []

        ### read Employees from DataBag stored in session state key
        for i in a:
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

        st.success("Sorted by Name")
        frame = st.dataframe(data=data, width=577, height=500)

    if load_data:
        test = DataBag()
        test = loadData()

        if 'key' not in st.session_state:
            st.session_state.key = test

        print(len(st.session_state.key))

        st.success("DataBag Loaded")

    if clear_page:
        frame.empty()

    ### here lies where the exit button would be
    ### there is no exit button due to streamlit's devs
    ### according to dev kmcgrady on Mar 25, 2021:
    #     
    #       "we do not envision a use case
    #           to shut down the server due
    #           to a UI interaction in the
    #           script."
    #
    ###               kmcgrady ...
    ###              meet use case