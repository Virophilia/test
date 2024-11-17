import streamlit as st

st.title('Ahoy!')
hide_st_style = """
            <style>
            #MaiMenU {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)