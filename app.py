{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import streamlit.components.v1 as components\
\
# Set page to wide layout with custom title\
st.set_page_config(\
    page_title="Kerry FC Performance Portal",\
    page_icon="\uc0\u9917 ",\
    layout="wide",\
    initial_sidebar_state="collapsed"\
)\
\
# Hide Streamlit default headers/footers for a clean app feel\
st.markdown("""\
    <style>\
        #MainMenu \{visibility: hidden;\}\
        footer \{visibility: hidden;\}\
        header \{visibility: hidden;\}\
        .block-container \{padding: 0rem !important;\}\
    </style>\
""", unsafe_allow_html=True)\
\
# Load and render your exact HTML portal\
with open("index.html", "r", encoding="utf-8") as f:\
    html_code = f.read()\
\
components.html(html_code, height=1400, scrolling=True)}