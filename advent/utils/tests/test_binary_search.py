from advent.utils.binary_search import *

def greater_than_99(value):
    if value > 99:
        return True
    return False

def test_binary_search_1():
    assert find_first(greater_than_99, 0, 200) == 100
    
def test_binary_search_2():
    assert find_first(greater_than_99, 99, 99) == 100
    
def test_binary_search_3():
    assert find_first(greater_than_99, 99, 100) == 100

def greater_than_149(value):
    if value > 149:
        return True
    return False

def test_binary_search_4():
    assert find_first(greater_than_149, 141, 208) == 150

def greater_than_312(value):
    if value > 312:
        return True
    return False

def test_binary_search_4():
    assert find_first(greater_than_312, 281, 319) == 313