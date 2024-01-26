from advent.year_2019.day_3 import *

def test_wires_1_1():
    test_text = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83'''
    assert wires_1(test_text) == 159

def test_wires_1_2():
    test_text = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
    assert wires_1(test_text) == 135
    
def test_wires_2_1():
    test_text = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83'''
    assert wires_2(test_text) == 610
        
def test_wires_2_2():
    test_text = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''
    assert wires_2(test_text) == 410