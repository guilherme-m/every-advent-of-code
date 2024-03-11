# AoC - 2015 - Day 15
# Guilherme M.
# 2024-03-11
import re
import numpy as np
import itertools
import math

class Ingredient:
    def __init__(self, info, quantity = None):
        #Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
        parsed_info = re.findall(r'^[^:]+|-{0,1}\d+', info)
        
        self.name = parsed_info[0]
        
        self.attributes = {
            'capacity': int(parsed_info[1]),
            'durability': int(parsed_info[2]),
            'flavor': int(parsed_info[3]),
            'texture': int(parsed_info[4]),
            'calories': int(parsed_info[5])
        }
        
        self.quantity = quantity
    
    def __str__(self):
        return f'''{self.name}:
\t==> {self.attributes} | {self.quantity}
'''
    def set_quantity(self, quantity):
        self.quantity = quantity
        
class Cookie:
    def __init__(self, ingredients: list[Ingredient]):
        self.ingredients = ingredients
        self.score = self.__get_score()
        self.calories = self.__get_calories()
        
    def __get_calories(self):
        return sum(i.quantity*i.attributes['calories'] for i in self.ingredients)
        
    def __get_score(self):
        partial_scores = {
            'capacity': 0,
            'durability': 0,
            'flavor': 0,
            'texture': 0
        }
        for ingredient in self.ingredients:
            partial_scores = {k: partial_scores.get(k, 0) 
                              + ingredient.attributes[k] * ingredient.quantity
                              for k in partial_scores}
        
        partial_scores = {k: max([0, v]) for k, v in partial_scores.items()}
        score = math.prod(partial_scores.values())
                
        return score

def get_spoons(num_ingredients, spoons):
    masks = np.identity(num_ingredients, dtype=int)
    return [list(sum(x)) 
            for x in itertools.combinations_with_replacement(masks, spoons)]
    
ingredients = []
with open('inputs/day15.txt', 'r') as file:
    for line in file:
        ingredients.append(Ingredient(line))
        
spoons = get_spoons(len(ingredients), 100)
best_cookie = None

for spoon in spoons:
    [i.set_quantity(s) for i, s in zip(ingredients, spoon)]
    new_cookie = Cookie(ingredients)
    if best_cookie == None:
        best_cookie = new_cookie
    else:
        if new_cookie.score > best_cookie.score:
            best_cookie = new_cookie
            
print(f'part 1: {best_cookie.score}')

best_cookie = None
for spoon in spoons:
    [i.set_quantity(s) for i, s in zip(ingredients, spoon)]
    new_cookie = Cookie(ingredients)
    if new_cookie.calories != 500:
        continue
    if best_cookie == None:
        best_cookie = new_cookie
    else:
        if new_cookie.score > best_cookie.score:
            best_cookie = new_cookie
print(f'part 2: {best_cookie.score}')