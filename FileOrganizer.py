import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


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

        moved_count = 0

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
                #print(f"Moved {filename} to {category}")
                moved_count += 1
                file_moved = True
                break

        #Move Remaining Files to "Other"
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Other", filename))
            #print(f'Moved {filename} to Other')
            moved_count += 1

    print(f"Files in '{directory}' have been organized successfully! ({moved_count} files moved)")

#directory_to_organize = input('Enter the directory path to organize: ')
#organize_files(directory_to_organize)



#Function Allows User to Select File to Organize and Stores in Variable
def choose_folder():
    folder = filedialog.askdirectory()
    folder_var.set(folder)

#Uses Folder Selected to Run organize_files Function and Shows Warning if No Folder Selected
def run_organizer():
    folder = folder_var.get().strip()
    if not folder:
        messagebox.showwarning("Please select a folder to organize.")
        return
    
    result = organize_files(folder)
    output_var.set(result)
    

root = tk.Tk()
root.title("FileOrganizer")
root.geometry("500x250")


folder_var = tk.StringVar()
output_var = tk.StringVar()

tk.Label(root, text = "Choose Folder to Organize:", font = ("Arial", 12)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Entry(frame, textvariable = folder_var, width = 40).pack(side = tk.LEFT, padx = 5)
tk.Button(frame, text = "Browse", command = choose_folder).pack(side = tk.LEFT)
tk.Button(root, text = "Organize Files", command = run_organizer, height = 2, width = 20).pack(pady = 20)
tk.Label(root, textvariable = output_var, fg = "blue", font = ("Arial, 11")).pack(pady = 10)

root.mainloop()