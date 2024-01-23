from advent.runner import register
import re
import math

def ingredient_depth(recipes, key):
    if key == "ORE":
        return 1
    elif "depth" in recipes[key]:
        return recipes[key]["depth"]
    depths = []
    for underlying_code in recipes[key]["ingredients"].keys():
        depths.append(ingredient_depth(recipes, underlying_code))

    this_depth = max(depths) + 1
    recipes[key]["depth"] = this_depth
    return this_depth        

def single_object_cost(recipes, ordered_ingredients, recipe_used):    
    ore_count, spares = object_cost_with_spares(recipes, ordered_ingredients, recipe_used, {})
                
    return ore_count

def object_cost_with_spares(recipes, ordered_ingredients, recipe_used, spare_materials):
    for deepest_ingredient in ordered_ingredients:
        if deepest_ingredient in recipe_used:
            spare_existing = spare_materials.get(deepest_ingredient, 0)

            items_needed = recipe_used[deepest_ingredient] - spare_existing

            number_to_produce = math.ceil(items_needed / recipes[deepest_ingredient]["number"])

            spare_added = recipes[deepest_ingredient]["number"] * number_to_produce - recipe_used[deepest_ingredient]
            
            if spare_existing + spare_added == 0:
                if deepest_ingredient in spare_materials:
                    del spare_materials[deepest_ingredient]
                else:
                    pass
            else:
                spare_materials[deepest_ingredient] = spare_existing + spare_added

            for underlying_code, underlying_number in recipes[deepest_ingredient]["ingredients"].items():
                recipe_used[underlying_code] = recipe_used.get(underlying_code, 0) + underlying_number * number_to_produce

            del recipe_used[deepest_ingredient]
                
    return recipe_used["ORE"], spare_materials

def prepare_recipes(text):
    split_text = text.split("\n")
    recipes = {}

    for line in split_text:
        details = {
            "ingredients": {}
        }

        split_by_arrow = line.split(" => ")

        for ingredient in re.findall(r"(\d+) (\w+)", split_by_arrow[0]):
            details["ingredients"][ingredient[1]] = int(ingredient[0])

        matched_text = re.search(r"(\d+) (\w+)", split_by_arrow[1])
        details["number"] = int(matched_text.group(1))

        recipes[matched_text.group(2)] = details
    
    ordered_ingredients_with_depth = []

    for key in recipes.keys():
        depth = ingredient_depth(recipes, key)
        ordered_ingredients_with_depth.append({
            "key": key,
            "depth": depth,
        })

    def sort_by_depth(map):
        return map["depth"]
    
    ordered_ingredients_with_depth.sort(key=sort_by_depth, reverse=True)

    ordered_ingredients = [ x["key"] for x in ordered_ingredients_with_depth]

    return recipes, ordered_ingredients

@register(14, 2019, 1)
def reaction_1(text):
    recipes, ordered_ingredients = prepare_recipes(text)

    recipe_used = recipes["FUEL"]["ingredients"]
    
    return single_object_cost(recipes, ordered_ingredients, recipe_used)

@register(14, 2019, 2)
def reaction_2(text):
    recipes, ordered_ingredients = prepare_recipes(text)

    recipe_used = recipes["FUEL"]["ingredients"].copy()
    
    original_ore_remaining = 1000000000000
    ore_remaining = original_ore_remaining
    fuel_made = 0

    spare_materials = {}

    used_all_spares_once = False

    while True:
        ore_to_use, spare_materials = object_cost_with_spares(recipes, ordered_ingredients, recipe_used, spare_materials)

        if ore_to_use > ore_remaining:
            return fuel_made
        else:
            fuel_made += 1
            ore_remaining -= ore_to_use
            recipe_used = recipes["FUEL"]["ingredients"].copy()
            if len(spare_materials) == 0 and not used_all_spares_once:
                ore_used = original_ore_remaining - ore_remaining
                multiplier = int(original_ore_remaining/ore_used) 
                fuel_made = multiplier * fuel_made
                ore_remaining = original_ore_remaining - multiplier * ore_used