# Advent Of Code 2022 Puzzle Day 7
# PART 1

# RAW DATA FROM FILE

inputLinesFile = open('./day07/input_day07.txt','r')

inputLines =  inputLinesFile.read().splitlines()

for i, line in enumerate(inputLines):
    inputLines[i] = line.split()
    print(inputLines[i])
    
