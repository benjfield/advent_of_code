from advent.runner import register
from advent.year_2019.computer import Computer, computer_from_string
from advent.utils.direction import Direction, Rotation
from advent.utils.path_finding import Node
import copy

@register(17, 2019, 1)
def ascii_1(text):
    computer = computer_from_string(text)

    finished, output = computer.process_without_input()

    scaffold = [[]]

    added = 0
    for ascii in output:
        if ascii == 10:
            if added > 0:
                scaffold.append([])
                added = 0
        else:
            scaffold[-1].append(chr(ascii))
            added += 1

    if added == 0:
        scaffold = scaffold[:-1]

    alignment = 0

    for y, row in enumerate(scaffold):
        for x, value in enumerate(row):
            if value == "#":
                if x > 0 and x < (len(row) - 1) and y > 0 and y < (len(scaffold) - 1):
                    if scaffold[y-1][x] == "#" and scaffold[y+1][x] == "#" and scaffold[y][x-1] == "#" and scaffold[y][x+1] == "#":
                        alignment += x*y

    return alignment

class NeighbourNode(Node):
    def __init__(self, 
                 x, 
                 y,
                 valid_directions):
        super().__init__(x, y)
        self.valid_directions = valid_directions
        self.neighbours = {}
        self.junction_paths = {}
        if len(valid_directions) != 2:
            self.junction = True
        else:
            self.junction = False

    def populate_neighbours(self, nodes):
        for direction in self.valid_directions:
            x, y = direction.move_forward(self.x, self.y)
            potential_neighbour = Node(x, y)
            if potential_neighbour in nodes:
                self.neighbours[direction] = nodes[potential_neighbour]
            else:
                raise Exception(f"{potential_neighbour} missing")

    def get_path_to_next_junction(self, starting_direction, starting_junction, incoming_direction, prior_journey):
        #print(f"start {starting_direction} current {incoming_direction}")
        if self.junction:
            direction_from = incoming_direction.flip()

            self.junction_paths[direction_from] = {
                "journey": reverse_journey(prior_journey),
                "destination": starting_junction,
                "final_direction": starting_direction.flip()
            }

            #print(f"{self} to {starting_junction} starts {direction_from} ends {starting_direction.flip()}")

            return prior_journey, incoming_direction, self
        else:
            direction_from = incoming_direction.flip()
            potential_next_directions = [ x for x in self.neighbours.keys() if x != direction_from]
            if len(potential_next_directions) != 1:
                raise Exception("This should probably be a junction - shouldnt happen")
            next_direction = potential_next_directions[0]
            rotation_used = incoming_direction.get_rotation(next_direction)
            if rotation_used != Rotation.FORWARD:
                prior_journey += [rotation_used, 1]
            else:
                prior_journey[-1] += 1
            return self.neighbours[next_direction].get_path_to_next_junction(starting_direction, starting_junction, next_direction, prior_journey)

    def get_not_visited_neighbours(self, visited_junctions):
        not_visited_neighours = []
        for direction in self.neighbours.keys():
            if f"{self} {direction}" not in visited_junctions.keys():
                not_visited_neighours.append(direction)
        return not_visited_neighours

    def get_path(self, junctions, incoming_direction, visited_junctions, prior_journey, i=0):
        direction_from = incoming_direction.flip()

        visited_junctions[f"{self} {direction_from}"] = True
        
        not_visited_neighours = self.get_not_visited_neighbours(visited_junctions)

        if len(not_visited_neighours) == 0:
            visited_all_paths = True
            for junction in junctions:
                if len(junction.get_not_visited_neighbours(visited_junctions)) != 0:
                    visited_all_paths = False
            if visited_all_paths:
                return [prior_journey]
            else:
                return []
        else:
            journeys = []

            for possible_direction in not_visited_neighours:
                this_journey = prior_journey.copy()
                this_rotation = incoming_direction.get_rotation(possible_direction)
                if this_rotation != Rotation.FORWARD:
                    this_journey += [this_rotation]
                if type(self.junction_paths[possible_direction]["journey"][0]) is int and type(this_journey[-1]) is int:
                    this_journey[-1] += self.junction_paths[possible_direction]["journey"][0]
                    this_journey += self.junction_paths[possible_direction]["journey"][1:]
                else:
                    this_journey += self.junction_paths[possible_direction]["journey"]
                this_visited_junctions = visited_junctions.copy()
                
                this_visited_junctions[f"{self} {possible_direction}"] = True
                #print(f"{possible_direction} to {self.junction_paths[possible_direction]['final_direction']}")
                completed_journey = self.junction_paths[possible_direction]["destination"].get_path(
                    junctions,
                    self.junction_paths[possible_direction]["final_direction"],
                    this_visited_junctions,
                    this_journey,
                    i
                )
                journeys += completed_journey
            
            return journeys
    
    def populate_junction_paths(self):
        for direction, neighbour in self.neighbours.items():
            journey, final_direction, destination = neighbour.get_path_to_next_junction(direction, self, direction, [1])

            self.junction_paths[direction] = {
                    "journey": journey,
                    "destination": destination,
                    "final_direction": final_direction
                }
            #print(f"{self} to {destination} starts {direction} ends {final_direction}")

