import streamlit as st
from src.components.header import header_home
from ui.base_layout import style_background_home, style_base_layout

def home_screen(): 

    header_home()

    style_background_home()
    style_base_layout()
    
    col1, col2 = st.columns(2) 

    with col1: 
        if st.button('Teacher Portal'): 
            st.session_state['login_type'] = 'teacher'
            st.rerun()  # since wapas rerun karna padega since new screen load karna hai 
    with col2: 
        if st.button('Student Portal'): 
            st.session_state['login_type'] = 'student'
            st.rerun() 