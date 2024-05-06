from advent.year_2022.day_18 import *

text = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''.split("\n")

def test_boiling_boulders_1():
    assert boiling_boulders_1(text) == 64

def test_boiling_boulders_2():
    assert boiling_boulders_2(text) == 58