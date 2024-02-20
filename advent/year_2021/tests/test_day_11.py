from advent.year_2021.day_11 import *

def test_octopus_1():
    text = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''
    assert octopus_1(text) == 1656
    
def test_octopus_2():
    text = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''
    assert octopus_2(text) == 195