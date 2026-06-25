import streamlit as st 
from src.screens.home_page import home_page
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.components.auto_enroll import auto_enroll_dialog
def main():
    st.set_page_config(
        page_title='Aura Class ~make attendance Faster using AI',
        page_icon="https://ik.imagekit.io/tp9rocwx79/auralogo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type']=None
    match st.session_state['login_type']:
        case 'Teacher':
            teacher_screen()
        case 'Student':
            student_screen()
        case None:
            home_page()  
    join_code = st.query_params.get("join-code")
    if(join_code):
        if st.session_state.login_type != 'Student':
            st.session_state.login_type = 'Student'
            st.rerun()
        if(st.session_state.get('is_logged_in') and st.session_state.get('user_role')=='student'):
            auto_enroll_dialog(join_code)
main()