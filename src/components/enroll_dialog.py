import streamlit as st
from src.db.config import supabase
from src.db.db import enroll_student_to_subject
@st.dialog("Enroll New Subject")
def enroll_dialog(student_id):
    st.write("Enter the Subject Code Provided by your Teacher")
    join_code = st.text_input("Enter Subject Code",placeholder="GE2401")
    if st.button("Enroll Now",type="primary",width="stretch"):
        if join_code:
            res = supabase.table("subjects").select("subject_id","name","subject_code").eq("subject_code",join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data["student_id"]
                check = supabase.table("subject_students").select("*").eq("subject_id",subject["subject_id"]).eq("student_id",student_id).execute()
                if check.data:
                    st.warning("You are already enrolled in this program")
                else:
                    subject_id = subject["subject_id"]
                    enroll_student_to_subject(student_id,subject_id)
                    st.success("Successfully Enrolled")
                    import time
                    time.sleep(1)
                    st.rerun()
        else:   
            st.warning("Please Enter a subject code")
    