# Advent of code puzzle Day 1

groupCalories = []
calorieSum = 0
maxCalories = 0
nunberOfElves = 0
top3ElvesCalories = 0
sortedGroupCalories = []

caloriesData = open('./day01/input_day01.txt','r')
singleCalories = caloriesData.readlines()
caloriesData.close()

for singleCalorieAmount in singleCalories:
    if singleCalorieAmount.strip():
        calorieSum += int(singleCalorieAmount)
    else:
        groupCalories.append(calorieSum)
        calorieSum = 0

for groupCalorieAmount in groupCalories:
    maxCalories = max(maxCalories,groupCalorieAmount)

print('Calories carried by top elf: ' + str(maxCalories))

# PART 2

sortedGroupCalories = sorted(groupCalories)

numberOfElves = len(sortedGroupCalories)
for i in range(1,4):
    top3ElvesCalories += sortedGroupCalories[numberOfElves - i]

print('Calorie sum of top 3 elves: ' + str(top3ElvesCalories))
