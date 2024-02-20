from advent.runner import register
@register(10, 2021, 1)
def syntax_1(text):
    total_incorrect = {
        ")": 0, 
        "]": 0, 
        "}": 0, 
        ">": 0, 
    }

    open_chunks = {
        "(": ")", 
        "[": "]", 
        "{": "}", 
        "<": ">"
    }

    for line in text.split("\n"):
        char_list = []
        for char in line:
            if char in open_chunks:
                char_list.append(open_chunks[char])
            else:
                if char_list[-1] == char:
                    char_list.pop()
                else:
                    total_incorrect[char] += 1
                    break

    return total_incorrect[")"] * 3 + total_incorrect["]"] * 57 + total_incorrect["}"] * 1197 + total_incorrect[">"] * 25137

@register(10, 2021, 2)
def syntax_2(text):
    points = {
        ")": 1, 
        "]": 2, 
        "}": 3, 
        ">": 4, 
    }

    open_chunks = {
        "(": ")", 
        "[": "]", 
        "{": "}", 
        "<": ">"
    }

    point_totals = []

    for line in text.split("\n"):
        char_list = []
        corrupt = False
        for char in line:
            if char in open_chunks:
                char_list.append(open_chunks[char])
            else:
                if char_list[-1] == char:
                    char_list.pop()
                else:
                    corrupt = True
                    break
        
        if not corrupt:
            point_total = 0
            for char in reversed(char_list):
                point_total = point_total * 5
                point_total += points[char]
            point_totals.append(point_total)

    point_totals.sort()

    half_index = int(len(point_totals)/2)

    return point_totals[half_index]