# Advent Of Code 2022 Puzzle Day 5
# PART 1

numOfStackInputLines = 8
stacks = [[]]
stacksLines = []
movesLines = []

inputLines = open('./day05/input_day05.txt','r').read().splitlines()

# READ THE STACK INPUT LINES.
for i in range(numOfStackInputLines):
    stacksLines.append(inputLines[i])
    print(stacksLines[i])

# STACKS LIST WILL BE THE MODEL OF THE STACKS.
for stackIdx in range(1,10):
    stacks.append(list())
    for itemIdx in range(numOfStackInputLines-1,-1,-1):
        if stacksLines[itemIdx][(4 * stackIdx) - 3] != ' ':
            stacks[stackIdx].append(stacksLines[itemIdx][(4 * stackIdx) - 3])

print(stacks[4][5])