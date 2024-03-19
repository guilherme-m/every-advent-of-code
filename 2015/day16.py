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
    
    def __compare_items(self, gift, value, part):
        comparison = self.machine_output.get(gift, 0) == value
        if part == 2:
            if gift in ['cats', 'trees']:
                comparison = value > self.machine_output.get(gift, 0)
            elif gift in ['pomeranians', 'goldfish']:
                comparison = value < self.machine_output.get(gift, 0)
        
        return comparison
                
    def check_aunt(self, gift, part=1):
        aunt, gift = self.__parse_aunt_gift(gift)
        if all(self.__compare_items(k,v, part) for k, v in gift.items()):
            self.aunts.append(aunt)

gift_detector = GiftDetector(machine_output)
gift_detector_part_2 = GiftDetector(machine_output)

with open('inputs/day16.txt', 'r') as file:
    for line in file:
        gift_detector.check_aunt(line)
        gift_detector_part_2.check_aunt(line, 2)

print(f' part 1: {gift_detector.aunts}')
print(f' part 2: {gift_detector_part_2.aunts}')
