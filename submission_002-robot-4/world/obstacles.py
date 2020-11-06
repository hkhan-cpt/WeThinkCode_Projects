import random

block_list = []

def get_obstacles():
    """Generates a list of random co-ordinates consisting of up to 10 pairs.

    Returns:
        [list]: List of co-ordinates.
    """

    global block_list
    for i in range(random.randint(0,10)):
        (x,y)= (random.randint(-100,100), random.randint(-200,200))
        block_list.append((x,y))
    # print(block_list)
    return block_list


def is_position_blocked(x,y):
    """Comapares the robot position with the position of the blocks and returns a Boolean.

    Args:
        x (int): x co-ordinate
        y (int): y co-ordinate

    Returns:
        [Boolean]: True or False depending on certain conditions being met.
    """

    global block_list
    for co_ordinates in block_list:
        if co_ordinates[0] <= x <= co_ordinates[0]+4 and co_ordinates[1] <= y <= co_ordinates[1]:
            return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    """[summary]

    Args:
        x1 (int): old x co-ordinate
        y1 (int): old y co-ordinate
        x2 (int): new x co-ordinate
        y2 (int): new y co-ordinate

    Returns:
        [Boolean]: True or False depending on certain conditions being met.
    """

    # Caters for moving backward
    if x1 > x2:
        (x1,x2) = (x2,x1)
    if y1 > y2:
        (y1,y2) = (y2, y1)

    if y1==y2:
        for x in range(x1,x2,+1):
            if is_position_blocked(x,y1):
                return True

    if x1==x2:
        for y in range(y1,y2,+1):
            if is_position_blocked(x1,y):
                return True
    return False
