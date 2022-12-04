import os
import string

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.readlines()

sum = 0

for (index,line) in enumerate(lines[::3]):
    i = index * 3
    for letter in line:
        if letter in lines[i+1] and letter in lines[i+2]:
            if letter.islower():
                score = string.ascii_lowercase.index(letter) + 1
            else:
                score = string.ascii_uppercase.index(letter) + 27
            sum += score
            break

print(sum)