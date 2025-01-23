import os
import time
import shutil

def delete_old_zip_files(directory, hours_old=1):
    """
    Deletes ZIP files in a directory older than the specified number of hours.

    Args:
    directory: The path to the directory containing the ZIP files.
    hours_old: The number of hours a file must be older than to be deleted.
    """

    current_time = time.time()
    one_hour_ago = current_time - (hours_old * 60 * 60) 

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if filename.endswith(".zip"):
            file_mtime = os.path.getmtime(filepath) 
            if file_mtime < one_hour_ago:
                try:
                    os.remove(filepath)
                    print(f"Deleted: {filepath}")
                except OSError as e:
                    print(f"Error deleting {filepath}: {e}")

def delete_old_folders(directory, hours_old=1, prefixes=["source-", "output-"]):
    """
    Deletes folders in a directory that:
    - Start with any of the specified prefixes.
    - Are older than the specified number of hours.

    Args:
    directory: The path to the directory containing the folders.
    hours_old: The number of hours a folder must be older than to be deleted.
    prefixes: A list of prefixes to match for folder names.
    """

    current_time = time.time()
    one_hour_ago = current_time - (hours_old * 60 * 60) 

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            for prefix in prefixes:
                if filename.startswith(prefix):
                    folder_mtime = os.path.getmtime(filepath)
                    if folder_mtime < one_hour_ago:
                        try:
                            shutil.rmtree(filepath)  # Use shutil.rmtree() for directories
                            print(f"Deleted: {filepath}")
                        except OSError as e:
                            print(f"Error deleting {filepath}: {e}")

