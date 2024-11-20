import os 
import re
import shutil

def copy_and_rename_file(source_path, destination_folder, new_file_name):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Get the original file name from the source path
    original_file_name = os.path.basename(source_path)
    
    # Create the full destination path
    destination_path = os.path.join(destination_folder, original_file_name)
    
    try:
        # Copy the file
        shutil.copy(source_path, destination_path)
        # print(f"Copied {source_path} to {destination_path}")
        
        # Create the new destination path with the new file name
        new_destination_path = os.path.join(destination_folder, new_file_name)
        
        # Rename the copied file
        os.rename(destination_path, new_destination_path)
        # print(f"Renamed {destination_path} to {new_destination_path}")
    except:
        os.remove(destination_path)
        pass

def sluggify(sentence):
    # Convert to lowercase
    slug = sentence.lower()
    
    # Remove special characters using regex
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    
    # Replace spaces and consecutive hyphens with a single hyphen
    slug = re.sub(r'[\s-]+', '-', slug).strip('-')
    
    return slug


def is_not_jpg(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() not in ('.jpg', '.jpeg', '.png')