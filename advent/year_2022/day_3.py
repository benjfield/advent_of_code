from advent.runner import register

@register(3, 2022, 1, True)
def rucksack_reorganisation_1(split_text):
    bags = []

    for line in split_text:
        half_length = len(line) // 2

        first_compartment = set()
        for char in line[:half_length]:
            first_compartment.add(char)

        second_compartment = set()
        for char in line[half_length:]:
            second_compartment.add(char)

        bags.append((first_compartment, second_compartment))

    items = []
    for bag in bags:
        for item in bag[0].intersection(bag[1]):
            items.append(item)

    total_score = 0
    for item in items:
        if item.isupper():
            total_score += ord(item) - 38
        else:
            total_score += ord(item) - 96

    return total_score

@register(3, 2022, 2, True)
def rucksack_reorganisation_2(split_text):
    badges = []

    for i in range(0, len(split_text), 3):
        set_1 = set([x for x in split_text[i]])
        set_1 = set_1.intersection(set([x for x in split_text[i + 1]]))
        set_1 = set_1.intersection(set([x for x in split_text[i + 2]]))

        for item in set_1:
            badges.append(item)

    total_score = 0
    for item in badges:
        if item.isupper():
            total_score += ord(item) - 38
        else:
            total_score += ord(item) - 96

    return total_score