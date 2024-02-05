from advent.year_2019.day_24 import *

def test_bugs_1():
    text = '''....#
#..#.
#..##
..#..
#....'''

    assert bug_1(text) == 2129920
    
def test_bugs_2():
    text = '''....#
#..#.
#.?##
..#..
#....'''

    assert bug_2(text, 10) == 99