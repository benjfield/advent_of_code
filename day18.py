from aocd import get_data
import re
def dig_1(text):
    dig_instructions = []
    for digs in text.split("\n"):
        match = re.match(r"([R|D|L|U]) (\d+) .*", digs)
        dig_instructions.append({
            "direction": match.group(1),
            "distance": int(match.group(2))
        })

    total_dug = 0

    dig_pivots = {}    

    x = 0
    y = 0

    previous_x = 0

    for i, dig in enumerate(dig_instructions):
        if dig["direction"] == "U":
            pivots = dig_pivots.get(y, []) 
            if dig_instructions[i-2]["direction"] == "D":
                pivots.append({
                    "left": min(x, previous_x),
                    "right": max(x, previous_x),
                    "contain": False
                })
                dig_pivots[y] = pivots
            else:
                pivots.append({
                    "left": min(x, previous_x),
                    "right": max(x, previous_x),
                    "contain": True
                })
            
                dig_pivots[y] = pivots
            for i in range(1, dig["distance"]):
                pivots = dig_pivots.get(y - i, [])

                pivots.append({
                    "left": x,
                    "right": x,
                    "contain": True
                }) 
                dig_pivots[y-i] = pivots

            y -= dig["distance"]

        elif dig["direction"] == "D":
            pivots = dig_pivots.get(y, []) 
            if dig_instructions[i-2]["direction"] == "U":
                pivots.append({
                    "left": min(x, previous_x),
                    "right": max(x, previous_x),
                    "contain": False
                })
                dig_pivots[y] = pivots
            else:
                pivots.append({
                    "left": min(x, previous_x),
                    "right": max(x, previous_x),
                    "contain": True
                })
            
                dig_pivots[y] = pivots
            for i in range(1, dig["distance"]):
                pivots = dig_pivots.get(y + i, [])

                pivots.append({
                    "left": x,
                    "right": x,
                    "contain": True
                }) 
                dig_pivots[y+i] = pivots
            y += dig["distance"]
                
        elif dig["direction"] == "R":
            previous_x = x
            x += dig["distance"]
        else:
            previous_x = x
            x -= dig["distance"]

        total_dug += dig["distance"]

        inside_dig = 0

    for i, pivot_points in dig_pivots.items():


        def sort_by_left(map):
            return map["left"]
        
        pivot_points.sort(key=sort_by_left)

        inside=False
        for i in range(len(pivot_points) - 1):
            if inside == False and not pivot_points[i]["contain"]:
                pass
            elif inside == True and pivot_points[i]["contain"]:
                pass
            else:
                inside_dig += pivot_points[i+1]["left"] - pivot_points[i]["right"] - 1
                if pivot_points[i]["contain"]:
                    inside = not inside

    return total_dug + inside_dig
          
dig_text = get_data(day=18, year=2023)     
print(dig_1(dig_text))



        
