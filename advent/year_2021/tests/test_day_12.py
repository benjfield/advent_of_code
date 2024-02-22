from advent.year_2021.day_12 import *

def test_passage_1_1():
    text = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''
    assert passage_1(text) == 10
    
def test_passage_1_2():
    text = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''
    assert passage_1(text) == 19
        
def test_passage_1_3():
    text = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''
    assert passage_1(text) == 226
    
def test_passage_2_1():
    text = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''
    assert passage_2(text) == 36
        
def test_passage_2_2():
    text = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''
    assert passage_2(text) == 103
        
def test_passage_2_3():
    text = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''
    assert passage_2(text) == 3509