def reverse_journey(journey):
    reverse_journey = []
    for value in reversed(journey):
        if type(value) is int:
            reverse_journey.append(value)
        else:
            reverse_journey.append(value.reverse())
    return reverse_journey

def possible_stripped_journeys(
        letter_to_replace,
        array_to_strip,
        journey_remainder):
    array_length = len(array_to_strip)

    if len(journey_remainder) < array_length:
        return [journey_remainder]
    else:
        possible_journeys = [journey_remainder]
        for potential_start in range(len(journey_remainder) - array_length + 1):
            if journey_remainder[potential_start:potential_start+array_length] == array_to_strip:
                remainder_journeys = possible_stripped_journeys(letter_to_replace, array_to_strip, journey_remainder[potential_start+array_length:])
                for remainder_journey in remainder_journeys:
                    possible_journeys.append(journey_remainder[:potential_start] + [letter_to_replace] + remainder_journey)

        return possible_journeys
    
def replace_all(
    letter_to_replace,
    letters_to_leave,
    array_to_strip,
    journey_remainder):
    array_length = len(array_to_strip)

    if len(journey_remainder) < array_length:
        for value in journey_remainder:
            if value not in letters_to_leave:
                return None 
        
        return journey_remainder
    else:
        for potential_start in range(len(journey_remainder) - array_length + 1):
            if journey_remainder[potential_start] in letters_to_leave:
                pass
            elif journey_remainder[potential_start:potential_start+array_length] == array_to_strip:
                remainder_journey = replace_all(letter_to_replace, letters_to_leave, array_to_strip, journey_remainder[potential_start+array_length:])
                if remainder_journey is None:
                    return None
                else:
                    return journey_remainder[:potential_start] + [letter_to_replace] + remainder_journey
            else:
                return None
    
def compress_journey(journey):
    #Gonna assume that a, b and c are not subsets of each other
    for a_length in range(2, min(12, len(journey) - 1), 2):
        a = journey[:a_length]
        possible_remainders = possible_stripped_journeys("A", a, journey[a_length:])
        #if a == ['L', 6, 'L', 4, 'R', 12]:
        #    print(f"a {a}")
        #    print(possible_remainders)
        for possible_remainder in possible_remainders:
            for b_length in range(2, min(12, len(possible_remainder)) - 1, 2):
                b = possible_remainder[:b_length]
                if b[-1] == "A":
                    break
                possible_remainders_b = possible_stripped_journeys("B", b, possible_remainder[b_length:])
                for possible_remainder_b in possible_remainders_b:
                    pre_found_journey = ["A", "B"]
                    letters_to_ignore = ["A", "B"]
                    for i, value in enumerate(possible_remainder_b): 
                        if value in letters_to_ignore:
                            pre_found_journey.append(value)
                        else:
                            possible_remainder_b = possible_remainder_b[i:]
                            break                  

                    for c_length in range(2, min(12, len(possible_remainder_b) - 1), 2):
                        if c_length == len(possible_remainder_b) - 1 or possible_remainder_b[c_length] in letters_to_ignore:
                            c = possible_remainder_b[:c_length]
                            possible_remainder_c = replace_all("C", letters_to_ignore, c, possible_remainder_b[c_length:])
                            if possible_remainder_c is not None:
                                return {
                                    "Journey": pre_found_journey + ["C"] + possible_remainder_c,
                                    "A": a,
                                    "B": b,
                                    "C": c
                                }
                            else:
                                break
    return None


