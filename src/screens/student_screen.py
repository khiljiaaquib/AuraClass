import streamlit as st
import streamlit as st
from PIL import Image
import numpy as np
from src.components.home_footer import footer_dash
from src.pipelines.face_pipelines import predict_attendance,get_face_embeddings,train_classifier
from src.pipelines.voice_pipelines import get_voice_embedding
from src.ui.style_base_layout import style_bg_dashboard,style_layout,header
from src.components.header_home import header_student_dashboard
from src.db.db import get_all_students,create_student,get_student_subjects,get_student_attendance,unenroll_student_to_subject
from src.components.enroll_dialog import enroll_dialog
from src.components.header_home import header_teacher
from src.ui.style_base_layout import style_bg_dashboard,style_layout
from src.components.enroll_dialog import enroll_dialog
from src.components.subject_cards import subject_card
def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data["student_id"]
    header_student_dashboard()
    st.space()
    c1,c2 = st.columns(2)
    with c1:
        header("Your Enrolled Subjects")
    with c2:
        if st.button("Enroll In Subjects",type="primary",width="stretch"):
            enroll_dialog(student_id)
    st.divider()
    with st.spinner("Loading your enrolled subjects..."):
        subjects= get_student_subjects(student_id)
        logs= get_student_attendance(student_id)
    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if(sid not in stats_map):
            stats_map[sid]={"total":0,"attend":0}
        stats_map[sid]['total']+=1
        if log.get('is_present'):
            stats_map[sid]['attend']+=1
            
    cols = st.columns(2)
    for i , sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid  = sub['subject_id']
        stats = stats_map.get(sid,{"total":0,"attend":0})
        def unenroll_button():
            if st.button("Unenroll from this subject",type='tertiary',width="stretch",icon=':material/delete_forever:'):
                unenroll_student_to_subject(student_id,sid)
                st.toast(f'unenrolling from {sub['name']}')
                st.rerun()
        with cols[i%2]:
            subject_card(
                name=sub['name'],
                code = sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅','Total',stats['total']),
                    ('✅','Attended',stats['attend']),
                ],
                
                footer_callback=unenroll_button
            )
        
    
def student_screen():
    style_bg_dashboard()
    style_layout()
    if "student_data" in st.session_state:
        student_dashboard()
        return 
    else:
        header_teacher()  
    st.header("Login Using FaceID",text_alignment="center")
    st.space()
    st.space()
    show_registeratiom = False
    st.markdown('''
                <style>
                h2{
                    color:#000000 !important;
                }
                </style>
                ''',unsafe_allow_html=True)

    photo_source = st.camera_input("Place Your Face in the center")
    if photo_source:
        img = np.array(Image.open(photo_source))
        with st.spinner("AI is Scanning..."):
            detected , all_ids,num_faces = predict_attendance(img)
            if num_faces ==0:
                st.warning("Face not found")
            elif num_faces>1:
                st.warning("Multiple faces found")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s["student_id"]==student_id),None)
                    if student:
                        st.session_state.is_logged_in = True 
                        st.session_state.user_role = "student"
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student["name"]}")
                        import time
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info("Face not recognized you might be a new student!")
                    show_registeratiom = True 
    
    if show_registeratiom:
        with st.container(border=True):
            st.header("Register new Profile")
            new_name = st.text_input("Enter your name",placeholder="Eg:-Aaquib khilji")
            st.subheader("optional : voice Enrollment")
            st.info("Enroll your for voice only attendance ")
            audio_data = None 
            try:
                audio_data = st.audio_input("Record a short phrase like:-I am present , My name is Aaquib")
            except Exception as e:
                st.error("Audio data failed")
            if st.button("Create Account",type ="primary"):
                if new_name:
                    with st.spinner("Creating profile..."):
                        img = np.array(Image.open(photo_source))
                        encodings  = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()
                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())
                            response_data = create_student(new_name,face_embedding =face_emb,  voice_embedding = voice_emb )
                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True 
                                st.session_state.user_role = "student"
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Profile Created ! Hi , {new_name}!")
                                import time
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Couldnt capture your facial features for registeration")    
                else: 
                    st.warning("Name is required")
    footer_dash()