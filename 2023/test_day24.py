from day24 import *

test_text=r"""19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

def test_hail_1():
    assert hail_1(test_text) == 2
    
def test_hail_2():
    assert hail_2(test_text) == 47