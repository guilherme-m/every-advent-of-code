# AoC - 2015 - Day 17
# Guilherme M.
# 2024-03-18
import itertools

containers = open('inputs/day17.txt', 'r').read().split('\n')
containers = [int(c) for c in containers]

class FillingCombinations:
    def __init__(self, liters, containers):
        self.liters = liters
        self.containers = containers
        
    def __find_filling_options(self):
        smallest_container = min(self.containers)
        max_num_of_containers = self.liters // smallest_container
        
        container_combinations = []
        
        for i in range(1, max_num_of_containers + 1):
            container_combinations += itertools.combinations(
                self.containers,
                i
            )
            
        return [c for c in container_combinations if sum(c) == self.liters]
    
    def get_num_of_combinations(self):
        return len(self.__find_filling_options())

fill_combs = FillingCombinations(150, containers)
print(fill_combs.get_num_of_combinations())
