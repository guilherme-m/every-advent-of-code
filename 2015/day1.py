# AoC - 2015 - Day 1
# Guilherme M.
# 2024-02-26

with open('inputs/day1.txt', 'r') as file:
    input = file.read()
    
floor = 0

for ch in input:
    if ch == '(':
        floor += 1
    else:
        floor -= 1
        
print(floor)