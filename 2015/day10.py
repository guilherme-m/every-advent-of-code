# AoC - 2015 - Day 10
# Guilherme M.
# 2024-03-04
class Converter:
    def __init__(self, txt_input):
        self.txt_input = txt_input
        
    def __str__(self):
        return self.txt_input
        
    def __convert_part(self, txt):
        if len(txt) == 0: 
            return ''
        return f'{len(txt)}{txt[:1]}'
    
    def convert(self):
        txt_start = list(self.txt_input)
        txt_end = ''
        txt_part = ''
        while len(txt_start) > 0:
            if txt_start[0] != txt_part[-1:]:
                txt_end += self.__convert_part(txt_part)
                txt_part = txt_start.pop(0)
            else:
                txt_part += txt_start.pop(0)
        txt_end += self.__convert_part(txt_part)
        self.txt_input = ''.join(txt_end)
    
    


txt_input = open('inputs/day10.txt', 'r').read()
converter = Converter(txt_input)
for i in range(40):
    converter.convert()
print(len(converter.txt_input))
