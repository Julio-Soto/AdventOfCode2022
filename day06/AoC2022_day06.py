# Advent Of Code 2022 Puzzle Day 6
# PART 1

# RAW DATA FROM FILE

str = ''
startChar01 = 4  # use for PART 1
startChar02 = 14 # use for PART 2

dataStreamFile = open('./day06/input_day06.txt')
dataStream = dataStreamFile.read()
dataStreamFile.close()

for currentIDX in range(startChar02,len(dataStream)):
    str = dataStream[currentIDX-startChar02 : -len(dataStream) + currentIDX]
    if len(str) == len(set(str)):
        print(currentIDX)
        print(str)
        break
