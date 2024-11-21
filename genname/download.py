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

    # if st.session_state.download_clicked:

    #     done_session = st.button("Finish session", on_click=done_clicked)
        
        # if done_session or st.session_state.done_clicked:
        #     os.remove(image_output)
        #     os.remove(image_source)

        # # Clean up the ZIP file after download (optional)
        # if os.path.exists(zip_filename):
        #     os.remove(zip_filename)


