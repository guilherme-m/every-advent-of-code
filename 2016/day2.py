# AoC - 2016 - Day 2
# Guilherme M.
# 2024-09-14

import numpy as np

keypad = np.arange(1, 10).reshape((3,3))

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

position = np.array([1, 1])

password = []


with open('inputs/day2.txt') as file:
    instructions = file.read().split('\n')

def is_valid_index(idx, part=1):
    idx = np.array(idx)
    
    is_valid = (idx >= 0).all() and (idx < keypad.shape).all()
    
    if part == 2 and is_valid:
        is_valid = is_valid and keypad[idx[0], idx[1]] != '0'
    
    return is_valid

def get_digit(instruction, part=1):
    global position
    for direction in instruction:
        new_position = position + directions[direction]
        if is_valid_index(new_position, part):
            position = new_position
    
    password.append(keypad[position[0], position[1]].item())
    
for instruction in instructions:
    get_digit(instruction)
    
print(''.join(str(i) for i in password))
    
keypad = np.array([
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
])

position = np.array([2, 0])

password = []

for instruction in instructions:
    get_digit(instruction, part=2)
    
print(''.join(password))
