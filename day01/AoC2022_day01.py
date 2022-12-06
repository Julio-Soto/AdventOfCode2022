# Advent of code puzzle Day 1

calories = []
with open('input_day01.txt', 'r') as f:
    for line in f:
        if line.strip():  # Skip blank lines.
            calories.append(int(line))    
