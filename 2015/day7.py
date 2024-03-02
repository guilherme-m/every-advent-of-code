# AoC - 2015 - Day 7
# Guilherme M.
# 2024-02-29
import re

class Circuit:
    def __init__(self):
        self.wires = {}
    
    def __get_value(self, value):
        try:
            return int(value)
        except:
            return self.wires[value]
            
    def __calculate_expression(self, expression):
        if len(expression) == 1:
            return self.__get_value(expression[0])
        elif len(expression) == 2:
            return ~self.__get_value(expression[1]) & 0xFFFF
        elif len(expression) == 3:
            x = self.__get_value(expression[0])
            y = self.__get_value(expression[2])
            operation = expression[1]
            
            if operation == 'AND':
                return x & y & 0xFFFF
            elif operation == 'OR':
                return x | y & 0xFFFF
            elif operation == 'LSHIFT':
                return x << y & 0xFFFF
            elif operation == 'RSHIFT':
                return x >> y & 0xFFFF
    
    def __parse_input(self, user_input):
        return re.match(r'(.+) -> (.+)', user_input).groups()
    
    def __input_result(self, user_input):
        expression, wire = self.__parse_input(user_input)
        
        return wire, self.__calculate_expression(expression.split(' '))
    
    def __check_signal(self, expression):
        return (expression.isnumeric() 
                    or expression in self.wires.keys())
    
    def put_into_wire(self, user_input):
        wire, value = self.__input_result(user_input)
        self.wires[wire] = value
    
    def inputs_have_signal(self, user_input):
        expression, _ = self.__parse_input(user_input)
        expression = expression.split(' ')
        
        if 1 <= len(expression) <= 2:
            i = len(expression) - 1
            return self.__check_signal(expression[i])
        elif len(expression) == 3:
            return (self.__check_signal(expression[0]) 
                    and self.__check_signal(expression[2]))
        
    def get(self, key):
        return self.wires[key]
    
    def __str__(self):
        w = sorted(
            self.wires.items(),
            key=lambda x: x[0]
        )
        return f'{dict(w)}'
    
circuit = Circuit()
input = open('inputs/day7.txt').read().split('\n')
while len(input) > 0:
    if (circuit.inputs_have_signal(input[0])):
        circuit.put_into_wire(input[0])
        input.pop(0)
    else:
        input = input[1:] + input[:1]
print(circuit.get('a'))