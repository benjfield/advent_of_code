from advent.runner import register
from advent.year_2019.computer import computer_from_string

@register(13, 2019, 1)
def arcade_1(text):
    computer = computer_from_string(text)

    screen_output = {}

    output = computer.process_without_input()

    if not output[0]:
        raise Exception("Not finished")

    for i in range(0, len(output[1]), 3):
        screen_output[(output[1][i], output[1][i+1])] = output[1][i+2]

    block_count = 0

    for value in screen_output.values():
        if value == 2:
            block_count += 1

    return block_count

def get_game_state(output_data, game_data):
    block_count = game_data.get("block_count", 0)

    for i in range(0, len(output_data), 3):
        coordinate = (output_data[i], output_data[i+1])
        tile_id = output_data[i+2]
        
        if coordinate in game_data["state"]:
            if game_data["state"][coordinate] == 2:
                block_count -= 1
        
        game_data["state"][coordinate] = tile_id
    
        if tile_id == 2:
            block_count += 1
        elif tile_id == 4:
            game_data["ball_position"] = coordinate
        elif tile_id == 3:
            game_data["paddle_position"] = coordinate
        elif coordinate[0] == -1 and coordinate[1] == 0:
            game_data["score"] = tile_id

    game_data["block_count"] = block_count

    return game_data

def get_next_paddle_spot(game_data, ball_movement_right=True, ball_movement_down=True, paddle_height = 18):
    ball_position = game_data["ball_position"]
    while ball_position[1] != paddle_height:
        if ball_movement_right:
            next_x_position = ball_position[0] + 1
        else:
            next_x_position = ball_position[0] - 1

        if ball_movement_down:
            next_y_position = ball_position[1] + 1
        else:
            next_y_position = ball_position[1] - 1

        next_position = (next_x_position, next_y_position)
        
        tile_id = game_data["state"][next_position]

        vertical_tile_position = (ball_position[0], next_y_position)
        vertical_tile_id = game_data["state"][vertical_tile_position]

        horizontal_tile_position = (next_x_position, ball_position[1])
        horizontal_tile_id = game_data["state"][horizontal_tile_position]

        bounced = False
        if vertical_tile_id == 1 or vertical_tile_id == 2:
            ball_movement_down = not ball_movement_down
            bounced = True

        if horizontal_tile_id == 1 or horizontal_tile_id == 2:
            ball_movement_right = not ball_movement_right
            bounced = True

        if tile_id == 1 or tile_id == 2:
            ball_movement_down = not ball_movement_down
            ball_movement_right = not ball_movement_right
            bounced = True

        if not bounced:
            ball_position = next_position

    return ball_position[0], ball_movement_right, ball_movement_down


@register(13, 2019, 2)
def arcade_2(text):
    computer = computer_from_string(text)

    output = computer.process_without_input()

    game_data = get_game_state(output[1], {"state": {}})

    computer.reset()
    computer.state[0] = 2

    last_ball_x = 20
    while game_data["block_count"] > 0:     
        ball_position = game_data["ball_position"]

        if last_ball_x < ball_position[0]:
            moving_right = True
        else:
            moving_right = False

        if moving_right:
            if (ball_position[0] > game_data["paddle_position"][0]):
                input = [1]
            elif ball_position[0] < game_data["paddle_position"][0] - 1:
                input = [-1]
            else:
                input = [0]
        else:
            if (ball_position[0] < game_data["paddle_position"][0]):
                input = [-1]
            elif ball_position[0] > game_data["paddle_position"][0] + 1:
                input = [1]
            else:
                input = [0]

        output = computer.process(input)

        game_data = get_game_state(output[1], game_data)
        last_ball_x = ball_position[0]

    return game_data["score"]