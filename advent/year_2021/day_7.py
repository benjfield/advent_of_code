from advent.runner import register
@register(7, 2021, 1)
def crabs_1(text):
    positions = [ int(x) for x in text.split(",") ]

    max_position = max(positions)

    min_sum = max_position * len(positions)

    for possible_end in range(min(positions), max_position):
        sum = 0
        for number in positions:
            sum += abs(possible_end - number)
        if sum < min_sum:
            min_sum = sum
        else:
            return min_sum
    return min_sum 

@register(7, 2021, 2)
def crabs_2(text):
    positions = [ int(x) for x in text.split(",") ]

    max_position = max(positions)

    min_sum = int((max_position * (max_position + 1))/2) * len(positions)

    for possible_end in range(min(positions), max_position):
        sum = 0
        for number in positions:
            distance = abs(possible_end - number)
            sum += int((distance * (distance + 1))/2)
        if sum < min_sum:
            min_sum = sum
        else:
            return min_sum
    return min_sum 