from advent.year_2020.day_17 import *

def test_conway_cubes_1():
    text = '''.#.
..#
###'''.split("\n")
    
    assert conway_cubes_1(text) == 112

def test_conway_cubes_2():
    text = '''.#.
..#
###'''.split("\n")
    
    assert conway_cubes_2(text) == 848