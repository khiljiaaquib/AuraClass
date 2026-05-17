import streamlit as st

def teacher_screen():
    st.header("Teacher_screen")
    if st.button("Home Page"):
        st.session_state["login_type"]=None
        st.rerun()