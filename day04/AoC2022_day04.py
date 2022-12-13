# Advent Of Code 2022 Puzzle Day 4
# PART 1

containedTotal = 0
leftPair = []
rightPair = []

pairList = (open('./day04/input_day04.txt','r')).read().splitlines()

leftPair = pairList[0].split(',')[0].split('-')
rightPair = pairList[0].split(',')[1].split('-')

print(rightPair[1])