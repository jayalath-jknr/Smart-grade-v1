import streamlit as st
from models.user import User

def show():
    st.title("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        user = User(username, email, password)
        user.register()
        st.success("User registered successfully!")
