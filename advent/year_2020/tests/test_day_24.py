from advent.year_2020.day_24 import *

text = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.split("\n")

def test_lobby_layout_1():
    assert lobby_layout_1(text) == 10
    
def test_lobby_layout_2():
    assert lobby_layout_2(text) == 2208
        
def test_get_initial_black_tiles_1():
    assert get_initial_black_tiles(["nwwswee"]) == {(0, 0)}
    
def test_get_initial_black_tiles_2():
    assert get_initial_black_tiles(["esenee"]) == {(6, 0)}
    
def test_get_initial_black_tiles_2():
    assert get_initial_black_tiles(["esew"]) == {(1, -1)}

def test_get_initial_black_tiles_3():
    assert get_initial_black_tiles(["sesenwnenenewseeswwswswwnenewsewsw"]) == {(-4, -2)}