import streamlit as st
from templates import home, tutorial, playground, review, questions

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Tutorial", "Playground", "Review", "Questions"])

if page == "Home":
    home.show()
elif page == "Tutorial":
    tutorial.show()
elif page == "Playground":
    playground.show()
elif page == "Review":
    review.show()
elif page == "Questions":
    questions.show()
