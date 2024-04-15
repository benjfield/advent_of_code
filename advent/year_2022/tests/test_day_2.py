from advent.year_2022.day_2 import *

text = '''A Y
B X
C Z'''.split("\n")

def test_rock_paper_scissors_1():
    assert rock_paper_scissors_1(text) == 15
    
def test_rock_paper_scissors_2():
    assert rock_paper_scissors_2(text) == 12