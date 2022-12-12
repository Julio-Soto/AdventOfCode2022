# Advent Of Code 2022 Day 3
# PART 1

prioritySum = 0
leftSide = ''
rightSide = ''

rucksacksData = open('./day03/input_day03.txt','r')
rucksacksList = rucksacksData.read().splitlines()

print('Number of Rucksacks: ', len(rucksacksList))

leftSide, rightSide = rucksacksList[0][:len(rucksacksList[0])//2], rucksacksList[0][len(rucksacksList[0])//2:] 

for item in leftSide:
    if rightSide.find(item) > 0:
        print(rightSide[rightSide.find(item)])
      

""""
print(leftSide[2])
print(rightSide)
print(len(rucksacksList[0]))
"""