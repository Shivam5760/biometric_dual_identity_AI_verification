import streamlit as st 

def style_background_home() : 

    st.markdown("""
                <style>
                        .stApp{
                                background: #b89bf2 !important 
                                }
                        .stApp div[data-testid="stColumn"]{

                            background-color:#e3dab7 !important;

                            padding:2.5rem !important;

                            border-radius:5rem !important}

                </style>
                </style>
    
    """,unsafe_allow_html=True)

def style_background_dashboard() : 

    st.markdown("""
                <style>
                        .stApp{
                                background: #b89bf2 !important 
                                }
    
                </style>
    """,unsafe_allow_html=True)





import streamlit as st

def style_base_layout(): 
    st.markdown("""
        <style>
            /* 1. Imports MUST be inside <style> at the very top */
           

            @import url('https://fonts.googleapis.com/css2?family=Black+Ops+One&family=Climate+Crisis:YEAR@2005&family=Press+Start+2P&family=Rubik+Spray+Paint&family=Special+Elite&family=VT323&display=swap');


            /* 2. Hide Top Header & Toolbar completely */
            header[data-testid="stHeader"],
            div[data-testid="stHeader"],
            div[data-testid="stToolbar"],
            div[data-testid="stDecoration"],
            div[data-testid="stStatusWidget"],
            #MainMenu, 
            footer {
                visibility: hidden !important;
                display: none !important;
                height: 0px !important;
            }

            /* 3. Page Top Padding */
            .main .block-container {
                padding-top: 1rem !important;
            }

            /* 4. Apply Climate Crisis to H1  BUT GIVEN PRESS START 2P YOII  */
            h1, [data-testid="stMarkdownContainer"] h1 {
                font-family: 'Press Start 2P', cursive !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            /* 5. Apply VT323 to H2 */
            h2, [data-testid="stMarkdownContainer"] h2 {
                font-family: 'VT323', cursive, display !important;
                font-size: 2.8rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                letter-spacing: 1px !important;
            }

            h3, h4, p {
                font-family: 'Special Elite',sans-serif !important;
            }
            button{
                background: #f2e29b !important;
                color: black !important;
                padding:10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
            button[kind='Secondary']{
                background: #f29b9b !important;
                color: black !important;
                padding:10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
            button[kind='Tertiary']{
                background: #EB459E !important;
                color: black !important;
                padding:10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }
            button:hover{
                transform :scale(1.05)}
        </style>
    """, unsafe_allow_html=True)