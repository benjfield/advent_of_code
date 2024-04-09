from advent.year_2020.day_21 import *

def test_allergen_assesment_1():
    text = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''.split("\n")
    
    assert allergen_assesment_1(text) == 5
    
def test_allergen_assesment_2():
    text = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''.split("\n")
    
    assert allergen_assesment_2(text) == "mxmxvkd,sqjhc,fvjkl"