from advent.year_2021.day_24 import *

def test_monad_1_1():
    text = '''inp z
inp x
mul z 3
eql z x'''
    data = process_rules(text)
    assert str(data["z"]) == "int(3 * model_number[0] == model_number[1])"

def test_monad_1_2():
    text = '''inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2'''
    data = process_rules(text)
    assert str(data["w"]) == "(int(int(int(model_number[0] / 2) / 2) / 2)) % 2"
    assert str(data["x"]) == "(int(int(model_number[0] / 2) / 2)) % 2"
    assert str(data["y"]) == "(int(model_number[0] / 2)) % 2"
    assert str(data["z"]) == "(model_number[0]) % 2"