"""

Problem :
You are a Pokémon trainer. Each Pokémon has its own power, described by a positive 
integer value. As you travel, you watch Pokémon and you catch each of them. After each 
catch, you have to display maximum and minimum powers of Pokémon caught so far. You must 
have linear time complexity. So sorting won’t help here. Try having minimum extra space 
complexity.

"""
powerList = [3,8,9,7]

minNum, maxNum = 0, 0

for i in powerList:
    if minNum == 0 and maxNum == 0:
        minNum, maxNum = i, i
    else:
        minNum = min(minNum, i)
        maxNum = max(maxNum, i)
    print(minNum, maxNum)