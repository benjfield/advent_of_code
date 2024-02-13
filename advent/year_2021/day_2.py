from advent.runner import register
@register(2, 2021, 1)
def submarine_1(text):
    text_by_line = text.split("\n")

    depth = 0
    horizontal = 0

    for line in text_by_line:
        split_text = line.split(" ")

        number = int(split_text[1])

        match split_text[0]:
            case "forward":
                horizontal += number
            case "up":
                depth -= number
            case "down":
                depth += number

    return horizontal * depth

@register(2, 2021, 2)
def submarine_2(text):
    text_by_line = text.split("\n")

    depth = 0
    horizontal = 0
    aim = 0

    for line in text_by_line:
        split_text = line.split(" ")

        number = int(split_text[1])

        match split_text[0]:
            case "forward":
                horizontal += number
                depth += number * aim
            case "up":
                aim -= number
            case "down":
                aim += number

    return horizontal * depth