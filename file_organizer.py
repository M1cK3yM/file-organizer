import os
from organizer.filetype_orgnizer import organize_by_type


def main():
    folder_path = input("Enter the path of the folder you want to organize : ")

    if not os.path.exists(folder_path):
        print("Invalid path. Please enter a valid path.")
        return

    print("Choose how to organize your files : ")
    print("1. Organize by file type")
    print("2. Organize by date")

    choice = input("Enter your choice (1 or 2) : ")

    if choice == "1":
        organize_by_type(folder_path)
    elif choice == "2":
        print("Organizing by date is not yet implemented.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

    print("File organization completed.")


if __name__ == "__main__":
    main()
