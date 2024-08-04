from advent.year_2017.day_4 import *

def test_passphrase_1_1():
    assert passphrase_1(["aa bb cc dd ee"]) == 1
    
def test_passphrase_1_2():
    assert passphrase_1(["aa bb cc dd aa"]) == 0