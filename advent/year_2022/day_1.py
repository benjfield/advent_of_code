from advent.runner import register

@register(1, 2022, 1, True)
def calorie_count_1(split_text):
    split_text.append("")
    current_elf = 0
    max_elf = 0
    for line in split_text:
        if len(line) == 0:
            if current_elf > max_elf:
                max_elf = current_elf
            current_elf = 0
        else:
            current_elf += int(line)

    return max_elf

@register(1, 2022, 2, True)
def calorie_count_2(split_text):
    split_text.append("")
    current_elf = 0
    max_3_elves = [0, 0, 0]
    for line in split_text:
        if len(line) == 0:
            max_3_elves.append(current_elf)
            max_3_elves.sort(reverse=True)
            max_3_elves = max_3_elves[:3]
            current_elf = 0
        else:
            current_elf += int(line)

    return sum(max_3_elves)