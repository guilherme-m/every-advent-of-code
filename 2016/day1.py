# AoC - 2016 - Day 1
# Guilherme M.
# 2024-09-12

import pandas as pd 
import numpy as np
from collections import defaultdict

with open('./inputs/day1.txt') as file:
    input = file.read()
    
movements = input.split(', ')


facing = 'N'

class Car:
    
    def __init__(self, facing_direction: str):
        self.facing_direction = facing_direction
        
        self.coordinates = pd.Series({'x': 0, 'y': 0})
        
        self.movement = {
            'N': (0, 1),
            'W': (-1, 0),
            'S': (0, -1),
            'E': (1, 0)
        }
        
    def rotate(self, rotation: str):
        new_direction = {
            'N':'W',
            'W':'S',
            'S':'E',
            'E':'N'
        }
        
        if rotation == 'R':
            new_direction = {v:k for k, v in new_direction.items()}
            
        self.facing_direction = new_direction[self.facing_direction]
    
    def move(self, units: int):
        
        self.coordinates += np.array(self.movement[self.facing_direction])*units

    def get_distance(self):
        return self.coordinates.sum()
    
    
class Car_Part_Two(Car):
    
    def __init__(self, facing_direction):
        super().__init__(facing_direction)
        self.visited = defaultdict(int)
        self.visited[tuple(self.coordinates)] = 1
        
        self.origin = None
        
    def move(self, units: int):
        
        for _ in range(units):
            self.coordinates += np.array(
                self.movement[self.facing_direction])
            
            self.visited[
                tuple(self.coordinates)
            ] += 1
            
            if (self.visited[tuple(self.coordinates)] > 1
                and self.origin is None):
                self.origin = self.coordinates.copy()
            
                
    def get_distance(self):
        return (self.origin).abs().sum()
           
        

    
car = Car(facing)

for move in movements:
    car.rotate(move[:1])
    car.move(int(move[1:]))
    
print(car.get_distance())

car_2 = Car_Part_Two(facing)
    
for move in movements:
    car_2.rotate(move[:1])
    car_2.move(int(move[1:]))
    
print(car_2.get_distance())
