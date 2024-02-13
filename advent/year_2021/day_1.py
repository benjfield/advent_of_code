from advent.runner import register
@register(1, 2021, 1)
def sonar_1(text):
    text_by_line = text.split("\n")

    old_value = int(text_by_line[0])

    increase_count = 0

    for value in text_by_line[1:]:
        if int(value) > old_value:
            increase_count += 1
        old_value = int(value)

    return increase_count

@register(1, 2021, 2)
def sonar_2(text):
    text_by_line = text.split("\n")

    values = [int(x) for x in text_by_line]

    old_value = sum(values[:3])

    increase_count = 0

    for index in range(1, len(values)-2):
        current_value = sum(values[index:index+3])
        if current_value > old_value:
            increase_count += 1
        old_value = current_value

    return increase_count