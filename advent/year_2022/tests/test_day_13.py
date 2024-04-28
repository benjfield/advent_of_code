from advent.year_2022.day_13 import *

text = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''.split("\n")

def test_distress_signal_1():
    assert distress_signal_1(text) == 13
    
def test_distress_signal_2():
    assert distress_signal_2(text) == 140