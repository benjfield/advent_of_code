import re
original = { 
    1: {"c", "f"},
    7: {"a", "c", "f"},
    4: {"b", "c", "d", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
    0: {"a", "b", "c", "e", "f", "g"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
}
from advent.runner import register
@register(8, 2021, 1)
def segment_display_1(text):
    output_counts = 0
    for line in text.split("\n"):
        line_by_bar = line.split("|")

        codes = []

        for code in re.findall(r"(\w+)", line_by_bar[0]):
            code_list = list(code)
            code_list.sort()
            codes.append(tuple(code_list))

        codes.sort(key=lambda code: len(code))

        values = {
            codes[0]: 1,
            codes[1]: 7,
            codes[2]: 4,
            codes[9]: 8
        }

        value_5 = None

        for possible_value in codes[3:6]:
            difference_from_7 = set(possible_value).difference(set(codes[1]))
            if len(difference_from_7) == 2:
                values[possible_value] = 3
            else:
                difference_from_4 = set(possible_value).difference(set(codes[2]))
                if len(difference_from_4) == 2:
                    values[possible_value] = 5
                    value_5 = set(possible_value)
                else:
                    values[possible_value] = 2

        for possible_value in codes[6:9]:
            difference_from_5 = set(possible_value).difference(value_5)
            if len(difference_from_5) == 2:
                values[possible_value] = 0
            else:
                difference_from_1 = set(possible_value).difference(set(codes[0]))
                if len(difference_from_1) == 4:
                    values[possible_value] = 9
                else:
                    values[possible_value] = 6

        for code in re.findall(r"(\w+)", line_by_bar[1]):
            code_list = list(code)
            code_list.sort()
            if values[tuple(code_list)] in [1, 4, 7, 8]:
                output_counts += 1
            
    return output_counts

@register(8, 2021, 2)
def segment_display_2(text):
    output_total = 0
    for line in text.split("\n"):
        line_by_bar = line.split("|")

        codes = []

        for code in re.findall(r"(\w+)", line_by_bar[0]):
            code_list = list(code)
            code_list.sort()
            codes.append(tuple(code_list))

        codes.sort(key=lambda code: len(code))

        values = {
            codes[0]: 1,
            codes[1]: 7,
            codes[2]: 4,
            codes[9]: 8
        }

        value_5 = None

        for possible_value in codes[3:6]:
            difference_from_7 = set(possible_value).difference(set(codes[1]))
            if len(difference_from_7) == 2:
                values[possible_value] = 3
            else:
                difference_from_4 = set(possible_value).difference(set(codes[2]))
                if len(difference_from_4) == 2:
                    values[possible_value] = 5
                    value_5 = set(possible_value)
                else:
                    values[possible_value] = 2

        for possible_value in codes[6:9]:
            difference_from_5 = set(possible_value).difference(value_5)
            if len(difference_from_5) == 2:
                values[possible_value] = 0
            else:
                difference_from_1 = set(possible_value).difference(set(codes[0]))
                if len(difference_from_1) == 4:
                    values[possible_value] = 9
                else:
                    values[possible_value] = 6

        output_string = ""

        for code in re.findall(r"(\w+)", line_by_bar[1]):
            code_list = list(code)
            code_list.sort()
            output_string += str(values[tuple(code_list)])
        output_total += int(output_string)
            
    return output_total