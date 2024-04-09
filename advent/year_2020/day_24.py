from advent.runner import register

def get_initial_black_tiles(split_text): 
    two_length_moves = {
        "se": (1, -1),
        "sw": (-1, -1),
        "nw": (-1, 1),
        "ne": (1, 1),
    }
    
    one_length_moves = {
        "e": (2, 0),
        "w": (-2, 0),
    }

    coords = set()

    for line in split_text:
        text = line
        x = 0
        y = 0
        while len(text) > 0:
            if len(text) >= 2 and text[:2] in two_length_moves:
                x_change, y_change = two_length_moves[text[:2]]
                text = text[2:]
                x += x_change
                y += y_change
            elif len(text) >= 1:
                x_change, y_change = one_length_moves[text[:1]]
                text = text[1:]
                x += x_change
                y += y_change
            else:
                raise NotImplementedError
        this_coord = (x, y)
        if this_coord in coords:
            coords.remove(this_coord)
        else:
            coords.add(this_coord)
    return coords

@register(24, 2020, 1, True)
def lobby_layout_1(split_text):
    return len(get_initial_black_tiles(split_text))


@register(24, 2020, 2, True)
def lobby_layout_2(split_text): 
    black_tiles = get_initial_black_tiles(split_text)
    neighbours = [  
        (1, 1),  
        (1, -1),
        (-1, 1),
        (-1, -1),
        (2, 0),
        (-2, 0)
    ]
    
    for i in range(100):
        neighbour_count = {}

        for black_tile_coord in black_tiles:
            for x_change, y_change in neighbours:
                coord = (black_tile_coord[0] + x_change, black_tile_coord[1] + y_change)

                neighbour_count[coord] = neighbour_count.get(coord, 0) + 1
            
            neighbour_count[black_tile_coord] = neighbour_count.get(black_tile_coord, 0)        
        
        new_black_tiles = set()

        for neighbour_coord, count in neighbour_count.items():
            if neighbour_coord in black_tiles:
                if count == 1 or count == 2: 
                    new_black_tiles.add(neighbour_coord)
            else:
                if count == 2:
                    new_black_tiles.add(neighbour_coord)

        black_tiles = new_black_tiles

    return len(black_tiles)