from advent.year_2020.day_9 import *

text = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.split("\n")

def test_encoding_error_1():
    assert encoding_error_1(text, 5) == 127
    
def test_encoding_error_2():
    assert encoding_error_2(text, 5) == 62