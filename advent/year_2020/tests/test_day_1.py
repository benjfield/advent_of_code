from advent.year_2020.day_1 import *

text = '''1721
979
366
299
675
1456'''.split("\n")

def test_expenses_report_1():
    assert expenses_report_1(text) == 514579
    
def test_expenses_report_2():
    assert expenses_report_2(text) == 241861950