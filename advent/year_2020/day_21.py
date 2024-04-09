from advent.runner import register
import re

class Food:
    def __init__(
        self,
        ingredients,
        allergens
    ):
        self.ingredients = ingredients
        self.allergens = allergens


@register(21, 2020, 1, True)
def allergen_assesment_1(split_text):
    foods = []

    ingredients_count = {}
    all_allergens = {}

    for line in split_text:
        split_by_bracket = line.split("(")
        ingredients = set([x for x in split_by_bracket[0].split(" ") if len(x) > 0])
        matched_allergens = re.search(r"contains ([\w, ]+)\)" , split_by_bracket[1])
        allergens = set(matched_allergens.group(1).split(", "))

        foods.append(
            Food(
                ingredients,
                allergens,
            )
        )

        for ingredient in ingredients:
            ingredients_count[ingredient] = ingredients_count.get(ingredient, 0) + 1

        for allergen in allergens:
            all_allergens[allergen] = None

    for allergen in all_allergens.keys():
        all_allergens[allergen] = set(ingredients_count.keys())

    for allergen, allergen_ingredients in all_allergens.items():
        for food in foods:
            if allergen in food.allergens:
                allergen_ingredients &= food.ingredients

    all_possible_allergen_ingredients = set()

    for allergen_ingredients in all_allergens.values():
        all_possible_allergen_ingredients.update(allergen_ingredients)

    total_count = 0
    for ingredient, count in ingredients_count.items():
        if ingredient not in all_possible_allergen_ingredients:
            total_count += count
    
    return total_count

@register(21, 2020, 2, True)
def allergen_assesment_2(split_text):
    foods = []

    ingredients_count = {}
    all_allergens = {}

    for line in split_text:
        split_by_bracket = line.split("(")
        ingredients = set([x for x in split_by_bracket[0].split(" ") if len(x) > 0])
        matched_allergens = re.search(r"contains ([\w, ]+)\)" , split_by_bracket[1])
        allergens = set(matched_allergens.group(1).split(", "))

        foods.append(
            Food(
                ingredients,
                allergens,
            )
        )

        for ingredient in ingredients:
            ingredients_count[ingredient] = ingredients_count.get(ingredient, 0) + 1

        for allergen in allergens:
            all_allergens[allergen] = None

    for allergen in all_allergens.keys():
        all_allergens[allergen] = set(ingredients_count.keys())

    for allergen, allergen_ingredients in all_allergens.items():
        for food in foods:
            if allergen in food.allergens:
                allergen_ingredients &= food.ingredients

    finalised_allergens = {}

    allergen_list = list(all_allergens.keys())

    allergen_list.sort()

    while(len(finalised_allergens) < len(all_allergens)):
        for allergen, ingredients in all_allergens.items():
            if allergen not in finalised_allergens and len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                finalised_allergens[allergen] = ingredient
                for other_allergen, other_ingredients in all_allergens.items():
                    if other_allergen not in finalised_allergens and ingredient in other_ingredients:
                        other_ingredients.remove(ingredient)

    ingredients_list = [finalised_allergens[allergen] for allergen in allergen_list]
    
    return ",".join(ingredients_list)