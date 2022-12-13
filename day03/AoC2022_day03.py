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
"""
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
"""
print(range(1,len(rucksacksList)))

#while len(rucksacksList) != 0:
for idx in range(1,len(rucksacksList)):
    print('matching rucksack index : ', idx)
    for item in rucksacksList[currentRuckSack]:
        print(currentRuckSack, ' item: ',item)
        if rucksacksList[idx].find(item) >=0 :
            rucksacksList.pop(currentRuckSack)
            currentRuckSack = idx
            matchedItem = item
            foundMatch = True
            print('found match in rucksack: ', idx)
            break
    if foundMatch == True:
        print('BREAK')
        break


'''
for idx, ruckSack in enumerate(rucksacksList):
    for item in ruckSack:
        if rucksacksList[idx + 1].find(item) >= 0:
            rucksacksList.pop(idx)
        break
'''