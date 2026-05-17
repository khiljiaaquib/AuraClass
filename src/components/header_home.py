import streamlit as st
def header_home():
    logo_url = 'https://cdn.jumpshare.com/preview/gEhjWwTosoRHqcRfy-3PyGcloJIK-HxpRjH20tcPmf5olKN7uOlgGdfRf2S75FPrLcRMeV03xpBLlHbfwOVhlBsYOD7fXbwObhKQP108uCs'
    st.markdown(f'''
        <div style="text-align:center;"><img src="{logo_url}" alt="image" style = "height:100px;"/></div>
        <h1 style="text-align:center; color:#E0E3FF">AURA<br>&nbsp;&nbsp;Track</h1>
                ''',unsafe_allow_html=True)
   
  