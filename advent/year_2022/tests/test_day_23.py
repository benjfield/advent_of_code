from advent.year_2022.day_23 import *

text = '''....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''.split("\n")

def test_unstable_diffusion_1():
    assert unstable_diffusion_1(text) == 110
    
#def test_unstable_diffusion_2():
#    assert unstable_diffusion_2(text) == 20