from advent.runner import register

@register(4, 2022, 1, True)
def camp_cleanup_1(split_text):
    count = 0
    for line in split_text:
        comma_split = line.split(",")

        split_1 = comma_split[0].split("-")

        min_1 = int(split_1[0])
        max_1 = int(split_1[1])

        split_2 = comma_split[1].split("-")

        min_2 = int(split_2[0])
        max_2 = int(split_2[1])

        if (min_1 <= min_2 and max_1 >= max_2) or (min_1 >= min_2 and max_1 <= max_2):
            count += 1

    return count

@register(4, 2022, 2, True)
def camp_cleanup_2(split_text):
    count = 0
    for line in split_text:
        comma_split = line.split(",")

        split_1 = comma_split[0].split("-")

        min_1 = int(split_1[0])
        max_1 = int(split_1[1])

        split_2 = comma_split[1].split("-")

        min_2 = int(split_2[0])
        max_2 = int(split_2[1])

        total_min = max(min_1, min_2)
        total_max = min(max_1, max_2)

        if total_max >= total_min:
            count += 1

    return count