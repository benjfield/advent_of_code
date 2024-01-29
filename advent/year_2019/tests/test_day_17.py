from advent.year_2019.day_17 import *

def test_possible_stripped_journeys():
    initial = ["R",4,"R",4,"R",8,"L",6,"L",2,"R",4,"R",4,"R",8,"R",8,"R",8,"L",6,"L",2]

    results = possible_stripped_journeys(
        "A",
        ["R",8,"R",8],
        initial
    )

    assert results == [
            ["R",4,"R",4,"R",8,"L",6,"L",2,"R",4,"R",4,"R",8,"R",8,"R",8,"L",6,"L",2],
            ["R",4,"R",4,"R",8,"L",6,"L",2,"R",4,"R",4,"A","R",8,"L",6,"L",2],
            ["R",4,"R",4,"R",8,"L",6,"L",2,"R",4,"R",4,"R",8,"A","L",6,"L",2],
        ]
    
def test_replace_all():
    initial = ["B","L",6,"L",2,"B","A","L",6,"L",2]

    results = replace_all(
        "C",
        ["A", "B"],
        ["L",6,"L",2],
        initial
    )

    assert results == ["B","C","B","A","C"]

def test_replace_all_fail_1():
    initial = [6, 'L', 2, 'R', 4, 'R', 4, 'R', 8, 'R', 8, 'R', 8, 'L', 6, 'L', 2]

    results = replace_all(
        "C",
        ["A", "B"],
        ['R', 8, 'L', 6, 'L', 2],
        initial
    )

    assert results == None

def test_compress_journey():
    initial = ["R",8,"R",8,"R",4,"R",4,"R",8,"L",6,"L",2,"R",4,"R",4,"R",8,"R",8,"R",8,"L",6,"L",2]

    results = compress_journey(
        initial
    )

    print(results)

    expected_results = {
        "Journey": ['A', 'B', 'B', 'C', 'B', 'B', 'A', 'C'],
        "A": ["R",8,"R",8],
        "B": ["R",4],
        "C": ["R",8, "L", 6, "L", 2]
    }

    assert results == expected_results

def test_compress_journey_2():
    initial = ['L', 6, 'L', 4, 'R', 12, 'L', 6, 'R', 12, 'R', 12, 'L', 8, 'L', 6, 'L', 4, 'R', 12, 'L', 6, 'L', 10, 'L', 10, 'L', 6, 'L', 6, 'R', 12, 'R', 12, 'L', 8, 'L', 6, 'L', 4, 'R', 12, 'L', 6, 'L', 10, 'L', 10, 'L', 6, 'L', 6, 'R', 12, 'R', 12, 'L', 8, 'L', 6, 'L', 4, 'R', 12, 'L', 6, 'L', 10, 'L', 10, 'L', 6] 

    results = compress_journey(
        initial
    )

    expected_results = {
        "Journey": ['A', 'B','A', 'C', 'B','A', 'C', 'B','A', 'C',] ,
        "A": ['L', 6, 'L', 4, 'R', 12],
        "B": ['L', 6, 'R', 12, 'R', 12, 'L', 8],
        "C": ['L', 6, 'L', 10, 'L', 10, 'L', 6]
    }

    assert results == expected_results