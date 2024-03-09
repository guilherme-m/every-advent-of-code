# AoC - 2015 - Day 14
# Guilherme M.
# 2024-03-08
import re

class Reindeer:
    def __init__(self, info):
        (self.name, self.speed, 
         self.moving_time, self.resting_time) = self.__parse_info(info)
    
    def __parse_info(self, info):
        # Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
        info_groups = re.match(
            r'(^\w+)\D+(\d+)\D+(\d+)\D+(\d+)', info
        ).groups()
        name, speed, moving_time, resting_time = info_groups
        return (name, int(speed), int(moving_time), int(resting_time))
    
    def get_distance(self, time):
        full_cycles = time // (self.moving_time + self.resting_time)
        remaing_time = time % (self.moving_time + self.resting_time)
        if remaing_time > self.moving_time:
            aditional_distance = self.moving_time
        else:
            aditional_distance = remaing_time
        return (self.name, 
                full_cycles*self.moving_time*self.speed 
                + aditional_distance*self.speed
                )

class Race:
    def __init__(self, reindeers, time):
        self.reindeers = reindeers
        self.time = time
        
    def get_winner(self):
        distances = [r.get_distance(self.time) for r in self.reindeers]
        return max(distances, 
                   key=lambda x: x[1])
    
    
reindeers = []

race_time = int(open('inputs/day14_2.txt', 'r').read())

with open('inputs/day14.txt', 'r') as file:
    for line in file:
        reindeers.append(Reindeer(line))
race = Race(reindeers, race_time)
print(race.get_winner())