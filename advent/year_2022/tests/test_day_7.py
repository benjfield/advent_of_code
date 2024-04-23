from advent.year_2022.day_7 import *

text = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split("\n")

def test_no_space_left_1():
    assert no_space_left_1(text) == 95437

def test_no_space_left_1_1():
    assert no_space_left_1('''$ cd /
$ ls
dir a
$ cd a
$ ls
dir a
2 a.txt
$ cd a
$ ls
99999 a.txt'''.split("\n")) == 99999
    
def test_no_space_left_2():
    assert no_space_left_2(text) == 24933642
