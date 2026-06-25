import streamlit as st
def footer_home():
    url = "https://ik.imagekit.io/tp9rocwx79/Firefly_Gemini%20Flash_make%20background%20of%20this%20colour%20_5366ed%20Add%20text%20in%20orange%20AAQUIB%20and%20this%20text%20in%20bla%20590979.png"
    st.markdown(f'''
                <div style="margin-top:2rem;gap:6px; justify-content:center; align-items:center;display:flex;"><p style="font-size:25px; color:white;font-weight:900;">Made With 💖 by</p>
                <img src='{url}' alt="image" style="max-width:85px;" /></div>
                ''',unsafe_allow_html=True)
    
def footer_dash():
    url = "https://ik.imagekit.io/tp9rocwx79/Gemini_Generated_Image_wqytztwqytztwqyt.png"
    st.markdown(f'''
                <div style="margin-top:2rem;gap:6px; justify-content:center; align-items:center;display:flex;"><p style="font-size:25px;line-height:1.1rem; color:black;font-weight:900;">Made With 💖 by</p>
                <img src='{url}' alt="image" style="max-width:85px;" /></div>
                ''',unsafe_allow_html=True)