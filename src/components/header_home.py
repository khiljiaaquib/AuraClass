import streamlit as st
def header_home():
    logo_url="https://ik.imagekit.io/tp9rocwx79/auralogo.png"
    st.markdown(f'''
        <div style="text-align:center;"><img src="{logo_url}" alt="image" style = "height:100px;"/></div>
        <h1 style="text-align:center; color:#E0E3FF">AURA<br>&nbsp;&nbsp;Track</h1>
                ''',unsafe_allow_html=True)

def header_teacher():
    logo_url = 'https://ik.imagekit.io/tp9rocwx79/aur.png'
    
    c1,c2 = st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        st.markdown(f'''
        <div style="display:flex;flex-direction:row;gap:10px;align-items:center;justify-content:center;"><img src="{logo_url}" alt="image" style = "height:100px;display:inline;"/>
        <h2 style="text-align:left;color:#5366ed;">AURA<br>Track</h2></div>      
                ''',unsafe_allow_html=True)
    with c2:
        if st.button("Go Back TO Home",type="secondary",key="BackHome",shortcut="Control+Backspace"):
            st.session_state["login_type"]=None
            st.rerun()

def header_teacher_dashboard():
    logo_url = 'https://ik.imagekit.io/tp9rocwx79/aur.png'
    teacher_data = st.session_state.teacher_data
    st.markdown(f"""<h2 style = "color:#000000;">Welcome {teacher_data["name"]}</h2>""",unsafe_allow_html=True)
    c1,c2 = st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        st.markdown(f'''
        <div style="display:flex;flex-direction:row;gap:10px;align-items:center;justify-content:center;"><img src="{logo_url}" alt="image" style = "height:100px;display:inline;"/>
        <h2 style="text-align:left;color:#5366ed;">AURA<br>Track</h2></div>      
                ''',unsafe_allow_html=True)
    with c2:
        if st.button("Logout",type="secondary",key="loginbackbtn",shortcut="Control+Backspace"):
            st.session_state["is_logged_in"]=False
            del st.session_state.teacher_data
            st.rerun()
            
def header_student_dashboard():
    logo_url = 'https://ik.imagekit.io/tp9rocwx79/aur.png'
    student_data = st.session_state.student_data
    st.markdown(f"""<h2 style = "color:#000000;">Welcome {student_data["name"]}</h2>""",unsafe_allow_html=True)
    c1,c2 = st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        st.markdown(f'''
        <div style="display:flex;flex-direction:row;gap:10px;align-items:center;justify-content:center;"><img src="{logo_url}" alt="image" style = "height:100px;display:inline;"/>
        <h2 style="text-align:left;color:#5366ed;">AURA<br>Track</h2></div>      
                ''',unsafe_allow_html=True)
    with c2:
        if st.button("Logout",type="secondary",key="loginbackbtn",shortcut="Control+Backspace"):
            st.session_state["is_logged_in"]=False
            del st.session_state.student_data
            st.rerun()