# AoC - 2015 - Day 5
# Guilherme M.
# 2024-02-27
import re

total_nice_strings = 0


def is_nice(string):
    vowels = re.findall(r'[aeiou]', string)
    vowels_test = len(vowels) >= 3

    repeated_words = re.findall(r'(\w)\1', string)
    repeated_words_test = len(repeated_words) >= 1
    
    prohibited_words = re.findall(r'(ab|cd|pq|xy)', string)
    prohibited_words_test = len(prohibited_words) == 0
    
    return (vowels_test
            and repeated_words_test
            and prohibited_words_test)

with open("inputs/day5.txt", "r") as file:
    for line in file:
        if is_nice(line):
            total_nice_strings += 1

print(total_nice_strings)