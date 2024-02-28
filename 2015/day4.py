# AoC - 2015 - Day 4
# Guilherme M.
# 2024-02-27
from hashlib import md5

input = open('inputs/day4.txt', 'r').read()

hash_found = False
number = 1
while not hash_found:
    hash = md5(f'{input}{number}'.encode()).hexdigest()
    if hash[:5] == '00000':
        break
    number += 1
print(f'part 1: {number}')

hash_found = False
number = 1
while not hash_found:
    hash = md5(f'{input}{number}'.encode()).hexdigest()
    if hash[:6] == '000000':
        break
    number += 1
print(f'part 2: {number}')

