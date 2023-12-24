from aocd import get_data
import re
class Brick:
    def __init__(
        self,
        start_x,
        start_y,
        start_z,
        finish_x,
        finish_y,
        finish_z):
        self.start_x = min(start_x, finish_x) 
        self.start_y = min(start_y, finish_y) 
        self.start_z = min(start_z, finish_z)
        self.finish_x = max(start_x, finish_x) 
        self.finish_y = max(start_y, finish_y)
        self.finish_z = max(start_z, finish_z)

        self.supporting_bricks = []
        self.supported_by_bricks = []
    
    def __str__(self):
        return f"{self.start_x} {self.start_y} {self.start_z} {self.finish_x} {self.finish_y} {self.finish_z} "

    def drop_brick_to_ground(self):
        self.finish_z -= (self.start_z - 1)
        self.start_z = 1

    def drop_brick(self, supporting_brick):
        new_start_z = supporting_brick.finish_z + 1
        self.finish_z -= (self.start_z - new_start_z)
        self.start_z = new_start_z

        supporting_brick.supporting_bricks.append(self)
        self.supported_by_bricks.append(supporting_brick)    

def compare_bricks(brick_1, brick_2):
    return (
        (max(brick_1.start_x, brick_2.start_x) <= min(brick_1.finish_x, brick_2.finish_x))
        and (max(brick_1.start_y, brick_2.start_y) <= min(brick_1.finish_y, brick_2.finish_y)) 
        )

def sort_by_start_z(brick):
    return brick.start_z

def sort_by_finish_z(brick):
    return brick.finish_z

def create_and_drop_bricks(text):
    bricks_by_start_z = []
    bricks_by_finish_z = []
    ground = Brick(0, 0, 0, 0, 0, 0)

    for row in text.split("\n"):
        parsed_brick = re.match(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", row)

        brick = Brick(
            int(parsed_brick.group(1)),
            int(parsed_brick.group(2)),
            int(parsed_brick.group(3)),
            int(parsed_brick.group(4)),
            int(parsed_brick.group(5)),
            int(parsed_brick.group(6)),
        )

        bricks_by_start_z.append(brick)
        bricks_by_finish_z.append(brick)

    bricks_by_start_z.sort(key=sort_by_start_z)
    bricks_by_finish_z.sort(key=sort_by_finish_z)

    for brick_to_drop in bricks_by_start_z:
        #print(f"dropping {brick_to_drop}")
        brick_supporting_level = 0
        
        for j in range(bricks_by_finish_z.index(brick_to_drop)-1, -1, -1):
            if bricks_by_finish_z[j].finish_z < brick_supporting_level:
                break

            if compare_bricks(brick_to_drop, bricks_by_finish_z[j]):    
                #print(f"supporting {bricks_by_finish_z[j]}")
                brick_to_drop.drop_brick(bricks_by_finish_z[j])
                brick_supporting_level = bricks_by_finish_z[j].finish_z

        if brick_supporting_level == 0:
            brick_to_drop.drop_brick(ground)
        
        #technically we dont need a full sort here
        bricks_by_finish_z.sort(key=sort_by_finish_z)

    return bricks_by_finish_z

def brick_1(text):
    bricks = create_and_drop_bricks(text)

    bricks_to_disintegrate = 0
    for brick in bricks:
        #print(f"testing {brick}")
        can_disintegrate = True
        for supported_brick in brick.supporting_bricks:
            #print(f"supporting {supported_brick} with {len(supported_brick.supported_by_bricks)} supports")
            if len(supported_brick.supported_by_bricks) < 2:
                can_disintegrate = False
                break
        if can_disintegrate:
            bricks_to_disintegrate += 1
    
    return bricks_to_disintegrate

def brick_2(text):
    bricks = create_and_drop_bricks(text)

    bricks.sort(key=sort_by_start_z)


    total_fall_count = 0
    for i, brick in enumerate(bricks):
        remove_list = [brick]

        #Could shortcut this super heavily because it can be done by layers - if no brick removed in the layer before, it terminates.
        for brick_to_test in bricks[i+1:]:
            will_fall = True
            for supporting_brick in brick_to_test.supported_by_bricks:
                if supporting_brick not in remove_list:
                    will_fall = False
                    break
            if will_fall:
                remove_list.append(brick_to_test)
        
        total_fall_count += len(remove_list) - 1
    
    return total_fall_count

brick_text = get_data(day=22, year=2023)
#print(brick_2(brick_text))        

                
    