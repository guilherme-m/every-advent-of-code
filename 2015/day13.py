# AoC - 2015 - Day 13
# Guilherme M.
# 2024-03-08
import itertools
import re

class Table:
    def __init__(self, people):
        self.people = people
    
    def __pair_score(self, person, person_at_side):
        return self.people.people[person][person_at_side]
    
    def __get_score(self, perm):
        score = 0
        for i, person in enumerate(perm):
            if i == 0:
                left_side_person_index = -1
            else:
                left_side_person_index = i - 1
            if i == len(perm) - 1:
                right_side_person_index = 0
            else:
                right_side_person_index = i + 1
            
            score += self.__pair_score(person, perm[left_side_person_index])
            score += self.__pair_score(person, perm[right_side_person_index])
        return score
    
    def get_best_score(self):
        best_score = None
        for perm in self.people.get_permutations():
            new_score = self.__get_score(perm)
            if best_score == None:
                best_score = new_score
            if new_score > best_score:
                best_score = new_score
        return best_score
    
class People:
    def __init__(self):
        self.people = {}
    
    def update(self, info):
        #Eric would gain 95 happiness units by sitting next to Frank.
        person, sign, points, person_at_side = re.match(
            r'(\w+) \w+ (\w+) (\d+) .+ (\w+)\.',
            info
        ).groups()
        if sign == 'gain':
            sign = 1
        else:
            sign = -1
        
        self.people[person] = self.people.get(person, {})
        self.people[person][person_at_side] = sign * int(points)
        
    def get_permutations(self):
        perm = itertools.permutations(self.people.keys())
        return list(perm)
    
    def add_dummy_person(self, name='Dummy Person'):
        self.people[name] = {}
        for k in self.people:
            if k != name:
                self.people[k][name] = 0
            self.people[name][k] = 0
            
    def __str__(self):
        return f'{self.people}'

people = People()
with open('inputs/day13.txt', 'r') as file:
    for line in file:
        people.update(line)
table = Table(people)
print(table.get_best_score())

people.add_dummy_person()
table = Table(people)
print(table.get_best_score())