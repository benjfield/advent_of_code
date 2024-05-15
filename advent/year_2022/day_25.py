from advent.runner import register

def process_snafu_number(string):
    number = 0
    number_dict = {
        "=": -2,
        "-": -1,
        "0": 0,
        "1": 1,
        "2": 2
    }

    for i, char in enumerate(reversed(string)):
        number += (5 ** i) * number_dict[char]

    return number

def generate_snafu_number(number):
    biggest_index = 0
    while number > 3 * (5 ** biggest_index):
        biggest_index += 1

    char_dict = {
        -2: "=",
        -1: "-",
        0: "0",
        1: "1",
        2: "2"
    }

    string = ""

    remaining_number = number
    for i in range(0, biggest_index + 1):
        power_of_5 = (5 ** i)
        char_number = (remaining_number // power_of_5) % 5

        if char_number >= 3:
            char_number = -5 + char_number
        
        string = char_dict[char_number] + string
        remaining_number -= char_number * power_of_5

    return string

@register(25, 2022, 1, True)
def full_of_hot_air_1(split_text):
    total = 0

    for line in split_text:
        total += process_snafu_number(line)

    return generate_snafu_number(total)