# Advent Of Code 2022 Puzzle Day 6
# PART 1

# RAW DATA FROM FILE

str = ''
startChar = 4

dataStreamFile = open('./day06/input_day06.txt')
dataStream = dataStreamFile.read()
dataStreamFile.close()

for currentIDX in range(startChar,len(dataStream)):
    str = dataStream[currentIDX-4 : -len(dataStream) + currentIDX]
    if len(str) == len(set(str)):
        print(currentIDX)
        print(str)
        break
