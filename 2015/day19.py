# AoC - 2015 - Day 19
# Guilherme M.
# 2024-09-14
import re
import pandas as pd
import numpy as np
import random

conversions = []

conversion_pattern = re.compile(r'(.+) => (.+)')

with open('inputs/day19.txt') as file:
    for line in file:
        pattern_match = re.match(conversion_pattern, line)
        if pattern_match:
            k, v = pattern_match.groups()
            conversions.append((k, v))
        else:
            if len(line) > 1:
                molecules = pd.Series(re.findall(r'[A-Z][a-z]{0,1}', line))
        
total_conversions = set()

for conv in conversions:
    indexes = np.where(molecules == conv[0])[0]
    for idx in indexes:
        total_conversions.add(
            ''.join(np.where(molecules.index == idx, conv[1], molecules))
        )

print(len(total_conversions))

molecules = ''.join(molecules)

def find_medicine(conversions_list):
    new_molecules = molecules
    counter = 0
    patt = re.compile(r'^e+$')
    for _ in range(1_000):
        random.shuffle(conversions_list)
        if re.match(patt, new_molecules):
            break
        for c in conversions_list:
            idx = [s.start() for s in re.finditer(c[1], new_molecules)]
            
            if len(idx) > 0:
                idx = random.sample(idx, 1)[0]
                new_molecules = new_molecules[:idx] + c[0] + new_molecules[idx + len(c[1]):]
                counter += 1
                break
    return counter, new_molecules
    
    
trials = 25
success = []

for i in range(trials):
    counter, conversion = find_medicine(conversions)
    if conversion == 'e':
        success.append((counter, conversion))

min_steps = sorted(success, key=lambda x: x[0])

try:
    min_steps = min_steps[0][0]
except:
    min_steps = ''

print(min_steps)