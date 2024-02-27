# AoC - 2015 - Day 2
# Guilherme M.
# 2024-02-26
import re

total_paper_area = 0
total_ribbon_area = 0

def parse_dimensions(dimensions_string):
    dimensions = re.findall(r'(\d+)', dimensions_string)
    
    return [int(d) for d in dimensions]

def calculate_paper_area(dimensions_string):
    # Part 1:
    l, w, h = parse_dimensions(dimensions_string)
    areas = [l*w, w*h, h*l]
    
    return sum(2*area for area in areas) + min(areas)

def calculate_ribbon_area(dimensions_string):
    # Part 2:
    l, w, h = parse_dimensions(dimensions_string)
    perimeters = [l+w, l+h, w+h]
    
    return min(perimeters)*2 + l*w*h

with open('inputs/day2.txt', 'r') as file:
    for line in file:
        total_paper_area += calculate_paper_area(line)
        total_ribbon_area += calculate_ribbon_area(line)
        
print(f'part 1: {total_paper_area}')
print(f'part 2: {total_ribbon_area}')

