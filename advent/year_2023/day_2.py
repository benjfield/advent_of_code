import re
from advent.runner import register

def parse_games(text):
    games = {}

    for line in text.split("\n"):
        split_by_colon = line.split(":")

        game_id = int(re.search("Game (\d+)", split_by_colon[0]).group(1))

        split_by_semi_colon = split_by_colon[1].split(";")

        red_max = 0
        green_max = 0
        blue_max = 0
        red_regex = "(\d+) red"
        blue_regex = "(\d+) blue"
        green_regex = "(\d+) green"

        for show in split_by_semi_colon:
            red_result = re.search(red_regex, show)
            if red_result:
                red_max = max(red_max, int(red_result.group(1))) 

            green_result = re.search(green_regex, show)
            if green_result:
                green_max = max(green_max, int(green_result.group(1)))
                
            blue_result = re.search(blue_regex, show)
            if blue_result:
                blue_max = max(blue_max, int(blue_result.group(1)))
        
        games[game_id] = {
            "red": red_max,
            "blue": blue_max,
            "green": green_max,
        }
    
    return games

@register(2, 2023, 1)
def cube_1(text, red, blue, green):
    games = parse_games(text)
    
    total_ids = 0
    for key, value in games.items():
        if value["red"] <= red and value["blue"] <= blue and value["green"] <=green:
            total_ids += key

    return total_ids

@register(2, 2023, 2)
def cube_2(text):
    games = parse_games(text)
    
    total_power = 0
    for key, value in games.items():
        total_power += value["red"] * value["blue"] * value["green"]

    return total_power
