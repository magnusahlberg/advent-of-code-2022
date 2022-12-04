import os
import string

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.readlines()

sum = 0

for line in lines:
    divider = int(len(line)/2)
    comp1 = line[:divider]
    comp2 = line[divider:]
    for letter in comp2:
        if letter in comp1:
            if letter.islower():
                score = string.ascii_lowercase.index(letter) + 1
            else:
                score = string.ascii_uppercase.index(letter) + 27
            sum += score
            break

print(sum)