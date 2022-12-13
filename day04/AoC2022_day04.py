# Advent Of Code 2022 Puzzle Day 4
# PART 1

notContainedTotal = 0
leftPair = []
rightPair = []

pairList = (open('./day04/input_day04.txt','r')).read().splitlines()

for pair in pairList:
    leftPair = pair.split(',')[0].split('-')
    rightPair = pair.split(',')[1].split('-')
    print(leftPair, ' ', rightPair)
    if int(leftPair[0]) - int(rightPair[0]) > 0 and int(leftPair[1]) - int(rightPair[1]) > 0: notContainedTotal += 1
    if int(leftPair[0]) - int(rightPair[0]) < 0 and int(leftPair[1]) - int(rightPair[1]) < 0: notContainedTotal += 1

print('Contained Total: ', (len(pairList) - notContainedTotal)) 
