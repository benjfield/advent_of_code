from advent.runner import register

@register(2, 2022, 1, True)
def rock_paper_scissors_1(split_text):
    rps = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    score = 0
    for line in split_text:
        split = line.split(" ")
        first_result = rps[split[0]]
        second_result = rps[split[1]]

        result = (second_result - first_result) % 3

        score += second_result

        if result == 1:
            score += 6
        elif result == 0:
            score += 3

    return score

@register(2, 2022, 2, True)
def rock_paper_scissors_2(split_text):
    rps = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }

    score = 0
    for line in split_text:
        score += rps[line]

    return score