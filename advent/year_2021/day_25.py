from advent.runner import register

@register(25, 2021, 1)
def cucumber_1(text):
    split_text = text.split("\n")

    eastbound = set()
    southbound = set()

    max_y = len(split_text)
    max_x = len(split_text[0])

    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            if char == ">":
                eastbound.add((x, y))
            elif char == "v":
                southbound.add((x, y))

    i = 1
    while True:
        cucumbers_to_remove = []
        cucumbers_to_add = []
        for cucumber in eastbound:
            next_x = cucumber[0] + 1
            if next_x == max_x:
                next_position = (0, cucumber[1])
            else:
                next_position = (next_x, cucumber[1])

            if next_position not in eastbound and next_position not in southbound:
                cucumbers_to_remove.append(cucumber)
                cucumbers_to_add.append(next_position)
        
        for cucumber in cucumbers_to_remove:
            eastbound.remove(cucumber)
            
        for cucumber in cucumbers_to_add:
            eastbound.add(cucumber)

        changed = len(cucumbers_to_add)

        cucumbers_to_remove = []
        cucumbers_to_add = []
        for cucumber in southbound:
            next_y = cucumber[1] + 1
            if next_y == max_y:
                next_position = (cucumber[0], 0)
            else:
                next_position = (cucumber[0], next_y)

            if next_position not in eastbound and next_position not in southbound:
                cucumbers_to_remove.append(cucumber)
                cucumbers_to_add.append(next_position)
        
        for cucumber in cucumbers_to_remove:
            southbound.remove(cucumber)
            
        for cucumber in cucumbers_to_add:
            southbound.add(cucumber)

        changed += len(cucumbers_to_add)
        if changed == 0:
            return i
        else:
            i += 1