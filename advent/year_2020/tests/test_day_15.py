from advent.year_2020.day_15 import *

def test_rambunctious_recitation_1_1():
    text = '''0,3,6'''.split("\n")
    
    assert rambunctious_recitation_1(text) == 436
    
def test_rambunctious_recitation_1_2():
    text = '''1,3,2'''.split("\n")
    
    assert rambunctious_recitation_1(text) == 1
    
def test_rambunctious_recitation_1_3():
    text = '''2,1,3'''.split("\n")
    
    assert rambunctious_recitation_1(text) == 10