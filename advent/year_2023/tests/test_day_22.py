from advent.year_2023.day_22 import *

test_text=r"""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

def test_brick_1():
    assert brick_1(test_text) == 5
    
def test_brick_2():
    assert brick_2(test_text) == 7