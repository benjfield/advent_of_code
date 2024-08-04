from advent.year_2017.day_5 import *

text_1 ='''0
3
0
1
-3'''.split("\n")

def test_maze_1():
    assert maze_1(text_1) == 5
    
def test_maze_2():
    assert maze_2(text_1) == 10