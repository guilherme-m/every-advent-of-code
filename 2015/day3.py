# AoC - 2015 - Day 3
# Guilherme M.
# 2024-02-27

current_position = (0, 0)
direction_value = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, 1),
    'v': (0, -1)
}
visited_places = {
    current_position: 1
}
input = open('inputs/day3.txt', 'r').read()
for char in input:
    x, y = current_position
    delta_x, delta_y = direction_value[char]
    current_position = (x + delta_x, y + delta_y)
    visited_places[current_position] = 1 + visited_places.get(
        current_position, 0
    )
        
print(len(visited_places))