import os
import string
from functools import reduce 

def read_input(rel_path: str):
    file_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(file_dir, rel_path)
    file = open(file_name, 'r')
    return file.read()

distinct_chars = 4

input = read_input('input/input.txt')

for i in range(distinct_chars,len(input)):
    seek_string = input[i-distinct_chars:i]

    count = sum([seek_string.count(char) for char in seek_string])

    if count == distinct_chars:
        print(i)
        break