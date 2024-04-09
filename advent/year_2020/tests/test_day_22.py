from advent.year_2020.day_22 import *

def test_crab_combat_1():
    text = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''.split("\n")
    
    assert crab_combat_1(text) == 306
    
def test_crab_combat_2():
    text = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''.split("\n")
    
    assert crab_combat_2(text) == 291
        
def test_crab_combat_2_infinite_loop():
    text = '''Player 1:
43
19

Player 2:
2
29
14'''.split("\n")
    
    assert crab_combat_2(text) == 105