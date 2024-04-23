from advent.runner import register

@register(8, 2022, 1, True)
def treetop_tree_house_1(split_text):
    trees = []

    for line in split_text:
        trees.append([])
        for char in line:
            trees[-1].append(int(char))
    
    visible_trees = set()

    for y in range(len(trees)):
        highest_tree = 0
        for x in range(len(trees[0])):
            if trees[y][x] > highest_tree or x == 0:
                visible_trees.add((x, y))
                highest_tree = trees[y][x]
                
        highest_tree = 0
        for x in range(len(trees[0]) - 1, -1, -1):
            if trees[y][x] > highest_tree or x == len(trees[0]) - 1:
                visible_trees.add((x, y))
                highest_tree = trees[y][x]

    for x in range(len(trees[0])):
        highest_tree = 0
        for y in range(len(trees)):
            if trees[y][x] > highest_tree or y == 0:
                visible_trees.add((x, y))
                highest_tree = trees[y][x]
                
        highest_tree = 0
        for y in range(len(trees) - 1, -1, -1):
            if trees[y][x] > highest_tree or y == len(trees) - 1:
                visible_trees.add((x, y))
                highest_tree = trees[y][x]

    return len(visible_trees)


@register(8, 2022, 2, True)
def treetop_tree_house_2(split_text):
    trees = []

    for line in split_text:
        trees.append([])
        for char in line:
            trees[-1].append(int(char))
    
    best_tree = 0
    for tree_y in range(len(trees)):
        for tree_x in range(len(trees[0])):
            tree_value = trees[tree_y][tree_x]

            x_left_distance = 0
            for x_change in range(1, tree_x + 1):
                x_left_distance = x_change
                if trees[tree_y][tree_x - x_change] >= tree_value:
                    break

            x_right_distance = 0
            for x_change in range(1, len(trees[0]) - tree_x):
                x_right_distance = x_change
                if trees[tree_y][tree_x + x_change] >= tree_value:
                    break
            
            y_up_distance = 0
            for y_change in range(1, tree_y + 1):
                y_up_distance = y_change
                if trees[tree_y - y_change][tree_x] >= tree_value:
                    break

            y_down_distance = 0
            for y_change in range(1, len(trees) - tree_y):
                y_down_distance = y_change
                if trees[tree_y + y_change][tree_x] >= tree_value:
                    break

            total = x_left_distance * x_right_distance * y_up_distance * y_down_distance

            if total > best_tree:
                best_tree = total

    return best_tree