import streamlit as st
from services.codestral_integration import CodestralIntegration
from config.config import Config

def show():
    st.title("C++ Playground")
    st.write("Write and test your C++ code here.")
    
    user_code = st.text_area("Your C++ Code", height=300)
    
    if st.button("Generate Code"):
        codestral = CodestralIntegration(Config.API_KEY)
        generated_code = codestral.generate_code(user_code)
        st.subheader("Generated Code")
        st.code(generated_code, language='cpp')
