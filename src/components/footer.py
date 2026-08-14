import streamlit as st 

def footer_home(): # header for home screen

    logo_url ='"https://raw.githubusercontent.com/Shivam5760/biometric_dual_identity_verification/main/assets/teacher_use.png"'

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:black";> Shivam Nibalwar </p>
            <img src='{logo_url}' style='height:25px;'/>
    
        </div>
        
                """, unsafe_allow_html=True)