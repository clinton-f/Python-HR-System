import streamlit as st

# Custom imports #
from multipage import MultiPage
from apps import home, employee_table, manager, executive, payroll
from objects.DataBag import DataBag
from objects.sourceData import loadData


### Create header
####  st.header("HR Payroll Employee Management Application")

### Adds DataBag for storage to session state
test = DataBag()
test = loadData()

if 'key' not in st.session_state:
    st.session_state.key = test
 

### Create an instance of the app 
app = MultiPage()

st.set_page_config(page_title="HR Mgmt App", page_icon="💼")

### Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Employee", employee_table.app)
app.add_page("Manager", manager.app)
app.add_page("Executive", executive.app)
app.add_page("Payroll", payroll.app)


### Run app
app.run()