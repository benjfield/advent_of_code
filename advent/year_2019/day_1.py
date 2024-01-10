from advent.runner import register
def mass_calculate(number):
    return int(number/3) - 2

def mass_recursive(number):
    added_mass = mass_calculate(number)

    if added_mass > 0:
        return mass_recursive(added_mass) + added_mass
    else: 
        return 0

@register(1, 2019, 1)
def mass_1(text):
    text_by_line = text.split("\n")

    total_mass = 0

    for line in text_by_line:
        total_mass += mass_calculate(int(line))

    return total_mass

@register(1, 2019, 2)
def mass_2(text):
    text_by_line = text.split("\n")

    total_mass = 0

    for line in text_by_line:
        total_mass += mass_recursive(int(line))

    return total_mass