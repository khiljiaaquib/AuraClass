import streamlit as st
from src.db.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new Subject")
    sub_id = st.text_input("Subject Code",placeholder="GE2401")
    sub_name = st.text_input("Subject Name",placeholder="Graphics")
    sub_section = st.text_input("Section",placeholder="A")
    if st.button("Create Now",type="secondary",width="stretch"):
          if sub_id and sub_name and sub_section:
                try:
                    create_subject(sub_id,sub_name,sub_section,teacher_id)
                    st.toast("Subject Created!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error:{str(e)}")
          else:    
              st.warning("Please fill all the fields")  