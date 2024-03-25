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
        
    def __get_distances(self, time = None):
        if time == None:
            time = self.time
        distances = [r.get_distance(time) for r in self.reindeers]
        return sorted(distances, 
                   key=lambda x: x[1])
    
    def __get_winners(self, time = None):
        distances = self.__get_distances(time)
        max_dist = max(distances, key=lambda x: x[1])[1]
        return list(filter(lambda x: x[1] == max_dist, distances))
    
    def get_winner(self):
        distances = [r.get_distance(self.time) for r in self.reindeers]
        return max(distances, 
                   key=lambda x: x[1])[1]
    
    def get_seconds_leading(self):
        score = {}
        for t in range(1, self.time + 1):
            winners = self.__get_winners(t)
            for name, _ in winners:
                score[name] = score.get(name, 0) + 1
        return max(score.items(), key=lambda x: x[1])[1]
    
    
reindeers = []

race_time = 2503

with open('inputs/day14.txt', 'r') as file:
    for line in file:
        reindeers.append(Reindeer(line))
race = Race(reindeers, race_time)

print(f'part 1: {race.get_winner()}')
print(f'part 2: {race.get_seconds_leading()}')