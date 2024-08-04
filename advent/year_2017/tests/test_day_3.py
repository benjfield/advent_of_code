from advent.year_2017.day_3 import *
    
def test_spiral_memory_1_2():
    assert spiral_memory_1("12") == 3
    
def test_spiral_memory_1_3():
    assert spiral_memory_1("23") == 2
    
def test_spiral_memory_1_4():
    assert spiral_memory_1("1024") == 31