# AoC - 2015 - Day 19
# Guilherme M.
# 2024-09-14
import re
import pandas as pd
import numpy as np

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

start = [0, [['e']]]

def find_medicine(start):
    counter, fabrications = start
    counter += 1
    new_fabrications = set()
    for fab in fabrications:
        
        fab = pd.Series(fab)
        for conv in conversions:
            indexes = np.where(fab == conv[0])[0]
            for idx in indexes:
                
                new_fabrications.add(''.join(np.where(
                    range(len(fab)) == idx, conv[1], np.array(fab)
                    ).tolist()))
                
    new_fabrications = [re.findall(r'[A-Z][a-z]{0,1}', f) for f in new_fabrications]
    print('--> ', len(new_fabrications))
    new_start = [counter, new_fabrications]
    if ''.join(molecules) in [''.join(s) for s in new_fabrications]:
        return counter
    else:
        return find_medicine(new_start)
        
print(find_medicine(start))