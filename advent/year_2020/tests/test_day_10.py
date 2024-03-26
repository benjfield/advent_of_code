from advent.year_2020.day_10 import *

def test_adapter_array_1_1():
    text = '''16
10
15
5
1
11
7
19
6
12
4'''.split("\n")
    
    assert adapter_array_1(text) == 35
    
def test_adapter_array_1_2():
    text = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split("\n")
    
    assert adapter_array_1(text) == 220
    
def test_adapter_array_2_1():
    text = '''16
10
15
5
1
11
7
19
6
12
4'''.split("\n")
    
    assert adapter_array_2(text) == 8
        
def test_adapter_array_2_2():
    text = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split("\n")
    
    assert adapter_array_2(text) == 19208