from advent.runner import register

@register(13, 2021, 1)
def origami_1(text):
    split_text = text.split("\n")

    coords = set()
    rules = []

    folds = False
    for line in split_text:
        if folds:
            split_by_space = line.split(" ")
            rule_split = split_by_space[2].split("=")
            rules.append((rule_split[0], int(rule_split[1])))
        elif len(line) == 0:
            folds = True
        else:
            split_coords = line.split(",")
            coords.add((int(split_coords[0]), int(split_coords[1])))

    for rule in rules[:1]:
        new_coords = set()
        for coord in coords:
            if rule[0] == "x":
                index = 0
            else:
                index = 1

            if coord[index] > rule[1] * 2:
                pass
            else:
                if coord[index] < rule[1]:
                    new_coord = coord
                else:
                    if index == 0:
                        new_coord = (2 * rule[1] - coord[0], coord[1])
                    else:
                        new_coord = (coord[0], 2 * rule[1] - coord[1])
                new_coords.add(new_coord)
        coords = new_coords

    return len(coords)

@register(13, 2021, 2)
def origami_2(text):
    split_text = text.split("\n")

    coords = set()
    rules = []

    folds = False
    for line in split_text:
        if folds:
            split_by_space = line.split(" ")
            rule_split = split_by_space[2].split("=")
            rules.append((rule_split[0], int(rule_split[1])))
        elif len(line) == 0:
            folds = True
        else:
            split_coords = line.split(",")
            coords.add((int(split_coords[0]), int(split_coords[1])))

    x = 0
    y = 0

    for rule in rules:
        new_coords = set()
        for coord in coords:
            if rule[0] == "x":
                x = rule[1]
                index = 0
            else:
                y = rule[1]
                index = 1

            if coord[index] > rule[1] * 2:
                pass
            else:
                if coord[index] < rule[1]:
                    new_coord = coord
                else:
                    if index == 0:
                        new_coord = (2 * rule[1] - coord[0], coord[1])
                    else:
                        new_coord = (coord[0], 2 * rule[1] - coord[1])
                new_coords.add(new_coord)
        coords = new_coords
        
    for i in range(y):
        text = "" 
        for j in range(x):
            if (j, i) in coords:
                text += "."
            else:
                text += "#"
        print(text)

    return len(coords)