from advent.year_2020.day_13 import *

def test_shuttle_search_1():
    text = '''939
7,13,x,x,59,x,31,19'''.split("\n")
    
    assert shuttle_search_1(text) == 295
    
def test_shuttle_search_2_1():
    text = '''939
7,13,x,x,59,x,31,19'''.split("\n")
    
    assert shuttle_search_2(text) == 1068781
        
def test_shuttle_search_2_2():
    text = '''939
1789,37,47,1889'''.split("\n")
    
    assert shuttle_search_2(text) == 1202161486