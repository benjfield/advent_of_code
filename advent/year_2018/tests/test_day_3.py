from advent.year_2018.day_3 import *

text = '''#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2'''.split("\n")

def test_fabric_slice_1():
    assert fabric_slice_1(text) == 4