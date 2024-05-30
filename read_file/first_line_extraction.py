import os

directory_name = os.listdir(os.getcwd())
print(os.getcwd())
for folder in directory_name:
    folder_path = os.path.join(os.getcwd(), folder)
    try:
        for filename in os.listdir(folder_path):
            print("-------------------------------------------")

            print(f"Folder is {folder} and file name is {filename}")
            print("-------------------------------------------")

            with open(os.path.join(folder_path, filename), 'r') as f:
                print(f.readline())
                print()
                print("---------------***********-----------------")
    except NotADirectoryError:
        continue