from advent.year_2022.day_3 import *

text = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split("\n")

def test_rucksack_reorganisation_1():
    assert rucksack_reorganisation_1(text) == 157
    
def test_rucksack_reorganisation_2():
    assert rucksack_reorganisation_2(text) == 70