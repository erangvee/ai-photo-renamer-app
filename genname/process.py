import os
from genname.utils import copy_and_rename_file, sluggify, is_not_jpg
from genname import generator, download
import streamlit as st



def process_summary():
    image_source = "./source/"
    image_output = "./output/"

    images = os.listdir(image_source)
    placeholder = st.empty()

    placeholder.write("### *Processing...*")
    for f in images:
        if is_not_jpg(f):
            placeholder.write(f"The image {f} is not in JPG/PNG format.")
        else:
            print(f"The image {f} is in JPG/PNG format.")
            image_path = image_source+f
            summary = generator.get_image_summary(image_path)
            if summary:
                print(f"Image summary: {summary}")
                new_file_name = sluggify(summary)+'.'+f.split('.')[1]
                copy_and_rename_file(image_path, image_output, new_file_name)
                placeholder.write(f"Successfully renamed image **{f}** to **{new_file_name}**.")
            else:
                placeholder.write(f"Failed to rename image {f}.")

    placeholder.write("### *DONE*")
    return True



