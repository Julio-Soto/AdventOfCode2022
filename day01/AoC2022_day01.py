# Advent of code puzzle Day 1

groupCalories = []
calorieSum = 0
maxCalories = 0

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

print(groupCalories)
print(maxCalories)
