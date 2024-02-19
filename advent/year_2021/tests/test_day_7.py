from advent.year_2021.day_7 import *

def test_crabs_1():
    text = '''16,1,2,0,4,2,7,1,2,14'''
    assert crabs_1(text) == 37
    
def test_crabs_2():
    text = '''16,1,2,0,4,2,7,1,2,14'''
    assert crabs_2(text) == 168