def strip_from_journey(to_strip, journey_remainder):
    a_length = len(to_strip)
    stripped_journey = []
    potential_start = 0
    last_finish = 0
    while potential_start < len(journey_remainder) - a_length:
        if journey_remainder[potential_start:potential_start+a_length] == to_strip:
            remainder = journey_remainder[last_finish:potential_start]
            if len(remainder) > 0:
                stripped_journey.append(remainder)
            last_finish = potential_start + a_length
            potential_start += a_length
        else:
            potential_start += 1

    remainder = journey_remainder[last_finish:]
    if len(remainder) > 0:
        stripped_journey.append(remainder)
    return stripped_journey

def journey_array_to_strings(journey_array):
    string_array = []
    for journey in journey_array:
        string_array.append(journey_to_string(journey))
    return string_array

def journey_to_string(journey): 
    journey_copy = journey.copy()       
    for i, value in enumerate(journey_copy):
        if type(value) is Rotation:
            journey_copy[i] = value.get_letter()
    return journey_copy


def ascii_2(text):
    computer = computer_from_string(text)

    finished, output = computer.process_without_input()

    scaffold = [[]]

    added = 0
    for ascii in output:        
        if ascii == 10:
            if added > 0:
                scaffold.append([])
                added = 0
        else:
            scaffold[-1].append(chr(ascii))
            added += 1

    if added == 0:
        scaffold = scaffold[:-1]
    #scaffold = scaffold[:22]

    start = None
    starting_direction = None
    junctions = []
    nodes = {}
    for y, row in enumerate(scaffold):
        print("".join(row))
        for x, value in enumerate(row):
            if value != ".":
                valid_directions = []
                if x > 0 and scaffold[y][x-1] != ".":
                    valid_directions.append(Direction.LEFT)
                    
                if x < (len(row) - 1) and scaffold[y][x+1] != ".":
                    valid_directions.append(Direction.RIGHT)

                if y > 0 and scaffold[y-1][x] != ".":
                    valid_directions.append(Direction.UP)

                if y < (len(scaffold) - 1) and scaffold[y+1][x] != ".":
                    valid_directions.append(Direction.DOWN)
        
                node = NeighbourNode(x, y, valid_directions)
                nodes[node] = node
                if node.junction:
                    junctions.append(node)

                if value != "#":
                    starting_direction = Direction.direction_from_arrow(value)
                    start = node

    for node in nodes.values():
        node.populate_neighbours(nodes)

    for i, junction in enumerate(junctions):
        junction.populate_junction_paths()

    final_journeys = start.get_path(
        junctions,
        starting_direction.flip(),
        {},
        []
    )

    def sort_by_len(map):
        return len(map)

    final_journeys.sort(key=sort_by_len)

    for i, possible_journey in enumerate(final_journeys):
        journey_results = compress_journey(possible_journey)
        if journey_results is not None:
            break

    if journey_results is None:
        raise Exception("No compression found")
    
    return journey_results

@register(17, 2019, 2)
def ascii_2_hardcoded(text):
    #Splitting this out because the above takes quite a long time
    journey_details = {
        "Journey": ['A', 'B','A', 'C', 'B','A', 'C', 'B','A', 'C',] ,
        "A": ['L', 6, 'L', 4, 'R', 12],
        "B": ['L', 6, 'R', 12, 'R', 12, 'L', 8],
        "C": ['L', 6, 'L', 10, 'L', 10, 'L', 6]
    }
    

    journey_strings = {}
    for key, value in journey_details.items():
        for i, individual_value in enumerate(value):
            value[i] = str(individual_value)

        journey_strings[key] = ",".join(value)

    journey_ascii = {}
    for key, value in journey_strings.items():
        ascii_array = []
        for individual_value in value:
            ascii_array.append(ord(individual_value))
        ascii_array.append(10)
        journey_ascii[key] = ascii_array

    input = journey_ascii["Journey"] + journey_ascii["A"] + journey_ascii["B"] + journey_ascii["C"] + [ord("N"), 10]

    computer = Computer(text)

    computer.state[0] = 2
    finished, output = computer.process(input)

    line = []
    for ascii in output:  
        if ascii == 10:
            print("".join(line))
            line = []
        else:
            line.append(chr(ascii))
    return output[-1]