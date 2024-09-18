import os
import shutil
from config.file_catagories import FILE_CATEGORIES
from utils.helpers import create_folder_if_not_exists


def organize_by_type(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, file_extension = os.path.splitext(filename)
        moved = False

        for category, extensions in FILE_CATEGORIES:
            if file_extension.lower() in extensions:
                category_folder = os.path.join(folder_path, category)
                create_folder_if_not_exists(category_folder)
                shutil.move(file_path, category_folder)
                moved = True
                break
        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            create_folder_if_not_exists(others_folder)
            shutil.move(file_path, others_folder)
