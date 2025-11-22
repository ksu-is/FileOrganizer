import os
import shutil

#File Categories Dictionary
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Data": [".csv", ".json", ".xml"],
    "Photoshop": [".psd"],
    "Other": []

}

#Organization Function
def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"Error {directory} is not a valid directory.")
        return
    
    #Create Folders for Category
    for category in file_categories:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    #Move Files into Corresponding Folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        #Skip if its a directory
        if os.path.isdir(file_path):
            continue

        #Check File Extension and Move
        file_moved = False
        for category, extensions in file_categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break

        #Move Remaining Files to "Other"
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Other", filename))

    print(f"Files in '{directory}' have been organized successfully!")

directory_to_organize = input('Enter the directory path to organize: ')
organize_files(directory_to_organize)
