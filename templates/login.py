import streamlit as st
from models.user import User

def show():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = User(username, None, password)
        if user.login():
            st.success("Login successful!")
            st.session_state['user'] = user
        else:
            st.error("Invalid username or password")
