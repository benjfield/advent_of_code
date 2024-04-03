from advent.utils.modulo import *

def test_chinese_remainder_theorem_1():
    test_data = {
        3: 2,
        5: 3,
        7: 2
    }

    assert chinese_remainder_theorem(test_data) == 23