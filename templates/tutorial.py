import streamlit as st
from services.codestral_integration import CodestralIntegration

def show():
    st.title("C++ Tutorial")
    st.write("Follow the tutorial and get real-time code suggestions.")
    
    # Example tutorial content
    st.subheader("Example: Hello World in C++")
    code_snippet = """
    #include <iostream>
    using namespace std;

    int main() {
        cout << "Hello, World!";
        return 0;
    }
    """
    st.code(code_snippet, language='cpp')
    
    # Generate code
    codestral = CodestralIntegration()
    prompt = "int main() {"
    suffix = "    return 0;\n}"
    generated_code = codestral.generate_code(prompt, suffix)
    
    st.subheader("Generated Code")
    st.code(generated_code, language='cpp')
