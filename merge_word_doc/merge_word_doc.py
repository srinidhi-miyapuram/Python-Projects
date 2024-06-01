
import os
from docx import Document
from docxcompose.composer import Composer


filename = "merged_word_doc.docx"

file_path = os.path.join(os.getcwd(), filename) 

new_doc = Document(file_path)

compose_merge = Composer(new_doc)

f = os.walk(os.getcwd())

for root,folder,files in f:
    for file in files:
        nf = file.split(".")[-1]
        if file == filename:
            continue

        if file.endswith("docx"):
            doc = Document(file)
            compose_merge.append(doc)
            new_doc.add_page_break()
compose_merge.save(filename)