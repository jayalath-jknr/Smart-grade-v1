import streamlit as st
from models.course import Course

def show():
    user = st.session_state.get('user', None)
    print(user)
    if user:
        st.title(f"Welcome, {user.username}")
        st.header("Your Courses")
        for course in user.get_courses():
            st.subheader(course.title)
            for module in course.get_course_content():
                st.write(module.get_module_content())
    else:
        st.error("You need to log in to access the dashboard")
