# AoC - 2015 - Day 12
# Guilherme M.
# 2024-03-05
import json

class NumberFinder:
    def calculate(self, data, puzzle_part=1):
        total = 0
        try:
            iter(data)
            if (type(data) == dict 
                    and puzzle_part == 2 
                    and 'red' in data.values()):
                #print(data)
                return 0
            for i in data:
                if type(data) == dict:
                    i = data[i]
                total += self.calculate(i, puzzle_part)
            return total
        except:
            if type(data) == int:
                return data
            else:
                return 0

with open('inputs/day12.txt', 'r') as file:
    json = json.load(file)

num_finder = NumberFinder()
print(f'part 1: {num_finder.calculate(json)}')
print(f'part 2: {num_finder.calculate(json, puzzle_part=2)}')
