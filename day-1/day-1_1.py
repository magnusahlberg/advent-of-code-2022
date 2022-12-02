import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.read()

elves = [elf.split('\n') for elf in lines.split('\n\n')]
sums = sorted([sum([int(calories) for calories in elf if calories != '']) for elf in elves])

most_calories = sums[-1]

print(f"Elf with most calories: {most_calories}")