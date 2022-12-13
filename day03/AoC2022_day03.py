# Advent Of Code 2022 Day 3
# PART 1

prioritySum = 0
groupPrioritySum = 0
currentRuckSack = 0
foundMatch = False
matchedItem = ''
leftSide =  ''
rightSide = ''

rucksacksData = open('./day03/input_day03.txt','r')
rucksacksList = rucksacksData.read().splitlines()

print('Number of Rucksacks: ', len(rucksacksList))

for idx, ruckSack in enumerate(rucksacksList):
    leftSide, rightSide = ruckSack[:len(ruckSack)//2], ruckSack[len(ruckSack)//2:]
    print(idx, ' ', leftSide, " ", rightSide) 
    for item in leftSide:
        if rightSide.find(item) >= 0: 
            print('Item: ', rightSide[rightSide.find(item)])
            print('Priority: ', '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(rightSide[rightSide.find(item)]))
            prioritySum += '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(rightSide[rightSide.find(item)])
            break

print('Sum of Priorities: ', prioritySum)

# PART 2 - GROUPS OF 3

for idx in range(0,len(rucksacksList) - 2,3):
    for item in rucksacksList[idx]:
        if rucksacksList[idx +1].find(item) >= 0 and rucksacksList[idx + 2].find(item) >= 0:
            print('index: ',idx)
            print('item matched: ',item)
            groupPrioritySum += '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(item)
            break

print('elf group priority sum: ',groupPrioritySum)



