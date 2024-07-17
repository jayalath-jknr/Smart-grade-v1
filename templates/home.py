import streamlit as st

def show():
    # Header
    st.markdown("""
    <div style="display: flex; align-items: center;">
        <h1 style="margin: 0;">🚀 CodeMentor C++</h1>
        <nav style="margin-left: auto;">
            <a href="#about">About</a> |
            <a href="#services">Services</a> |
            <a href="#contact">Contact</a> |
            <a href="#blog">Blog</a>
        </nav>
    </div>
    """, unsafe_allow_html=True)
    # st.text_input("Search...", "")

    # if st.button("Sign Up"):
    #     st.write("Sign Up clicked")
    # if st.button("Get Started"):
    #     st.write("Get Started clicked")

    # Hero Section
    st.title("Master C++ with CodeMentor")
    st.subheader("Your ultimate platform for learning and mastering C++ programming.")
    st.image("images/hero_jpg_1.jpg")  # Replace with your hero image path

    # Introduction
    st.write("""
    Welcome to CodeMentor C++, your go-to platform for interactive and comprehensive C++ learning. 
    Whether you are a beginner or looking to advance your skills, we provide everything you need to 
    succeed in C++ programming.
    """)

    # Featured Content
    st.subheader("Highlights")
    st.write("🚀 New Course Launched: Advanced C++ Programming")
    st.write("🔥 Summer Discount: Get 50% off on all courses!")

    # Key Services or Products
    st.subheader("Our Services")
    st.write("- **Interactive Tutorials**: Step-by-step guides to help you learn C++ from scratch.")
    st.write("- **Code Playground**: Experiment with your code and get instant feedback.")
    st.write("- **AI Assistance**: Get real-time code suggestions and corrections.")

    # Testimonials/Reviews
    st.subheader("What Our Users Say")
    st.write("""
    "CodeMentor C++ has transformed the way I learn programming. The interactive tutorials and 
    real-time feedback are just amazing!" - Jane Doe
    """)

    # Benefits/Features
    st.subheader("Why Choose Us?")
    st.write("""
    - **Personalized Learning**: Tailored tutorials and exercises based on your skill level.
    - **Community Support**: Join a community of learners and get help from peers and mentors.
    - **Real-World Projects**: Work on real-world projects to apply your skills and build your portfolio.
    """)

    # Social Proof
    st.subheader("Our Partners")
    # st.image("path/to/partner_logos.jpg")  # Replace with logos of clients/partners

    # Latest Blog Posts or News
    st.subheader("Latest News")
    st.write("- [Understanding Pointers in C++](#)")
    st.write("- [10 Tips for Writing Efficient C++ Code](#)")

    # Call-to-Action Section
    st.subheader("Stay Connected")
    st.write("Subscribe to our newsletter to stay updated with the latest news and courses.")
    st.text_input("Enter your email", "")
    if st.button("Subscribe"):
        st.write("Subscribed!")

    # Footer
    st.subheader("Contact Us")
    st.write("""
    Address: 123 CodeMentor Street, Tech City, TC 12345  
    Phone: (123) 456-7890  
    Email: support@codementor.com  
    """)
    st.markdown("""
    <nav>
        <a href="#privacy">Privacy Policy</a> |
        <a href="#terms">Terms of Service</a> |
        <a href="#faq">FAQs</a>
    </nav>
    """, unsafe_allow_html=True)
    st.write("© 2024 CodeMentor C++")
