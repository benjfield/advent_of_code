from advent.year_2022.day_5 import *

text = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split("\n")

def test_supply_stacks_1():
    assert supply_stacks_1(text) == "CMZ"
    
def test_supply_stacks_2():
    assert supply_stacks_2(text) == "MCD"