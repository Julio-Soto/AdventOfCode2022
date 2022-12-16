# Advent Of Code 2022 Puzzle Day 5
# PART 1

# RAW DATA FROM FILE
numOfStackInputLines = 8
separation =  2     # number of lines that separate stack and moves data.
stacksLines =  []
movesLines = []

#MODEL DATA FOR PROCESSING
stacks = [[]]
moves = []
movingItem = ''
solution = ''

inputLines = open('./day05/input_day05.txt','r').read().splitlines() # a list of strings

# READ THE STACK INPUT LINES.
for i in range(numOfStackInputLines):
    stacksLines.append(inputLines[i])
    print(stacksLines[i])

# POPULATE MOVES LIST. READ THE MOVES DATA INPUT LINES AND CLEAN IT.
for lineNum in range (numOfStackInputLines + separation, len(inputLines)):
    moves.append((inputLines[lineNum].replace('move ','').replace('from ','').replace('to ','')).split())


# POPULATE STACKS LIST. IT WILL BE THE MODEL OF THE STACKS.
for stackIdx in range(1,10):
    stacks.append(list())
    for itemIdx in range(numOfStackInputLines-1,-1,-1):
        if stacksLines[itemIdx][(4 * stackIdx) - 3] != ' ':
            stacks[stackIdx].append(stacksLines[itemIdx][(4 * stackIdx) - 3])

# PRINTS THE DATA MODEL CURRENT STATE.
def stackPrint():
    for i in range(1,10):
        print(str(i) + ' ', end='')
        for item in stacks[i]:
            print(item,end='')
        print('')
    print('')

# MOVES A NUMBER OF ITEMS FROM ONE STACK TO OTHER.
def moveItems(number,fromStack,toStack):
    for k in range(number):
        movingItem = stacks[fromStack][len(stacks[fromStack])-1]
        stacks[toStack].append(movingItem)
        stacks[fromStack].pop()

# ACCESS A SINGLE ITEM BY STACK NUMBER AND ITEM INDEX.
#print(stacks[4][5])

print('Initial State:')
stackPrint()

for move in moves:
    moveItems(int(move[0]),int(move[1]),int(move[2]))

print('Final State:')
stackPrint()

for idx in range(1,10):
    solution += stacks[idx][-1]

print('Solution: ',solution)