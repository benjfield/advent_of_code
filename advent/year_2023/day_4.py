import re
from advent.runner import register
def get_card_wins(text):
    card_wins = []

    for line in text.split("\n"):
        split_by_colon = line.split(":")

        game_id = int(re.search(r"Card\s+(\d+)", split_by_colon[0]).group(1))

        split_by_pipe = split_by_colon[1].split("|")

        winning_numbers = {}

        for number in split_by_pipe[0].split():
            winning_numbers[number] = True
        
        wins = 0

        for number in split_by_pipe[1].split():
            if number in winning_numbers:
                wins += 1

        card_wins.append(wins)

    return card_wins

@register(4, 2023, 1)
def cards_1(text):
    card_wins = get_card_wins(text)

    total_points = 0
    for wins in card_wins:
        if wins > 0:
            total_points += 2 ** (wins - 1)

    return total_points

@register(4, 2023, 2)
def cards_2(text):
    card_wins = get_card_wins(text)

    number_of_cards = card_wins.copy()

    for i in range(-1, -1 * len(card_wins) - 1, -1):
        this_number_of_cards = 1

        for j in range(1, card_wins[i] + 1):
            this_number_of_cards += number_of_cards[i + (j) ]

        number_of_cards[i] = this_number_of_cards

    return sum(number_of_cards)