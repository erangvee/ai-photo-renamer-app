import streamlit as st 
import os
import secrets

def init_session_states():    
    token = secrets.token_hex(4)

    if "process_clicked" not in st.session_state:
        st.session_state.process_clicked = False 

    if "download_clicked" not in st.session_state:
        st.session_state.download_clicked = False

    if "done_clicked" not in st.session_state:
        st.session_state.done_clicked = False

    if "SOURCE_PATH" not in st.session_state:
        st.session_state.SOURCE_PATH = ""

    if "DOWNLOAD_PATH" not in st.session_state:
        st.session_state.DOWNLOAD_PATH = ""

    if "counter" not in st.session_state:
        st.session_state.counter = 0

    if "checker" not in st.session_state:
        st.session_state.checker = []

    if "token" not in st.session_state:
        st.session_state.token = token

def init_dirs(path):
    for dirx in ['source', 'output']:
        if dirx not in os.listdir(path):
            os.mkdir(path+'/'+dirx)
