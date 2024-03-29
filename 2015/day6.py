# AoC - 2015 - Day 6
# Guilherme M.
# 2024-02-28
import numpy as np
import re

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((self.size, self.size), dtype=np.int32)
    
    def parse_prompt(self, input):
        patt = r'(\D+)([\d,]+)\D+([\d,]+)'
        matches = re.match(patt, input).groups()
        
        prompt = matches[0].strip()
        corner_1 = tuple(int(x) for x in matches[1].split(','))
        corner_2 = tuple(int(x) for x in matches[2].split(','))
        
        return (prompt, corner_1, corner_2)
    
    def update_grid(self, change: str, start, end):
        
        x0, y0 = start
        x1, y1 = end
        original_slice = self.grid[x0:x1+1, y0:y1+1].copy()
        
        if change == 'toggle':
            self.grid[x0:x1+1, y0:y1+1] = 1 - original_slice
        elif change.endswith('on'):
            self.grid[x0:x1+1, y0:y1+1] = 1
        elif change.endswith('off'):
            self.grid[x0:x1+1, y0:y1+1] = 0
    
    def update_grid_part_2(self, change: str, start, end):
        
        x0, y0 = start
        x1, y1 = end
        
        if change == 'toggle':
            self.grid[x0:x1+1, y0:y1+1] += 2
        elif change.endswith('on'):
            self.grid[x0:x1+1, y0:y1+1] += 1
        elif change.endswith('off'):
            self.grid[x0:x1+1, y0:y1+1] = np.vectorize(lambda x: max(0, x-1))(
                self.grid[x0:x1+1, y0:y1+1]
            )
        
    def alter_lights(self, input, part_1=True):
        change, start, end = self.parse_prompt(input)
        if part_1:
            self.update_grid(change, start, end)
        else:
            self.update_grid_part_2(change, start, end)
        
    def get_total_lights_on(self):
        return np.sum(self.grid, dtype=np.int32)
        

grid = Grid(1000)
grid_part_2 = Grid(1000)
with open('inputs/day6.txt', 'r') as file:
    for line in file:
        grid.alter_lights(line)
        grid_part_2.alter_lights(line, False)
print(f'part 1: {grid.get_total_lights_on()}')
print(f'part 2: {grid_part_2.get_total_lights_on()}')



