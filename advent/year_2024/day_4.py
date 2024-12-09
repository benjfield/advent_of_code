from advent.runner import register

@register(4, 2024, 1, True)
def wordsearch_1(text):
    grid = []
    for line in text:
        grid.append([])
        for char in line:
            grid[-1].append(char)

    count = 0 
    for y in range(len(grid)):
        for x in range(len(line)):
            if grid[y][x] == "X":
                for y_change in [-1, 0, 1]:
                    for x_change in [-1, 0, 1]:
                        if not(x_change == 0 and y_change == 0):
                            new_x = x
                            new_y = y
                            found_word = True
                            for letter in ["M", "A", "S"]:
                                new_x = new_x + x_change
                                new_y = new_y + y_change
                                if not(new_x >= 0 and new_x < len(line) and new_y >= 0 and new_y < len(grid)):
                                    found_word = False
                                    break
                                elif grid[new_y][new_x] != letter:
                                    found_word = False
                                    break
                            if found_word:
                                count += 1
    return count

@register(4, 2024, 2, True)
def wordsearch_2(text):
    grid = []
    for line in text:
        grid.append([])
        for char in line:
            grid[-1].append(char)

    count = 0 
    for y in range(1,len(grid) - 1):
        for x in range(1,len(grid) - 1):
            if grid[y][x] == "A":
                found_xmas = True
                for x_change_1, y_change_1, x_change_2, y_change_2 in [
                    (-1, -1, 1, 1),
                    (-1, 1, 1, -1)
                ]:
                    char_1 = grid[y + y_change_1][x + x_change_1]
                    char_2 = grid[y + y_change_2][x + x_change_2]

                    if {char_1, char_2} != {"M", "S"}:
                        found_xmas = False
                        break
                    
                if found_xmas:
                    count += 1
    return count