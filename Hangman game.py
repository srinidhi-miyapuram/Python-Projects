import random

def guessWord(word):
    
    j = 0
    word = word.lower()
    userWord = ['_' for i in word]

    userChoosenWord = input("Enter the alphabet :- ").lower()
    while j < len(word) + 2:
        if userChoosenWord in word:
            ind = word.index(userChoosenWord)
            if userWord[ind] != "_":
                newWord = word[ind+1:]
                ind += newWord.index(userChoosenWord) + 1
            
            userWord[ind] = userChoosenWord
            if "_" not in userWord:
                break
            print(*userWord)
            userChoosenWord = input("Enter the alphabet :- ").lower()
            
        else:
            userChoosenWord = input("Choose another alphabet :- ").lower()
        j += 1
    userWord = "".join(userWord)
    if userWord == word:
        print(word)
    else:
        print("Better Luck Next time")

if __name__ == "__main__":
    name = input("Enter you Name :- ")
    wordsarr = ["Plan","Dream","Implement","Work","Success"]
    randWord = random.choice(wordsarr)
    print(randWord)
    guessWord(randWord)