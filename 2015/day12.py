# AoC - 2015 - Day 12
# Guilherme M.
# 2024-03-05
import json

class NumberFinder:
    def calculate(self, data):
        total = 0
        try:
            iter(data)
            for i in data:
                if type(data) == dict:
                    i = data[i]
                total += self.calculate(i)
            return total
        except:
            if type(data) == int:
                return data
            else:
                return 0

with open('inputs/day12.txt', 'r') as file:
    json = json.load(file)

num_finder = NumberFinder()
print(num_finder.calculate(json))
