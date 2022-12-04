import os
import string

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.read().splitlines()

count = 0

for line in lines:
    pairs = line.split(',')

    sets = [[int(id) for id in ids] for ids in [set.split('-') for set in pairs]]
    # Check if first set is in second set
    if sets[0][0] >= sets[1][0] and sets[0][1] <= sets[1][1]:
        count += 1
    # Check if second set is in first set
    elif sets[1][0] >= sets[0][0] and sets[1][1] <= sets[0][1]:
        count += 1

print(count)