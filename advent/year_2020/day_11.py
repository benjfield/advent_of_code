from advent.runner import register

class Chair:
    def __init__(
        self,
        coords
    ):
        self.coords = coords
        self.full = False
        self.next_full = False
        self.neighbours = []

    def populate_neighbours(self, chairs):
        for x in [self.coords[0] - 1, self.coords[0], self.coords[0] + 1]:
            for y in [self.coords[1] - 1, self.coords[1], self.coords[1] + 1]:
                coords = (x, y)
                if coords != self.coords and coords in chairs:
                    self.neighbours.append(chairs[coords])

                    
    def populate_neighbours_full_lines(self, chairs, max_x, max_y):
        for coord_move in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            coords = (self.coords[0] + coord_move[0], self.coords[1] + coord_move[1])

            while (coords[0] >= 0 and coords[0] < max_x and coords[1] >= 0 and coords[1] < max_y):
                if coords in chairs:
                    self.neighbours.append(chairs[coords])
                    break
                else:
                    coords =  (coords[0] + coord_move[0], coords[1] + coord_move[1])
    
    def check_neighbours(self):
        full_count = 0
        for neighbour in self.neighbours:
            if neighbour.full:
                full_count += 1
        
        if not self.full and full_count == 0:
            self.next_full = True
        
        elif self.full and full_count >= 4:
            self.next_full = False

        else:
            self.next_full = self.full
    
    def check_neighbours_full_lines(self):
        full_count = 0
        for neighbour in self.neighbours:
            if neighbour.full:
                full_count += 1
        
        if not self.full and full_count == 0:
            self.next_full = True
        
        elif self.full and full_count >= 5:
            self.next_full = False

        else:
            self.next_full = self.full

    def set_full_to_next(self):
        self.full = self.next_full
    
def create_chair_tuple(chair_list):
    return tuple([x.full for x in chair_list])

@register(11, 2020, 1, True)
def seating_system_1(split_text):
    chairs_dict = {}
    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            if char == "L":
                coords = (x, y)
                chairs_dict[coords] = Chair(coords)
            elif char == ".":
                pass
            else:
                raise Exception
            
    for chair in chairs_dict.values():
        chair.populate_neighbours(chairs_dict)

    chair_list = list(chairs_dict.values())

    state = create_chair_tuple(chair_list)

    while True:
        prior_state = state

        for chair in chair_list:
            chair.check_neighbours()
        
        for chair in chair_list:
            chair.set_full_to_next()

        state = create_chair_tuple(chair_list)

        if state == prior_state:
            return sum(state)


@register(11, 2020, 2, True)
def seating_system_2(split_text):
    chairs_dict = {}
    max_x = len(split_text[0])
    max_y = len(split_text)

    for y, line in enumerate(split_text):
        for x, char in enumerate(line):
            if char == "L":
                coords = (x, y)
                chairs_dict[coords] = Chair(coords)
            elif char == ".":
                pass
            else:
                raise Exception
            
    for chair in chairs_dict.values():
        chair.populate_neighbours_full_lines(chairs_dict, max_x, max_y)

    chair_list = list(chairs_dict.values())

    state = create_chair_tuple(chair_list)

    while True:
        prior_state = state

        for chair in chair_list:
            chair.check_neighbours_full_lines()
        
        for chair in chair_list:
            chair.set_full_to_next()

        state = create_chair_tuple(chair_list)

        if state == prior_state:
            return sum(state)