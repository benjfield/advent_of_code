from advent.year_2020.day_18 import *

def test_operation_order_1():
    text = '''1 + (2 * 3) + (4 * (5 + 6))'''.split("\n")
    
    assert operation_order_1(text) == 51
    
def test_operation_order_2_1():
    text = '''1 + 2 * 3 + 4 * 5 + 6'''.split("\n")
    
    assert operation_order_2(text) == 231
          
def test_operation_order_2_2():
    text = '''1 + (2 * 3) + (4 * (5 + 6))'''.split("\n")
    
    assert operation_order_2(text) == 51
          
def test_operation_order_2_3():
    text = '''2 * 3 + (4 * 5)'''.split("\n")
    
    assert operation_order_2(text) == 46

def test_operation_order_2_4():
    text = '''5 + (8 * 3 + 9 + 3 * 4 * 3)'''.split("\n")
    
    assert operation_order_2(text) == 1445

def test_operation_order_2_5():
    text = '''5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'''.split("\n")
    
    assert operation_order_2(text) == 669060
        
def test_operation_order_2_6():
    text = '''((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'''.split("\n")
    
    assert operation_order_2(text) == 23340