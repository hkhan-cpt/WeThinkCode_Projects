from world import obstacles


# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# Defining obstacle global
blocked = False


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps, robot_name):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, blocked
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_path_blocked(position_x,position_y, new_x, new_y):
        print(robot_name+ ": Sorry, there is an obstacle in the way.")
        blocked = True
        return True

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def list_obstacles(block_list):
    """Receives block_list from get_obstacles() in the obstacles package and displays a message indicating
    where the obstacles are located. 

    Args:
        block_list (list): List of co-ordinates.
    """

    if len(block_list) > 0:
        print("There are some obstacles:")
        for i in block_list:
            print(f"- At position {i[0]},{i[1]} (to {i[0]+4},{i[1]+4})")