import hashlib
from tkinter.filedialog import askdirectory
import os 
from pathlib import Path
from tkinter import Tk

Tk().withdraw()

file_path = askdirectory(title="Select the folder")

list_files = os.walk(file_path)

files = dict()

def find(root, file):
    for f in file:
        try:
            file_path = Path(os.path.join(root, f))
            Hashfile = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            if Hashfile not in files:
                files[Hashfile] = file_path
            else:
                os.remove(file_path)
                print(f"{file_path} is removed")
        except Exception as e:
            continue

for root,folder, file in list_files:
    print(folder)
    if len(folder) != 0:
        for fold in folder:
            file_name = os.path.join(root,fold)
            find(file_name, file)
    find(root, file)     