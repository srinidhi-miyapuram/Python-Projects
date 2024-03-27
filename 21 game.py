import random

class Game:

    userChoiceNum = [0]


    def addNum(self,num):
       
        for i in range(num):
            if len(self.userChoiceNum) > 0 and self.userChoiceNum[-1] < 21:
                res = self.userChoiceNum[-1] + 1
                self.userChoiceNum.append(res)
            else:
                self.userChoiceNum.append(1)
        if self.userChoiceNum[0] == 0:
            self.userChoiceNum.pop(0)

    def startGame(self,choice):
        myNum = 1
        count = 1 if choice == "no" else 0
        res = False
        while self.userChoiceNum[-1] < 21:
            if count % 2 != 0:
                myNum = random.randint(1,4)
                self.addNum(myNum)
                count += 1
                print("\nOrder of input's after computer's turn :- \n")
                print(self.userChoiceNum)
            else:
                print("\nYour Turn\n")
                userNum = int(input("How many numbers you wish to enter :- \n"))
                print("Enter your Numbers below  :- ")
                for i in range(userNum):
                    num = int(input())
                    if num - self.userChoiceNum[-1] != 1:
                        print("\nYou're disqualified")
                        res = True
                        break
                    else:
                        self.userChoiceNum.append(num)
                count += 1
                if res:
                    break
        if count % 2 == 0 and not res:
            print("\nYou Won")
        elif not res: 
            print("\nComputer Won")
                
                

       

            

if __name__ == "__main__":
    choice = input("Do you want to play first ? Type yes or no :- ").lower()
    Game().startGame(choice)