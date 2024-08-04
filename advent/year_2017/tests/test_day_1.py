from advent.year_2017.day_1 import *

def test_inverse_captcha_1_1():
    assert inverse_captcha_1(["1122"]) == 3
    
def test_inverse_captcha_1_2():
    assert inverse_captcha_1(["1111"]) == 4
    
def test_inverse_captcha_1_3():
    assert inverse_captcha_1(["1234"]) == 0

def test_inverse_captcha_1_4():
    assert inverse_captcha_1(["91212129"]) == 9
    
def test_inverse_captcha_2_1():
    assert inverse_captcha_2(["1212"]) == 6