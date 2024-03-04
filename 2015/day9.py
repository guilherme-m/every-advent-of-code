# AoC - 2015 - Day 9
# Guilherme M.
# 2024-03-03
import re


class City:
    def __init__(self, name):
        self.name = name
        self.destinations = {}

    def add_destination(self, city_name, distance):
        self.destinations[city_name] = distance


class Paths:
    def __init__(self, cities):
        self.cities = cities
        self.paths = {city: 0 for city in cities}

    def __calculate_paths(self):
        has_paths = True
        depth = 0
        while has_paths:
            has_paths = False
            for path, distance in {
                path: dist
                for path, dist in self.paths.items()
                if len(path.split(",")) == depth + 1
            }.items():
                path = path.split(",")
                last_city = path[-1]
                if last_city not in self.cities:
                    continue
                for dest, dest_distance in self.cities[last_city].destinations.items():
                    if dest not in path[:-1]:
                        self.paths[",".join(path + [dest])] = distance + dest_distance
                        has_paths = True

            depth += 1

    def __get_path(self, fun = min):
        self.__calculate_paths()
        max_path = max(len(k.split(",")) for k in self.paths)
        filtered_paths = {
            k: v for k, v in self.paths.items() if len(k.split(",")) == max_path
        }
        shortest_distance = fun(v for v in filtered_paths.values())
        return {k: v for k, v in filtered_paths.items() if v == shortest_distance}
    
    def get_shortest_path(self):
        return self.__get_path(min)
    
    def get_longest_path(self):
        return self.__get_path(max)


cities = {}
pattern = r"(\w+) to (\w+) = (\d+)"  # Faerun to Tristram = 65
with open("inputs/day9.txt", "r") as file:
    for line in file:
        origin, destination, dist = re.match(pattern, line).groups()
        dist = int(dist)
        if origin not in cities:
            cities[origin] = City(origin)
        if destination not in cities:
            cities[destination] = City(destination)
        cities[origin].add_destination(destination, dist)
        cities[destination].add_destination(origin, dist)

paths = Paths(cities)
print(f'{paths.get_shortest_path()}')
print(f'{paths.get_longest_path()}')

