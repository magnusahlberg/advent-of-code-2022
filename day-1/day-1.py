import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')

lines = file.readlines()

elf = 1
calories = 0
highest_calories = 0
elf_with_highest_calories = 0


for line in lines:
    if line == "\n":
        if calories > highest_calories:
            elf_with_highest_calories = elf
            highest_calories = calories
        elf += 1
        calories = 0
    else:
        calories += int(line)

print(f'Elf: {elf_with_highest_calories}\nCalories: {highest_calories}\n')