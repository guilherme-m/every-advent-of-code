# AoC - 2015 - Day 7
# Guilherme M.
# 2024-03-02
import re

class Circuit:
    gates = {
       'AND': lambda x, y: x & y & 0xFFFF,
       'OR':  lambda x, y: x | y & 0xFFFF,
       'LSHIFT': lambda x, y: x << y & 0xFFFF,
       'RSHIFT': lambda x, y: x >> y & 0xFFFF,
       'NOT': lambda x: ~x & 0xFFFF
    }

    def __init__(self):
        self.wires = {}
    
    def __str__(self):
        wires_str = {k: v.result for k, v in self.wires.items()}
        return f'{dict(sorted(wires_str.items()))}'
    
    def put_into_wire(self, user_input: str):
        gate, wire = re.match(r'(.+) -> (.+)', user_input).groups()
        self.wires[wire] = Wire(gate.strip(), None)
    
    def get(self, wire):
        if self.wires[wire].result:
            return self.wires[wire].result
        else:
            result = self.__calculate(wire)
            self.wires[wire].result = result
            return result
    
    def set(self, wire, value):
        self.wires[wire].result = value
    
    def __get_value(self, value:str):
        if value.isnumeric():
            return int(value)
        else:
            return self.get(value)
    
    def __calculate(self, wire):
        gate = self.wires[wire].gate.split()
        if len(gate) == 1:
            return self.__get_value(gate[0])
        elif len(gate) == 2:
            return self.gates[gate[0]](self.__get_value(gate[1]))
        elif len(gate) == 3:
            return self.gates[gate[1]](
                self.__get_value(gate[0]),
                self.__get_value(gate[2])
                )
            
        

class Wire:
    def __init__(self, gate, result):
        self.gate = gate
        self.result = result
        
    def __str__(self):
        d = {'operation': self.gate,
                'result': self.result}
        return f'{d}'
    
circuit = Circuit()

with open('inputs/day7.txt', 'r') as file:
    for line in file:
        circuit.put_into_wire(line)
print(f'part1 : {circuit.get("a")}')