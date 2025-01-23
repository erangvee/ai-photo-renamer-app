import streamlit as st 
import os
import secrets

from utils import clean

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

    if "processed" not in st.session_state:
        st.session_state.processed = False

    if "uploaded" not in st.session_state:
        st.session_state.uploaded = False

    if "count" not in st.session_state:
        st.session_state.count = 0

def init_cleanup(path, hours_old, prefixes=["source-", "output-"]):
    clean.delete_old_zip_files(path, hours_old)
    clean.delete_old_folders(path, hours_old, prefixes)
