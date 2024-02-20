from advent.year_2021.day_9 import *

def test_smoke_basin_1():
    text = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
    assert smoke_basin_1(text) == 15
    
def test_smoke_basin_2():
    text = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
    assert smoke_basin_2(text) == 1134