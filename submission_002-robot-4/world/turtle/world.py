import turtle
from world import obstacles


# Displaying the toy robot
turtle.title("Hassan's Toy Robot")
turtle.bgcolor("black")
turtle.setup(width = 500, height = 700)
robot = turtle.Turtle()
robot.color("yellow")
robot.fillcolor("green")
robot.left(90)
robot.shapesize(1)

# Displaying the restricted area 
fence = turtle.Turtle()
fence.shape("classic")
fence.color("red")
fence.shapesize(0.01)
fence.speed(0)

fence.penup()
fence.goto(100, 0)
fence.pendown()
fence.left(90)

for i in range(2):
    fence.forward(200)
    fence.left(90)
    fence.forward(200)
    fence.left(90)
    fence.forward(200)


# Displaying the obstacles
block = turtle.Turtle()

block.shape("square")
block.color("red")
block.shapesize(0.01)
block.speed(10)

block_list = obstacles.get_obstacles()
for co_ordinates in block_list:
    block.penup()
    block.goto(co_ordinates)
    block.pendown()

    # Drawing the blocks
    block.begin_fill()
    for i in range(4):
        block.fillcolor("red")
        block.forward(4)
        block.left(90)
    block.end_fill()


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
        robot.penup()
        robot.goto(new_x, new_y)
        robot.pendown()
        return True
    return False