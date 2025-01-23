import streamlit as st 

import os
import shutil
from dotenv import load_dotenv
from genname import process, inits, download
from streamlit_js_eval import streamlit_js_eval

def process_clicked():
    st.session_state.process_clicked = True

def done_clicked():
    st.session_state.done_clicked = True

def uploaded():
    st.session_state.uploaded = True


# initialize session states for global variables
inits.init_session_states()
token = st.session_state.token # to facilitate unique sessions

# load variables from file
load_dotenv('vars')

SOURCE_PREFIX = os.getenv('SOURCE_PREFIX')
OUTPUT_PREFIX = os.getenv('OUTPUT_PREFIX')

# specify constants
PAGE_TITLE = os.getenv('PAGE_TITLE')
DOWNLOAD_PATH = './' + OUTPUT_PREFIX + token + '/'
SOURCE_PATH = './' + SOURCE_PREFIX + token + '/'
HOURS_OLD = int(os.getenv('HOURS_OLD'))
st.session_state.prompt = os.getenv('BASE_PROMPT')

# clean up old files
try:
    inits.init_cleanup(os.getcwd(), HOURS_OLD, [SOURCE_PREFIX, OUTPUT_PREFIX])
except:
    # pass if there are no older files
    pass

st.session_state.DOWNLOAD_PATH = DOWNLOAD_PATH # save variables to session state
st.session_state.SOURCE_PATH = SOURCE_PATH # save variables to session state

st.set_page_config(page_title=PAGE_TITLE,
                   page_icon=os.getenv('FAVICON'),
                   layout=os.getenv('LAYOUT')) 

st.write("# ", PAGE_TITLE)
st.markdown(str(os.getenv('PAGE_DESC'))+""" (_"""+str(os.getenv('GEMINI_VER'))+"""_)""")

st.markdown("## Upload photos")
uploaded_files = st.file_uploader("Upload images. Only PNG and JPG photos accepted.", 
                                type=['png','jpg'], 
                                accept_multiple_files=True,
                                on_change=uploaded)

if uploaded_files or st.session_state.uploaded:
    st.markdown("""
                ## Prompt
                The system uses the base prompt:

                _"""+st.session_state.prompt+"""_"""
                )

    st.session_state.count+=1
    st.write(st.session_state.count)
    # give option to append text to the original prompt.
    add = st.checkbox("Append text to the prompt.")

    if add:
        add_text = st.text_input("Enter text to append to original prompt here")
        st.session_state.prompt = st.session_state.prompt+" "+add_text

    process_button = st.button("Start processing", on_click=process_clicked)
    
    if process_button or st.session_state.process_clicked:       
        processed = False
        for path in [DOWNLOAD_PATH, SOURCE_PATH]:
            try:
                shutil.rmtree(path)
            except:
                pass
            os.makedirs(path, exist_ok=True)

        for uploaded_file in uploaded_files:
            if uploaded_file is not None:                  
                # Save the uploaded file to the specified directory
                file_path = os.path.join(SOURCE_PATH, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())  # Use getbuffer() to get the file data

        processsed = process.process_summary()
    st.session_state.uploaded = False
    
if st.session_state.processed:
    st.session_state.uploaded = False
    col1, col2 = st.columns(2)

    with col1:        
        download.download_folder(DOWNLOAD_PATH, key="Second")

    with col2:
        
        done_session = st.button("Finish session", on_click=done_clicked, key="Done")

        if done_session or st.session_state.done_clicked:
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
            
            shutil.rmtree(DOWNLOAD_PATH)
            shutil.rmtree(SOURCE_PATH)

            # Clean up the ZIP fi le after download (optional)
            zip_filename = st.session_state.DOWNLOAD_PATH.strip('./')+".zip"
            if os.path.exists(zip_filename):
                os.remove(zip_filename)

                
                
            
                    
                    
