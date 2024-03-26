from advent.runner import register
from enum import Enum
import re

class BagContainsShinyGold(Enum):
    NO = 0
    MAYBE = 1
    YES = 2

class Bag:
    def __init__(
        self,
        name,
        contains_by_name,
        line
    ):
        self.name = name
        self.contains_by_name = contains_by_name
        self.contains = []
        self.contains_gold = BagContainsShinyGold.MAYBE
        self.line = line

        if self.name == "shiny gold":
            self.is_gold = True
        else:
            self.is_gold = False

    def populate_contains(
        self,
        all_bags
    ):
        for bag in self.contains_by_name:
            self.contains.append((bag[0], all_bags[bag[1]]))

    def process_contains_gold(
        self,
        called_directly
    ):
        if self.contains_gold == BagContainsShinyGold.YES or (self.is_gold and self.contains_gold == BagContainsShinyGold.NO):
            return True
        elif self.contains_gold == BagContainsShinyGold.NO:
            return False
        else:
            if self.is_gold and not called_directly:
                return True
            else:
                contains_gold = False 
                for bag in self.contains:
                    underlying_contains_gold = bag[1].process_contains_gold(False)
                    if underlying_contains_gold:
                        contains_gold = True
                        break
                if contains_gold:
                    self.contains_gold = BagContainsShinyGold.YES
                    return True
                else:
                    self.contains_gold = BagContainsShinyGold.NO
                    return False
    
    def get_contained_bags(
        self,
    ):
        if len(self.contains) == 0:
            return 1, True
        else:
            total = 0
            for bag in self.contains:
                contained_bags, bottom_level = bag[1].get_contained_bags()
                total += bag[0] * contained_bags
                if not bottom_level:
                    total += bag[0]
            return total, False

    def __str__(
        self
    ):
        return self.name

@register(7, 2020, 1, True)
def handy_haversacks_1(split_text):
    bags = {}
    for line in split_text:
        initial_match = re.match(r"(.+) bags contain (.*).", line)

        name = initial_match.group(1)
        contains = []
        for potential_bag in initial_match.group(2).split(","):
            contains_match = re.match(r".*(\d+) (.*) bag", potential_bag)
            if contains_match is not None:
                contains.append((int(contains_match.group(1)), contains_match.group(2)))

        bag = Bag(
            name,
            contains,
            line
        )

        bags[name] = bag

    for bag in bags.values():
        bag.populate_contains(bags)

    count = 0
    for bag in bags.values():
        bag.process_contains_gold(True)
        if bag.contains_gold == BagContainsShinyGold.YES:
            count += 1
    
    return count

@register(7, 2020, 2, True)
def handy_haversacks_2(split_text):
    bags = {}
    for line in split_text:
        initial_match = re.match(r"(.+) bags contain (.*).", line)

        name = initial_match.group(1)
        contains = []
        for potential_bag in initial_match.group(2).split(","):
            contains_match = re.match(r".*(\d+) (.*) bag", potential_bag)
            if contains_match is not None:
                contains.append((int(contains_match.group(1)), contains_match.group(2)))

        bag = Bag(
            name,
            contains,
            line
        )

        bags[name] = bag

    for bag in bags.values():
        bag.populate_contains(bags)

    
    return bags["shiny gold"].get_contained_bags()[0]