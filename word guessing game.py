import random

def guessWord(word):
    i = 0
    j = 0
    word = word.lower()
    userWord = []

    userChoosenWord = input("Enter the alphabet :- ").lower()
    while j < 12:
        if userChoosenWord == word[i]:
            userWord.append(userChoosenWord)
            i += 1
            if len(userWord) == len(word):
                break
            userChoosenWord = input("Enter the alphabet :- ").lower()
        else:
            userChoosenWord = input("Choose another alphabet :- ").lower()
        
        j += 1
    userWord = "".join(userWord)
    if userWord == word:
        print(word)
    else:
        print("Better Luck next time")

if __name__ == "__main__":
    name = input("Enter your Name :- ")
    words = ["Plan","Dream","Implement","Work","Success"]
    randWord = random.choice(words)
    guessWord(randWord)

