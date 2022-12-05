import os
import string

def read_input(rel_path: str):
    file_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(file_dir, rel_path)
    file = open(file_name, 'r')
    return file.read().splitlines()

def split_input(input: str):
    divider = lines.index('')

    input = lines[:divider-1]
    input.reverse()

    commands = lines[divider+1:]
    return (input, commands)
    
def generate_stacks(input: str):
    return [list() for s in range(1,len(input),4)]

def fill_stacks(stacks: list[str], input):
    for line in input:
        j = 0
        for i in range(1,len(line),4):
            if line[i] != ' ':
                stacks[j].append(line[i])
            j += 1
    return stacks

def move_stacks(stacks: list[str], commands):
    for line in commands:
        command = line.split(' ')
        moves = int(command[1])
        from_stack = int(command[3]) - 1
        to_stack = int(command[5]) - 1

        stacks[to_stack].extend(stacks[from_stack][-moves:])
        del stacks[from_stack][-moves:]
    return stacks

lines = read_input('input/input.txt')

(input, commands) = split_input(lines)

empty_stacks = generate_stacks(input[0])

stacks = fill_stacks(empty_stacks, input)

stacks = move_stacks(stacks, commands)

result = ''.join([stack.pop() for stack in stacks])
print(result)