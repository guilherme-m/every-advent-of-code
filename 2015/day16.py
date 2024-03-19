# AoC - 2015 - Day 16
# Guilherme M.
# 2024-03-18
import re

machine_output = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

class GiftDetector:
    def __init__(self, machine_output):
        self.machine_output = self.__parse_items(machine_output)
        self.aunts = []

    def __parse_items(self, machine_output, linebreak='\n'):
        items = machine_output.split(linebreak)
        items = [i.split(': ') for i in items]
        items_dict = {i[0]: int(i[1]) for i in items}
        
        return items_dict
    
    def __parse_aunt_gift(self, gift):
        aunt, gift = re.match(r'(Sue \d+): (.+)',
                              gift).groups()
        gift = self.__parse_items(gift, ', ')
        
        return aunt, gift
    
    def check_aunt(self, gift):
        aunt, gift = self.__parse_aunt_gift(gift)
        if all(self.machine_output.get(k, None) == v for k, v in gift.items()):
            self.aunts.append(aunt)

gift_detector = GiftDetector(machine_output)

with open('inputs/day16.txt', 'r') as file:
    for line in file:
        gift_detector.check_aunt(line)

print(gift_detector.aunts)
