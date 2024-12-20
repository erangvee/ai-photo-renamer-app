import streamlit as st
import os
import shutil

def download_clicked():
    st.session_state.download_clicked = True

def download_folder(path, key=None):
    # Set the directory you want to zip
    folder_to_zip = st.session_state.DOWNLOAD_PATH.rstrip('/')
    
    # Create a ZIP file of the folder
    # Set the output directory for the ZIP file

    zip_filename = folder_to_zip+".zip"
    shutil.make_archive(folder_to_zip, 'zip', folder_to_zip)

    # Provide a download link for the ZIP file  
    with open(zip_filename, "rb") as f:
        st.download_button(
            label="Download Folder as ZIP",
            data=f,
            file_name=os.path.basename(zip_filename),
            mime="application/zip",
            on_click=download_clicked,
            key=key
        )



