import streamlit as st

def app():
    st.title("Home")

    st.write("This app is a small application designed to generate payrolls for HR, as well as keep track of Employee data. There are several pages in the app that can be found on the left hand side of the screen, and each of the pages corresponds to a type of Employee.")

    st.write("The Employee, Manager, and Executive pages allow for a user to make changes to a DataBag full of Employees. The DataBag is a list based implementation of a bag that is able to store various types of objects. On these pages, users can create new Employees, or delete them by their ID number.")

    st.write("On the Payroll page, the user is able to perform a number of operations on the DataBag. The user can see all of the data contained in the DataBag, pay specific types of Employees, or pay them all. They can also view the Employees listed by name or salary.")