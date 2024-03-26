# AoC - 2015 - Day 18
# Guilherme M.
# 2024-03-25
import numpy as np

class Grid:
    def __init__(self, grid:np.array):
        self.grid = np.copy(grid)
    
    def change_lights(self, part=1):
        if part == 2:
            self.grid[0, 0] = '#'
            self.grid[0, -1] = '#'
            self.grid[-1, 0] = '#'
            self.grid[-1, -1] = '#'
        
        new_grid = np.copy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                neighbors = self.grid[max(0,i-1):i+2, max(0,j-1):j+2]
                if self.grid[i,j] == '.':
                    if np.count_nonzero(neighbors == '#') == 3:
                        new_grid[i,j] = '#'
                else:
                    if not 2 <= np.count_nonzero(neighbors == '#') - 1 <= 3:
                        new_grid[i,j] = '.'
        if part == 2:
            new_grid[0, 0] = '#'
            new_grid[0, -1] = '#'
            new_grid[-1, 0] = '#'
            new_grid[-1, -1] = '#'
            
        self.grid = new_grid                             
    
    def get_lights_on(self):
        return np.count_nonzero(self.grid == '#')
    
grid_txt = open('inputs/day18.txt', 'r').read().split('\n')
grid_txt = [list(line) for line in grid_txt]
grid_txt = np.array(grid_txt)

steps = 100

grid = Grid(grid_txt)
grid_part_2 = Grid(grid_txt)

for _ in range(steps):
    grid.change_lights()
    grid_part_2.change_lights(part=2)
    
print(f'part 1: {grid.get_lights_on()}')
print(f'part 2: {grid_part_2.get_lights_on()}')