from advent.year_2019.day_6 import *

def test_orbits_1():
    test_text = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''

    assert orbits_1(test_text) == 42

def test_orbits_2():
    test_text = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''

    assert orbits_2(test_text) == 4