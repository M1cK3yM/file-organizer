import os


def create_folder_if_not_exists(folder_name):
    """Creates a folder if it does not exists"""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
