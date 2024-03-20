from advent.runner import register
@register(1, 2020, 1, True)
def expenses_report_1(split_text):
    numbers = [int(x) for x in split_text]
    for i, number in enumerate(numbers):
        for number_2 in numbers[i+1:]:
            if number + number_2 == 2020:
                return number * number_2
            
@register(1, 2020, 2, True)
def expenses_report_2(split_text):
    numbers = [int(x) for x in split_text]
    for i, number in enumerate(numbers):
        for j, number_2 in enumerate(numbers[i+1:]):
            for number_3 in numbers[j+1:]:
                if number + number_2 + number_3 == 2020:
                    return number * number_2 * number_3