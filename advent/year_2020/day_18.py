from advent.runner import register

def split_formula(line):
    formula = []
    for value in line.split(" "):
        append_list = []
        while value[0] == "(":
            formula.append("(")
            value = value[1:]
        
        while value[-1] == ")":
            append_list.append(")")
            value = value[:-1]
        
        if value != "+" and value != "*":
            formula.append(int(value))
        else:
            formula.append(value)
        formula += append_list
    return formula

def recursive_process(formula):
    i = 0
    while i < len(formula):
        if formula[i] == "(":
            j = i + 1
            current_level = 0
            while j < len(formula):
                if formula[j] == "(":
                    current_level += 1
                elif formula[j] == ")":
                    if current_level == 0:
                        formula = formula[:i] + [recursive_process(formula[i + 1:j])] + formula[j + 1:]
                        break
                    else:
                        current_level -= 1
                j += 1
        i+= 1

    total = formula[0]
    for i in range(1, len(formula) - 1, 2):
        if formula[i] == "+":
            total += formula[i + 1]
        else:
            total *= formula[i + 1]
            
    return total

@register(18, 2020, 1, True)
def operation_order_1(split_text):
    total = 0
    for line in split_text:
        total += recursive_process(split_formula(line))

    return total

def recursive_process_addition_first(formula):
    i = 0
    while i < len(formula):
        if formula[i] == "(":
            j = i + 1
            current_level = 0
            while j < len(formula):
                if formula[j] == "(":
                    current_level += 1
                elif formula[j] == ")":
                    if current_level == 0:
                        formula = formula[:i] + [recursive_process_addition_first(formula[i + 1:j])] + formula[j + 1:]
                        break
                    else:
                        current_level -= 1
                j += 1
        i+= 1

    i = 0
    while i < len(formula) - 2:
        if formula[i + 1] == "+":
            formula = formula[:i] + [formula[i] + formula[i + 2]] + formula[i + 3:]
        else:
            i += 2

    total = 1
    i = 0
    for i in range(0, len(formula), 2):
        total *= formula[i]
    return total

@register(18, 2020, 2, True)
def operation_order_2(split_text):
    total = 0
    for line in split_text:
        total += recursive_process_addition_first(split_formula(line))

    return total