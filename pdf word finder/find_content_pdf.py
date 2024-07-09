import pdfplumber
import os

word = input("Enter the word you want to find ...  ")

current_path = os.getcwd()

files = os.walk(current_path)

for root, folder, file in files:
    for name in file:
        extension = name.split('.')[-1]
        if extension == 'pdf':
            with pdfplumber.open(name) as pdf:
                f = pdf.pages
                for page in range(len(f)):
                    content = f[page].extract_text()
                    num = content.find(word)
                    if num >= 0:
                        print(f"{word} was found in :- {name}, Page Number: {page}")

        