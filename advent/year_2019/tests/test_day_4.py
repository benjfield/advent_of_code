from advent.year_2019.day_4 import *

def test_passcode_1_1():
    assert passcode_1("111111-111111") == 1

def test_passcode_1_2():
    assert passcode_1("223450-223450") == 0
    
def test_passcode_1_3():
    assert passcode_1("123789-123789") == 0

def test_passcode_2_1():
    assert passcode_2("112233-112233") == 1

def test_passcode_1_2():
    assert passcode_2("123444-123444") == 0
    
def test_passcode_1_3():
    assert passcode_2("111122-111122") == 1