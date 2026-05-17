import streamlit as st
def style_bg_home():
    st.markdown('''
                <style>
                .stApp{
                    background:#5366ed !important;
                }
                </style>
                ''',unsafe_allow_html=True)
def style_bg_dashboard():
    st.markdown('''
                <style>
                .stApp{
                    background:#E0e3ff !important;
                }
                </style>
                ''',unsafe_allow_html=True)

def style_layout():
    st.markdown('''
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
                /*hide toolbar of streamlit*/
                #MainMenu,footer,header{
                    visibility:hidden;
                }
                .block-container{
                    padding_top:1.5rem !important;
                }
                h1{
                    font-family:'Climate Crisis' , sans-serif !important;
                    font-size:3.5rem !important;
                    line-height:0.9 !important;
                    margin-bottom:0rem !important;
                }
                h3,h4,p,h5{
                    font-family:'Outfit',sans-serif ;
                }
                button[kind="secondary"]{
                    border-radius:1.5rem !important;
                    color :white !important;
                    background:#EB459E !important;
                    padding:10px 20px !important;
                    border:none !important;
                    transition:transform 0.25s ease-in-out !important;
                }
                button{
                    border-radius:1.5rem !important;
                    color :white !important;
                    background:#5865F2 !important;
                    padding:10px 20px !important;
                    border:2px solid black !important;
                    transition:transform 0.25s ease-in-out !important;
                }
                button[kind="tertiary"]{
                    border-radius:1.5rem !important;
                    color :white !important;
                    background:black !important;
                    padding:10px 20px !important;
                    border:none !important;
                    transition:transform 0.25s ease-in-out !important;
                }
                button:hover ,button[kind="secondary"]:hover,button[kind="tertiary"]:hover {
                    transform:scale(1.05) !important;
                }
                h2{
                    color:#000f00 !important;
                    font-size:2rem !important;
                    font-family:'Climate Crisis' , sans-serif !important;
                    line-height:0.9 !important;
                    margin-bottom:0rem !important;
                }
                .stApp div[data-testid="stColumn"]{
                    background:#f4f5f7 !important;
                    padding:1.5rem !important;
                    border-radius:5rem !important;
                    transition:transform 0.25s ease-in-out !important;
                }
                .stApp div[data-testid="stColumn"]:hover{
                    transform:scale(1.05) !important;
                    }
                    
                </style>
                ''',unsafe_allow_html=True)