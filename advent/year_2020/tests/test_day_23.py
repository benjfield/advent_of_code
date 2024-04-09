from advent.year_2020.day_23 import *

def test_crab_cups_1():
    text = '''389125467'''.split("\n")
    
    assert crab_cups_1(text) == 67384529
    
def test_crab_cups_2():
    text = '''389125467'''.split("\n")
    
    #assert crab_cups_2(text) == 149245887792