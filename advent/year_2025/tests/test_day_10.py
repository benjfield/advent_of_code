from advent.year_2025.day_11 import *

text = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''.split("\n")

def test_server_rack_1():
    assert server_rack_1(text) == 5

text_2 = '''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out'''.split("\n")

def test_server_rack_2():
    assert server_rack_2(text_2) == 2