import streamlit as st 
import os

def init_session_states():    
    if "process_clicked" not in st.session_state:
        st.session_state.process_clicked = False 

    if "download_clicked" not in st.session_state:
        st.session_state.download_clicked = False

    if "done_clicked" not in st.session_state:
        st.session_state.done_clicked = False

def init_dirs(path):
    for dirx in ['source', 'output']:
        if dirx not in os.listdir(path):
            os.mkdir(path+'/'+dirx)
