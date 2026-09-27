"""
Module 2 — Activity: File Sorting with os and shutil
Student: Ignacio, Justine Paul
Date: 9-26-2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

The script sorts files in a specified directory using file extensions.
First, it checks if the file path being set actually exists using path.exists and 
it creates a count of the number of files in the directory using listdir which is 
then displayed.
Second, the file names are sorted using endswith and they're placed inside a list and 
a file path is bound to them using join.
Third, the sorting starts with path.isfile to filter out foldes in the directory and it 
proceeds to split the file names by "." and it then takes the last entry from the split 
function and places it into the ext variable which is for extensions.
Lasty, the files are moved by shutil.move which is guided by another join function that 
binds the destination folder to the actual file, then makedirs creates the folder for 
sorting if there's no designated folder yet.
The scans the directory for files


============================================
KEY VOCABULARY
============================================
- os module: allows python to interact with the os which includes file management, directory management, and other operating system functionalities. 
- shutil module: this module allows python to perform high-level actions which include copying and moving files.
- file path: the location of a file written as a string.
- directory: the actual location that contains files which is pointed to by a file path.



============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

# --- paste your existing code here ---
import os
import shutil

def set_path():
    global folder_path, file_list, png, zipc, pdf, txt, mp4, pptx

    folder_path = input("Set folder path: ")

    if os.path.exists(folder_path): #check file path
        print(f"Successfully set {folder_path}")           
        file_list = os.listdir(folder_path)

        for file in file_list: #loop to list files and with increments of 1                           
            if file.endswith('.jpg') or file.endswith('.jpeg'):  
                png += 1                                    
            elif file.endswith('.zipc'):                      
                zipc += 1
            elif file.endswith('.pdf'):
                pdf += 1
            elif file.endswith('.txt'):
                txt += 1
            elif file.endswith('.mp4'):
                mp4 += 1
            elif file.endswith('.pptx'):
                pptx += 1

        return True 
    else:
        print("Please set a valid path!")
        return False


def file_lister():
    print("Files found:", file_list)
    return


def sort_files(): #sorting logic
    for file in file_list:
        file_path = os.path.join(folder_path, file) #join binds the file path to the file it's associated with

        if not os.path.isfile(file_path): #skip subfolders
            continue

        ext = file.split('.')[-1].lower() if '.' in file else 'no_extension' #extract extension safely
        #This ternary expression splits the name of files by '.' and -1 sets it to take the last part of the split which is always the file extension and if there's none it will be "no extension"
        dest_folder = os.path.join(folder_path, ext) #extensions is bound to the file paths
        os.makedirs(dest_folder, exist_ok=True) #create destination folder if it doesn't exist

        shutil.move(file_path, os.path.join(dest_folder, file)) #actually move the file
        print(f"Moved: {file} -> {ext}/")


def print_summary(): #shows the counts that are being tracked 
    print("\n--- Summary ---")
    print(f"JPG/JPEG: {png}")
    print(f"zip: {zipc}")
    print(f"PDF: {pdf}")
    print(f"TXT: {txt}")
    print(f"MP4: {mp4}")
    print(f"PPTX: {pptx}")


folder_path = ""
file_list = []
png = 0
zipc = 0 #renamed from zip to zipc to avoid conflict with the zip python function
pdf = 0
txt = 0
mp4 = 0
pptx = 0

if set_path():                                                
    file_lister()
    print_summary()
    sort_files()





""""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
#exploring the os and shutil modules, I've encountered errors mostly from improper sytax when using functions from the modules.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
The code in this file takes a task that is usually done manually and makes it quick and automated.
The process is extremely simplified using python and similar things can be done to tasks performed by a computer.
"""
