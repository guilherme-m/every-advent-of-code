# AoC - 2015 - Day 5
# Guilherme M.
# 2024-02-27
import re

total_nice_strings = 0
total_nice_strings_part_two = 0

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

def is_nice_part_two(string):
    repeated_pair = re.findall(r'(\w\w).*\1', string)
    repeated_pair_test = len(repeated_pair) >= 1
    
    letter_between = re.findall(r'(\w)\w\1', string)
    letter_between_test = len(letter_between) >= 1
    
    return (letter_between_test
            and repeated_pair_test)

with open("inputs/day5.txt", "r") as file:
    for line in file:
        if is_nice(line):
            total_nice_strings += 1
        if is_nice_part_two(line):
            total_nice_strings_part_two += 1    
        

print(f'part 1: {total_nice_strings}\npart2: {total_nice_strings_part_two}')