import streamlit as st
from src.components.header_home import header_home
from src.components.home_footer import footer_home
from src.ui.style_base_layout import style_bg_home,style_layout,streamlit_columns

def home_page():
    header_home()
    style_layout()
    style_bg_home()
    streamlit_columns()
    col1, col2  = st.columns(2)
    with col1:
        st.header("I ' m Teacher")
        st.image("https://ik.imagekit.io/tp9rocwx79/Gemini_Generated_Image_9glyrx9glyrx9gly.png",width=130)
        if st.button("Teacher Portal",type="primary",icon=":material/more_up:",icon_position="right"):
            st.session_state["login_type"]="Teacher"
            st.rerun()
        
    with col2:
        st.header("I ' m Student")
        st.image("https://ik.imagekit.io/tp9rocwx79/Gemini_Generated_Image_tfzgxvtfzgxvtfzg.png",width=130)
        if st.button("Student Portal",type="primary",icon=":material/more_up:",icon_position="right"):
            st.session_state["login_type"]="Student"
            st.rerun()
    footer_home()
