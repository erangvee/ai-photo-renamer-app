import streamlit as st 
import os
from dotenv import load_dotenv
from genname import process, inits, download

def process_clicked():
    st.session_state.process_clicked = True

inits.init_session_states()
inits.init_dirs('./')

load_dotenv('vars')
PAGE_TITLE = os.getenv('PAGE_TITLE')


save_directory = './source'

st.title(PAGE_TITLE)

st.markdown(str(os.getenv('PAGE_DESC')))

uploaded_files = st.file_uploader("Upload images. Only PNG and JPG photos accepted.", type=['png','jpg'], accept_multiple_files=True)

for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        # Save the uploaded file to the specified directory
        file_path = os.path.join(save_directory, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())  # Use getbuffer() to get the file data

process_button = st.button("Start processing", on_click=process_clicked)

processed = False
if process_button:
    processsed = process.process_summary()
    st.write(processed)
    # if processed:
    download.download_folder("./output/")