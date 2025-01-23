import os
from genname.utils import copy_and_rename_file, sluggify, is_not_jpg
from genname import generator, download
import streamlit as st



def process_summary():
    image_source = st.session_state.SOURCE_PATH
    image_output = st.session_state.DOWNLOAD_PATH

    images = os.listdir(image_source)
    placeholder = st.empty()
    st.session_state.checker = []
    placeholder.write("### *Processing...*")
    for f in images:
        if f not in st.session_state.checker:
            st.session_state.checker.append(f)
        else:
            continue 
        
        if is_not_jpg(f):
            placeholder.write(f"The image {f} is not in JPG/PNG format.")
        else:
            image_path = image_source+f
            summary = generator.get_image_summary(image_path, st.session_state.prompt)
            if summary:
                new_file_name = sluggify(summary)+'.'+f.split('.')[1]

                while new_file_name in os.listdir(image_output):
                    st.session_state.counter += 1
                    new_file_name = sluggify(summary)+' ('+str(st.session_state.counter)+').'+f.split('.')[1]
                
                copy_and_rename_file(image_path, image_output, new_file_name)
                st.session_state.counter = 0
                placeholder.success(f"Successfully renamed image **{f}** to **{new_file_name}**.")
            else:
                placeholder.error(f"Failed to rename image {f}.")
    
    placeholder.write("### *DONE*")
    st.session_state.processed = True



