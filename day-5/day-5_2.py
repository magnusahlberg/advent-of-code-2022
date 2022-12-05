import os
import string

file_dir = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(file_dir, 'input/input.txt')
file = open(file_name, 'r')
lines = file.read().splitlines()

divider = lines.index('')
input = lines[:divider-1]
commands = lines[divider+1:]

input.reverse()

stacks = [list() for s in range(1,len(input[0]),4)]

for line in input:
    j = 0
    for i in range(1,len(line),4):
        if line[i] != ' ':
            stacks[j].append(line[i])
        j += 1


for line in commands:
    command = line.split(' ')
    moves = int(command[1])
    from_stack = int(command[3]) - 1
    to_stack = int(command[5]) - 1

    stacks[to_stack].extend(stacks[from_stack][-moves:])
    del stacks[from_stack][-moves:]

result = ''.join([stack.pop() for stack in stacks])
print(result)