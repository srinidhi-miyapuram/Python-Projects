
sentence = ""

with open("snowwhite.txt", 'r') as file:
    sentence = file.readlines()

words = sentence[0].split(".")
word = ""
for i in words:
    i = i.strip(" ")
    word += i.capitalize()
    word += ". "

with open("snowwhite.txt", 'w') as file:
    file.writelines(word)

