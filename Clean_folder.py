import os

folders = os.listdir(os.getcwd())

def remove_all(folders, path = os.getcwd()):
    for filename in folders:
        folder_path = os.path.join(path, filename)
        
        res = os.path.isdir(folder_path)
        if res:
            new_folder = os.listdir(folder_path)
            remove_all(new_folder, folder_path)
            os.rmdir(folder_path)
            print("***********************************")
            print(f"The folder {filename} has been removed")
        else:
            os.remove(folder_path) 
            print("---------------------------------------")
            print(f"The file {filename} has been removed")

remove_all(folders)