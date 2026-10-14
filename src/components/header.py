import streamlit as st 

def header_home(): # header for home screen

    logo_url = 'https://github.com/Shivam5760/biometric_dual_identity_verification/blob/main/assets/logo3.png?raw=true'

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;'/>
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>
        
                """, unsafe_allow_html=True)


def header_dashboard(): # header for teahcer sccreen 

    logo_url = 'https://github.com/Shivam5760/biometric_dual_identity_verification/blob/main/assets/logo3.png?raw=true'

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:5px">
            <img src='{logo_url}' style='height:80px;'/>
            <h2 style='text-align:left; color:#b89bf2'>SNAP CLASS</h2>
        </div>
        
                """, unsafe_allow_html=True)