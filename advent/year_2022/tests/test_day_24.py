from advent.year_2022.day_24 import *

text = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''.split("\n")

def test_blizzard_basin_1():
    assert blizzard_basin_1(text) == 18
    
def test_blizzard_basin_2():
    assert blizzard_basin_2(text) == 54