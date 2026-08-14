import streamlit as st
from src.components.header import header_home
from ui.base_layout import style_background_home, style_base_layout
from src.components.footer import footer_home

def home_screen():



    header_home()



    style_background_home()

    style_base_layout()

   

    col1, col2 = st.columns(2, gap='large')



    with col1:

        st.header("I'm Student")

        st.image("https://raw.githubusercontent.com/Shivam5760/biometric_dual_identity_verification/main/assets/teacher_use.png", width=135)

        if st.button('Student Portal',type='primary',icon=':material/arrow_outward:',icon_position='right'):

            st.session_state['login_type'] = 'student'

            st.rerun()

       

    with col2:

         st.header("I'm Teacher")

         st.image("https://raw.githubusercontent.com/Shivam5760/biometric_dual_identity_verification/main/assets/teacher_use.png", width=135)

         if st.button('Teacher Portal',type='primary', icon=':material/arrow_outward:',icon_position='right'):

             st.session_state['login_type'] = 'teacher'

             st.rerun()  # since wapas rerun karna padega since new screen load karna hai

    footer_home()