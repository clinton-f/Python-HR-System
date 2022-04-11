import streamlit as st

# Custom imports 

from multipage import MultiPage
from apps import employee_table, home


st.title("HR Payroll Employee Management Application")

# For the Menu Bar





# This is the multipage section, so all pages here.
 

# Create an instance of the app 
app = MultiPage()


# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Employee", employee_table.app)

# The main app
app.run()