import streamlit as st

def student_screen():
    st.header("Student_screen")
    if st.button("Home Page"):
        st.session_state["login_type"]=None
        st.rerun()