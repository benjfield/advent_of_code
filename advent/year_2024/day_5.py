from advent.runner import register
from functools import cmp_to_key

def invalid_lesser(rules, page, search_page):
    if page in rules:
        if search_page in rules[page]:
            return True
        else:
            for value in rules[page]:
                if invalid_lesser(rules, value, search_page):
                    return True
            return False
    else:
        return False

@register(5, 2024, 1, False)
def queue_1(text):
    text = text.split("\n\n")
    total = 0

    rules_lines = [(int(line.split("|")[0]), int(line.split("|")[1])) for line in text[0].split("\n")]

    for line in text[1].split("\n"):
        values = [int(x) for x in line.split(",")]

        valid_pages = set(values)

        rules = {}

        for greater, lesser in rules_lines:
            if greater in valid_pages and lesser in valid_pages:
                if greater not in rules:
                    rules[greater] = {lesser}
                else:
                    rules[greater].add(lesser)

        valid = True
        for i in range(1, len(values)):
            if invalid_lesser(rules, values[i], values[i -1]):
                valid = False
                break
        
        if valid:
            total += values[len(values)//2]

    return total

def compare(rules, val_1, val_2):
    if invalid_lesser(rules, val_1, val_2):
        return -1
    elif invalid_lesser(rules, val_2, val_1):
        return 1
    else:
        return 0

@register(5, 2024, 2, False)
def queue_2(text):    
    text = text.split("\n\n")
    total = 0

    rules_lines = [(int(line.split("|")[0]), int(line.split("|")[1])) for line in text[0].split("\n")]

    for line in text[1].split("\n"):
        values = [int(x) for x in line.split(",")]

        valid_pages = set(values)

        rules = {}

        for greater, lesser in rules_lines:
            if greater in valid_pages and lesser in valid_pages:
                if greater not in rules:
                    rules[greater] = {lesser}
                else:
                    rules[greater].add(lesser)

        valid = True
        for i in range(1, len(values)):
            if invalid_lesser(rules, values[i], values[i -1]):
                valid = False
                break
        
        if not valid:
            sorted_values = sorted(values, key=cmp_to_key(lambda item1, item2: compare(rules, item1, item2)))

            total += sorted_values[len(sorted_values)//2]

    return total