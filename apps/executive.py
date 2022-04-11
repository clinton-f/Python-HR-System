import streamlit as st

def app():
    st.title("Executive")

    # Error Alert - red
    st.error("Some error!")

    # Success Alert
    st.success("Input was a success!")


    st.write("This is the Executive page.")