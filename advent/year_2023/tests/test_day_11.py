from advent.year_2023.day_11 import *

test_text="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""    

def test_stars_1():
    assert stars_1(test_text) == 374
    
def test_stars_2_1():
    assert stars_2(test_text, 10) == 1030
    
def test_stars_2_2():
    assert stars_2(test_text, 100) == 8410