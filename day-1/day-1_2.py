import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')

lines = file.readlines()

elf = 1
calories = 0
elves = {}

for line in lines:
    if line == "\n":
        elves[elf] = calories
        elf += 1
        calories = 0
    else:
        calories += int(line)

sorted_calories = sorted(list(elves.values()))
top3 = sorted_calories[-3:]
sum = sum(top3)

print(f'Sum of the top 3 Elves: {sum}\n')