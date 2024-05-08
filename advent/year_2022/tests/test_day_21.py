from advent.year_2022.day_21 import *

text = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''.split("\n")

def test_monkey_math_1():
    assert monkey_math_1(text) == 152

def test_monkey_math_2():
    assert monkey_math_2(text) == 301