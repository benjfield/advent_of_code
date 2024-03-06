from advent.runner import register

pair_cache = {}

def produce_count(rules, max_depth, pair, depth):
    if depth == max_depth:
        return {
            pair[0]: 1
        }
    else:
        pair_key = (pair, depth)
        if pair_key in pair_cache:
            return pair_cache[pair_key]
        else:
            middle_letter = rules[pair]
            count_1 = produce_count(rules, max_depth, pair[0] + middle_letter, depth + 1)
            count_2 = produce_count(rules, max_depth, middle_letter + pair[1], depth + 1)

            count = count_1.copy()

            for key, value in count_2.items():
                count[key] = count.get(key, 0) + value
            
            pair_cache[pair_key] = count

            return count

def generate_rules_and_polymer(text):
    split_text = text.split("\n")

    rules = {}
    
    started_rules = False
    polymer = ""
    for line in split_text:
        if started_rules:
            rule_split = line.split(" -> ")
            rules[rule_split[0]] = rule_split[1]
        elif len(line) == 0:
            started_rules = True
        else:
            polymer = line
    
    return rules, polymer

@register(14, 2021, 1)
def polymerisation_1(text):
    pair_cache.clear()
    rules, polymer = generate_rules_and_polymer(text)

    count = {}

    for i in range(len(polymer) - 1):
        pair_count = produce_count(rules, 10, polymer[i:i+2], 0)

        for key, value in pair_count.items():
            count[key] = count.get(key, 0) + value

    count[polymer[-1]]= count.get(polymer[-1], 0) + 1
    highest_count = 0
    lowest_count = 10000000
    for value in count.values():
        if value > highest_count:
            highest_count = value
        elif value < lowest_count:
            lowest_count = value
    
    return highest_count - lowest_count

@register(14, 2021, 2)
def polymerisation_2(text):
    pair_cache.clear()
    rules, polymer = generate_rules_and_polymer(text)

    count = {}

    for i in range(len(polymer) - 1):
        pair_count = produce_count(rules, 40, polymer[i:i+2], 0)

        for key, value in pair_count.items():
            count[key] = count.get(key, 0) + value

    count[polymer[-1]]= count.get(polymer[-1], 0) + 1

    highest_count = 0
    lowest_count = 0
    for value in count.values():
        if value > highest_count:
            highest_count = value
        elif value < lowest_count or lowest_count == 0:
            lowest_count = value
    
    return highest_count - lowest_count