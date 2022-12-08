# Advent of code puzzle Day 1

calories = []

inputData = open('./day01/input_day01.txt','r')
for line in inputData:
    if line.strip():
        calories.append(line)

inputData.close()

print(calories)
