from advent.year_2021.day_5 import *

text = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

def test_vents_1():
    assert vents_1(text) == 5
    
def test_vents_2():
    assert vents_2(text) == 12