import streamlit as st
def footer_home():
    url = "https://cdn.jumpshare.com/preview/7fMBtsTy4qTWHYv6cNOLlu38Sb5ScayeaOhOJeaWYowu5bOtYxDVUiTMasKztb3wafIw5U9DCKE0yWYKuLIg1IHTF9bN8VvRbR3B4-zOUzUhp8xNTEFBICI53Rck8oRg"
    st.markdown(f'''
                <div style="margin-top:2rem;gap:6px; justify-content:center; align-items:center;display:flex;"><p style="font-size:25px; color:white;font-weight:900;">Made With 💖 by</p>
                <img src='{url}' alt="image" style="max-width:85px;" /></div>
                ''',unsafe_allow_html=True)