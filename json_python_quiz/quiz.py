
# Load json file and get the content from it based on the input id

import json


num = int(input("\nEnter the question number from 1-9 :- "))

if 1 <= num <= 9:
    file = open("quiz.json")
    res = json.load(file)
    for i in range(len(res["quizzes"])):
        nls = res["quizzes"][i]["questions"]
        for j in range(len(nls)):
            if nls[j]["id"] == num:
                print("\n", nls[j]["question"])
                ans = nls[j]["choices"]
                for key, value in ans.items():
                    if value:
                        print(f"ANS :- {key}")
                        break
                break
    
else:
    print("Please choose question number from 1-9")
