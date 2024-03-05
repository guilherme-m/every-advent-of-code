# AoC - 2015 - Day 11
# Guilherme M.
# 2024-03-04
import string
import re


class Password:
    def __init__(self, passwd):
        self.passwd = passwd
        self.letters = {
            l: n
            for l, n in zip(string.ascii_lowercase, range(len(string.ascii_lowercase)))
        }

    def __check_sequence(self):
        for i in range(len(self.passwd[:-2])):
            ch1, ch2, ch3 = [self.letters[c] for c in self.passwd[i : i + 3]]
            diff1 = ch2 - ch1
            diff2 = ch3 - ch2
            if diff1 == 1 and diff2 == 1:
                return True
        return False

    def __check_letters(self):
        bad_letters_pattern = r"([iol])"
        has_bad_letters = re.match(bad_letters_pattern, self.passwd)
        if not has_bad_letters:
            return True
        else:
            return False
    
    def __check_pairs(self):
        pairs = r'((\w)\2)'
        total_pairs = re.findall(pairs, self.passwd)
        return len(total_pairs) > 1

    def is_valid(self):
        has_sequence = self.__check_sequence()
        has_only_permited_letters = self.__check_letters()
        has_pairs = self.__check_pairs()
        return has_sequence and has_only_permited_letters and has_pairs
    
    def __next_letter(self, ch):
        index = self.letters[ch]
        return string.ascii_lowercase[index + 1]
    
    def increment_passwd(self, start=-1):
        if self.passwd[start] == 'z':
            self.increment_passwd(start - 1)
        else:
            self.passwd = self.passwd[:start] + (self.__next_letter(self.passwd[start]) 
                                    + 'a'*(-1*start - 1))

txt = open('inputs/day11.txt', 'r').read()
passwd = Password(txt)

while True:
    passwd.increment_passwd()
    if passwd.is_valid():
        break
print(passwd.passwd)

while True:
    passwd.increment_passwd()
    if passwd.is_valid():
        break
print(passwd.passwd)