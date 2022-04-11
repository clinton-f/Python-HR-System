import streamlit as st

def app():
    st.title("Home")

    # Success Alert
    st.success("Input was a success!")
    
    # Error Alert - red
    st.error("Some error!")

    st.write("This page will introduce the app.")