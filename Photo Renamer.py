import streamlit as st 
import os
from dotenv import load_dotenv
from genname import process, inits, download
from streamlit_js_eval import streamlit_js_eval

def process_clicked():
    st.session_state.process_clicked = True

def done_clicked():
    st.session_state.done_clicked = True


inits.init_session_states()
inits.init_dirs('./')

load_dotenv('vars')
PAGE_TITLE = os.getenv('PAGE_TITLE')
DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH')
SOURCE_PATH = os.getenv('SOURCE_PATH')


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
    # st.write(processed)
    # if processed:
    download.download_folder(DOWNLOAD_PATH)

if st.session_state.download_clicked:
    col1, col2 = st.columns(2)
    
    with col1:
        # st.write("## Download")
        download.download_folder(DOWNLOAD_PATH,key="Second")

    with col2:
        # st.write("## Finish Session")
        done_session = st.button("Finish session", on_click=done_clicked, key="Done")

        if done_session or st.session_state.done_clicked:
            #os.remove(DOWNLOAD_PATH)
            for i in os.listdir(SOURCE_PATH):
                os.remove(SOURCE_PATH+'/'+i)

            for i in os.listdir(DOWNLOAD_PATH):
                os.remove(DOWNLOAD_PATH+'/'+i)


            # Clean up the ZIP fi le after download (optional)
            zip_filename = 'output.zip'
            if os.path.exists(zip_filename):
                os.remove(zip_filename)

            
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
        
        
        