from enum import Flag, auto

class Direction(Flag):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def rotate(self, clockwise = True):
        if clockwise:
            return self.rotate_with_rotation(Rotation.CLOCKWISE)
        else:
            return self.rotate_with_rotation(Rotation.ANTICLOCKWISE)

    def flip(self):
        return self.rotate_with_rotation(Rotation.REVERSE)
            
    def move_forward_x_and_y(self, x, y, moves=1):
        if self == Direction.UP:
            return x, y - moves
        elif self == Direction.RIGHT:
            return x + moves, y
        elif self == Direction.DOWN:
            return x, y + moves
        else:
            return x - moves, y
                    
    def move_forward(self, coords, moves=1):
        return self.move_forward_x_and_y(*coords, moves)
    
    def is_horizontal(self):
        if self == Direction.RIGHT or self == Direction.LEFT:
            return True
        return False
    
    def is_vertical(self):
        if self == Direction.UP or self == Direction.DOWN:
            return True
        return False

    def in_direction_total(self, direction_total):
        if self in direction_total:
            return True

    def add_to_direction_total(self, direction_total):
        return self | direction_total
    
    @classmethod
    def direction_from_arrow(cls, symbol):
        if symbol == ">":
            return cls.RIGHT
        elif symbol == "<":
            return cls.LEFT
        elif symbol == "v":
            return cls.DOWN
        elif symbol == "^":
            return cls.UP
            
    def arrow_from_direction(self):
        if self == Direction.RIGHT:
            return ">"
        elif self == Direction.LEFT:
            return "<"
        elif self == Direction.DOWN:
            return "v"
        elif self == Direction.UP:
            return "^"
            
    @classmethod
    def direction_from_letter(cls, letter):
        if letter == "R":
            return cls.RIGHT
        elif letter == "L":
            return cls.LEFT
        elif letter == "D":
            return cls.DOWN
        elif letter == "U":
            return cls.UP
        
    def rotate_with_rotation(self, rotation):
        if rotation == Rotation.CLOCKWISE:
            if self == Direction.UP:
                return Direction.RIGHT
            elif self == Direction.RIGHT:
                return Direction.DOWN
            elif self == Direction.DOWN:
                return Direction.LEFT
            else:
                return Direction.UP
        elif rotation == Rotation.ANTICLOCKWISE:
            if self == Direction.UP:
                return Direction.LEFT
            elif self == Direction.RIGHT:
                return Direction.UP
            elif self == Direction.DOWN:
                return Direction.RIGHT
            else:
                return Direction.DOWN
        elif rotation == Rotation.REVERSE:
            if self == Direction.UP:
                return Direction.DOWN
            elif self == Direction.RIGHT:
                return Direction.LEFT
            elif self == Direction.DOWN:
                return Direction.UP
            else:
                return Direction.RIGHT
        elif rotation == Rotation.FORWARD:
            return self
        else:
            raise Exception("Invalid rotation")

    def get_rotation(self, next_direction):
        for possible_rotation in Rotation:
            if self.rotate_with_rotation(possible_rotation) == next_direction:
                return possible_rotation

class Rotation(Flag):
    ANTICLOCKWISE = auto()
    FORWARD = auto()
    CLOCKWISE = auto()
    REVERSE = auto()

    def reverse(self):
        if self == Rotation.CLOCKWISE:
            return Rotation.ANTICLOCKWISE
        elif self == Rotation.FORWARD:
            return Rotation.REVERSE
        elif self == Rotation.ANTICLOCKWISE:
            return Rotation.CLOCKWISE
        else:
            return Rotation.FORWARD
        
    def get_letter(self):
        if self == Rotation.CLOCKWISE:
            return "R"
        elif self == Rotation.ANTICLOCKWISE:
            return "L"
        else:
            return ""
    
    @classmethod
    def from_letter(cls, letter):
        if letter == "R":
            return Rotation.CLOCKWISE
        elif letter == "L":
            return Rotation.ANTICLOCKWISE
        else:
            raise NotImplementedError