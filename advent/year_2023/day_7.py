import re
from advent.runner import register

card_map = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}


@register(7, 2023, 1)
def poker_1(text):
    hands = []

    for line in text.split("\n"):
        processed_line = re.match(r"(\w+) (\d+)", line)

        hand_value_basis = 13*5
        hand = processed_line.group(1)

        cards_in_hand = {}
        for card in hand:
            cards_in_hand[card] = cards_in_hand.get(card, 0) + 1

        most_cards = 0
        second_most_cards = 0
        for card_count in cards_in_hand.values():
            if card_count > most_cards:
                if most_cards > second_most_cards:
                    second_most_cards = most_cards
                most_cards = card_count
                
            elif card_count > second_most_cards:
                second_most_cards = card_count

        hand_value = 0

        if most_cards == 5:
            hand_value = 6
        elif most_cards == 4:
            hand_value = 5
        elif most_cards == 3 and second_most_cards == 2:
            hand_value = 4
        elif most_cards == 3:
            hand_value = 3
        elif most_cards == 2 and second_most_cards == 2:
            hand_value = 2
        elif most_cards == 2:
            hand_value = 1
        else:
            hand_value = 0

        hand_value = hand_value * (13 ** 5)

        for i, card in enumerate(reversed(hand)):
            hand_value += card_map[card] * (13 ** i)

        hands.append({
            "value": hand_value,
            "bid": int(processed_line.group(2))
        })

        
    def sortByValue(card):
        return card["value"]
    
    hands.sort(key=sortByValue)

    total_bid_value = 0
    for i, hand in enumerate(hands):
        total_bid_value += (i + 1) * hand["bid"]

    return total_bid_value    

card_map_2 = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}

@register(7, 2023, 2)
def poker_2(text):
    hands = []

    for line in text.split("\n"):
        processed_line = re.match(r"(\w+) (\d+)", line)

        hand_value_basis = 13*5
        hand = processed_line.group(1)

        cards_in_hand = {}
        joker_count = 0
        for card in hand:
            if card == "J":
                joker_count += 1
            else:
                cards_in_hand[card] = cards_in_hand.get(card, 0) + 1

        most_cards = 0
        second_most_cards = 0
        for card_count in cards_in_hand.values():
            if card_count > most_cards:
                if most_cards > second_most_cards:
                    second_most_cards = most_cards
                most_cards = card_count
                
            elif card_count > second_most_cards:
                second_most_cards = card_count

        most_cards = most_cards + joker_count

        hand_value = 0

        if most_cards == 5:
            hand_value = 6
        elif most_cards == 4:
            hand_value = 5
        elif most_cards == 3 and second_most_cards == 2:
            hand_value = 4
        elif most_cards == 3:
            hand_value = 3
        elif most_cards == 2 and second_most_cards == 2:
            hand_value = 2
        elif most_cards == 2:
            hand_value = 1
        else:
            hand_value = 0

        hand_value = hand_value * (13 ** 5)

        for i, card in enumerate(reversed(hand)):
            hand_value += card_map_2[card] * (13 ** i)

        hands.append({
            "value": hand_value,
            "bid": int(processed_line.group(2))
        })

        
    def sortByValue(card):
        return card["value"]
    
    hands.sort(key=sortByValue)

    total_bid_value = 0
    for i, hand in enumerate(hands):
        total_bid_value += (i + 1) * hand["bid"]

    return total_bid_value    