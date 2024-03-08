# AoC - 2015 - Day 8
# Guilherme M.
# 2024-03-03
import re

total = 0
total_encoded = 0
total_repr = 0

with open("inputs/day8.txt", 'r') as file:
    for line in file:
        line = line.strip()
        line_repr = re.sub('"', r'\"', repr(line))
        
        total += len(line)
        total_encoded += len(line[1:-1].encode().decode('unicode-escape'))
        total_repr += len(line_repr)
        print(line, line_repr)
        
        
        
print(total - total_encoded)
print(total_repr - total)