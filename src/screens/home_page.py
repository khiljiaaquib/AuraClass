import streamlit as st
from src.components.header_home import header_home
from src.components.home_footer import footer_home
from src.ui.style_base_layout import style_bg_home,style_layout

def home_page():
    header_home()
    style_layout()
    style_bg_home()
    col1, col2  = st.columns(2)
    with col1:
        st.header("I ' m Teacher")
        st.image("https://cdn.jumpshare.com/preview/LjWrRw5zlQR_ospfpaZfAXBXGiSIpXvr9WpJKoxlTk2KElUhhMATY_0aUKX9yaKHvmdhQcvXw091-BQnzlWvnleYN6UmvouSqj71yA5lOKshp8xNTEFBICI53Rck8oRg",width=130)
        if st.button("Teacher Portal",type="primary",icon=":material/more_up:",icon_position="right"):
            st.session_state["login_type"]="Teacher"
            st.rerun()
        
    with col2:
        st.header("I ' m Student")
        st.image("https://cdn.jumpshare.com/preview/erb0DQ4He4rT4VrSjn9tC61snmf0SVlC-yGJMLSO1IHYVKYdSYWcE5mzVk5MSV5lvmdhQcvXw091-BQnzlWvnpUWP6I1wSXWnwCB1r3NANMhp8xNTEFBICI53Rck8oRg",width=130)
        if st.button("Student Portal",type="primary",icon=":material/more_up:",icon_position="right"):
            st.session_state["login_type"]="Student"
            st.rerun()
    footer_home()
