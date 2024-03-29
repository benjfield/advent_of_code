from advent.year_2023.day_18 import *

test_text=r"""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""  

def test_naive_dig_1():
    assert naive_dig_1(test_text) == 62

def test_dig_1():
    assert dig_1(test_text) == 62
    
def test_dig_2():
    assert dig_2(test_text) == 952408144115