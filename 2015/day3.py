# AoC - 2015 - Day 3
# Guilherme M.
# 2024-02-27
class GiftsDelivery():
    def __init__(self):
        self.current_position = (0, 0)
        self.direction_value = {
            '>': (1, 0),
            '<': (-1, 0),
            '^': (0, 1),
            'v': (0, -1)
        }
        self.visited_places = {
            self.current_position: 1
        }
    def move(self, direction):
        x, y = self.current_position
        delta_x, delta_y = self.direction_value[char]
        
        self.current_position = (x + delta_x, y + delta_y)
        
        self.visited_places[self.current_position] = 1 
        + self.visited_places.get(
            self.current_position, 0
        )
    def get_total_houses_visited(self):
        return len(self.visited_places)
    
        
input = open('inputs/day3.txt', 'r').read()

santa = GiftsDelivery()
for char in input:
    santa.move(char)
        
print(f'part 1: {santa.get_total_houses_visited()}')

santa = GiftsDelivery()
robot = GiftsDelivery()

for i, char in enumerate(input):
    if i%2 == 0:
        santa.move(char)
    else:
        robot.move(char)
total = len({**santa.visited_places, **robot.visited_places})
print(f'part 2: {total}')