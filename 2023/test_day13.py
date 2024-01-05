from day13 import *

test_text="""
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""    

def test_mirrors_1():
    assert mirrors_1(test_text) == 405
    
def test_mirrors_2():
    assert mirrors_2(test_text) == 400