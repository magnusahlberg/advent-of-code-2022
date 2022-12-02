import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.read()

elves = [elf.split('\n') for elf in lines.split('\n\n')]
sums = sorted([sum([int(calories) for calories in elf if calories != '']) for elf in elves])

top3_calories = sum(sums[-3:])

print(f"Sum of Top 3 Elves with most calories: {top3_calories}")