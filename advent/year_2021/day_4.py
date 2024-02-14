from advent.runner import register
import re

def build_boards(text):
    text_by_line = text.split("\n")

    numbers_strings = text_by_line[0].split(",")

    numbers = [ int(x) for x in numbers_strings ]

    bingo_cards = []
    start_index = 0

    for i, line in enumerate(text_by_line[1:]):
        if len(line) == 0:
            bingo_cards.append({
                "rows": [0, 0, 0, 0, 0],
                "columns": [0, 0, 0, 0, 0],
                "numbers": {}
            })
            start_index = i + 1
        else:
            for j, number in enumerate(re.findall(r"\d+", line)):
                bingo_cards[-1]["numbers"][int(number)] = {
                    "row": i - start_index,
                    "column": j,
                    "marked": False
                }

    return numbers, bingo_cards

@register(4, 2021, 1)
def bingo_1(text):
    numbers, bingo_cards = build_boards(text)

    for number in numbers:
        for card in bingo_cards:
            if number in card["numbers"].keys():
                card["rows"][card["numbers"][number]["row"]] += 1
                card["columns"][card["numbers"][number]["column"]] += 1
                card["numbers"][number]["marked"] = True

                if card["rows"][card["numbers"][number]["row"]] == 5 or card["columns"][card["numbers"][number]["column"]] == 5:
                    unmarked_sum = 0
                    for winning_number, winning_number_details in card["numbers"].items():
                        if not winning_number_details["marked"]:
                            unmarked_sum += winning_number       
                    return unmarked_sum * number 
                
@register(4, 2021, 2)
def bingo_2(text):
    numbers, bingo_cards = build_boards(text)

    for card in bingo_cards:
        card["winning"] = False

    winning_cards = 0

    for number in numbers:
        for card in bingo_cards:
            if not card["winning"] and number in card["numbers"].keys():
                card["rows"][card["numbers"][number]["row"]] += 1
                card["columns"][card["numbers"][number]["column"]] += 1
                card["numbers"][number]["marked"] = True

                if card["rows"][card["numbers"][number]["row"]] == 5 or card["columns"][card["numbers"][number]["column"]] == 5:
                    card["winning"] = True
                    winning_cards += 1
                    if winning_cards == len(bingo_cards):
                        unmarked_sum = 0
                        for winning_number, winning_number_details in card["numbers"].items():
                            if not winning_number_details["marked"]:
                                unmarked_sum += winning_number       
                        return unmarked_sum * number 