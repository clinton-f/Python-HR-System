import streamlit as st

def app():
    st.title("Manager")

    # Success Alert
    st.success("Input was a success!")
    
    # Error Alert - red
    st.error("Some error!")

    st.write("This is the Manager page.")