from advent.runner import register
from collections import deque
from itertools import islice

class RecursiveGame:
    def __init__(
        self,
        deck_1,
        deck_2
    ):
        self.deck_1 = deck_1
        self.deck_2 = deck_2

        self.state_cache = set()

    def play_game(self):
        while len(self.deck_1) > 0 and len(self.deck_2) > 0:
            state = tuple([len(self.deck_1)] + list(self.deck_1) + list(self.deck_2))

            if state in self.state_cache:
                return True
            else:
                self.state_cache.add(state)

                front_of_deck_1 = self.deck_1.popleft()
                front_of_deck_2 = self.deck_2.popleft()
                if front_of_deck_1 <= len(self.deck_1) and front_of_deck_2 <= len(self.deck_2):
                    deck_1_winner = RecursiveGame(deque(islice(self.deck_1, front_of_deck_1)), deque(islice(self.deck_2, front_of_deck_2))).play_game()
                else:
                    if front_of_deck_1 > front_of_deck_2:
                        deck_1_winner = True
                    else:
                        deck_1_winner = False
                            
                if deck_1_winner:
                    self.deck_1.append(front_of_deck_1)
                    self.deck_1.append(front_of_deck_2)
                else:
                    self.deck_2.append(front_of_deck_2)
                    self.deck_2.append(front_of_deck_1)

        if len(self.deck_1) > 0:
            return True
        else:
            return False 

@register(22, 2020, 1, True)
def crab_combat_1(split_text):
    deck_1 = deque()
    deck_2 = deque()

    add_to_deck_1 = True
    for line in split_text:
        if len(line) == 0:
            add_to_deck_1 = False
        elif line[0] == "P":
            pass
        elif add_to_deck_1:
            deck_1.append(int(line))
        else:
            deck_2.append(int(line))
    
    while len(deck_1) > 0 and len(deck_2) > 0: 
        front_of_deck_1 = deck_1.popleft()
        front_of_deck_2 = deck_2.popleft()
        if front_of_deck_1 > front_of_deck_2:
            deck_1.append(front_of_deck_1)
            deck_1.append(front_of_deck_2)
        else:
            deck_2.append(front_of_deck_2)
            deck_2.append(front_of_deck_1)

    total = 0

    deck = deck_1 + deck_2

    for i, value in enumerate(reversed(deck)):
        total += (i + 1) * value

    return total

@register(22, 2020, 2, True)
def crab_combat_2(split_text):
    deck_1 = deque()
    deck_2 = deque()

    add_to_deck_1 = True
    for line in split_text:
        if len(line) == 0:
            add_to_deck_1 = False
        elif line[0] == "P":
            pass
        elif add_to_deck_1:
            deck_1.append(int(line))
        else:
            deck_2.append(int(line))

    base_game = RecursiveGame(
        deck_1,
        deck_2
    )

    deck_1_winner = base_game.play_game()
    
    total = 0

    if deck_1_winner:
        deck = base_game.deck_1
    else:
        deck = base_game.deck_2

    for i, value in enumerate(reversed(deck)):
        total += (i + 1) * value

    return total