# Advent of Code 2022 Day 2 puzzle


finalScore = 0

games = open('./day02/input_day02.txt','r')
gamesList = games.readlines()
print('Number of Games: ',len(gamesList))
for game in gamesList:
    if game[0] == 'A' and game[2] == 'X':
        finalScore += (3 + 1)
    if game[0] == 'A' and game[2] == 'Y':
        finalScore += (6 + 2)
    if game[0] == 'A' and game[2] == 'Z':
        finalScore += (0 + 3)
    if game[0] == 'B' and game[2] == 'X':
        finalScore += (0 + 1)
    if game[0] == 'B' and game[2] == 'Y':
        finalScore += (3 + 2)
    if game[0] == 'B' and game[2] == 'Z':
        finalScore += (6 + 3)
    if game[0] == 'C' and game[2] == 'X':
        finalScore += (6 + 1)
    if game[0] == 'C' and game[2] == 'Y':
        finalScore += (0 + 2)
    if game[0] == 'C' and game[2] == 'Z':
        finalScore += (3 + 3)

print('Final Score: ', finalScore)
