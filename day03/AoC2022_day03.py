# Advent Of Code 2022 Day 3
# PART 1

prioritySum = 0
leftSide = ''
rightSide = ''

rucksacksData = open('./day03/input_day03.txt','r')
rucksacksList = rucksacksData.read().splitlines()

print('Number of Rucksacks: ', len(rucksacksList))

print(len(rucksacksList[0]))
print(rucksacksList[:3])