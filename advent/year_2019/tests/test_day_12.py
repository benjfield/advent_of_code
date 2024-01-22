from advent.year_2019.day_12 import *

def test_moons_1_1():
    text='''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

    assert moons_1(text, 10) == 179

def test_moons_1_2():
    text='''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''

    assert moons_1(text, 100) == 1940
    
def test_moons_2():
    text='''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''

    assert moons_2(text) == 4686774924