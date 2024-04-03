from advent.runner import register

@register(15, 2020, 1, True)
def rambunctious_recitation_1(split_text):
    input = [int(x) for x in split_text[0].split(",")]
    prior_numbers = {}

    for i in range(2020):
        if i < len(input):
            prior_numbers[input[i]] = i

            next_number = 0
        else:
            number = next_number
            if number in prior_numbers:
                next_number = i - prior_numbers[number]
            else:
                next_number = 0
            prior_numbers[number] = i

    return number

@register(15, 2020, 2, True)
def rambunctious_recitation_2(split_text):
    input = [int(x) for x in split_text[0].split(",")]
    prior_numbers = {}

    for i in range(30000000):
        if i < len(input):
            prior_numbers[input[i]] = i

            next_number = 0
        else:
            number = next_number
            if number in prior_numbers:
                next_number = i - prior_numbers[number]
            else:
                next_number = 0
            prior_numbers[number] = i

    return number