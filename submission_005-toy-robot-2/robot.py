x= 0
y= 0


def robot_start():
    """This is the entry function, do not change"""
    #pass
    robot_name = naming_robot()
    greet_user(robot_name)
    loop_commands(robot_name)


#Step 1: Get user input to name the robot and greet user
def naming_robot():
    """Asks the user for input to name the robot and returns it so it can be used
    by the other functions later. 
    """ 
    robot_name = input("What do you want to name your robot? ")
    return robot_name


def greet_user(robot_name):
    """Displays a welcome message to the user.

    Args:
        robot_name (string): Name taken from the naming_robot function.
    """
    print(robot_name + ": Hello kiddo!")


#Step 2: Get input from the user to provide instructions for the robot
def get_command(robot_name):
    """Receives a command as input from the user.Checks if it is in the
    list of allowed commands. If not, it informs the user and asks for
    input again. All commands are case insensitve.

    Args:
        robot_name (string): Name taken from the naming_robot function.

    Returns:
        [string]: Command provided for the robot by the user.
    """
    instruction = input(robot_name + ": What must I do next? ")
    comm_list= ["off", "help", "forward", "back", "right", "left", "sprint"]

    if len(instruction.split()) == 0 or instruction.split()[0].lower() not in comm_list:
        print(robot_name + ": Sorry, I did not understand", "'" +instruction + "'.")
        instruction= get_command(robot_name)
    return instruction


def off_command(robot_name):
    """If the user inputs "off", it displays a message indicating
    the robot is being shut down and resets it's co-ordinates.

    Args:
        robot_name (string): Name taken from the naming_robot function.
    """
    global x
    global y

    Boolean = False
    print(robot_name + ": Shutting down..")
    x= 0
    y= 0


#Step 3: Enable HELP command and update relevant functions
def help_command():
    """Returns the dictionary so it can be used by the printing function

    Returns:
        [dictionary]: Stores the valid commands.
    """
    comm_dict= {
    "off ": "Shut down robot",
    "help": "provide information about commands",
    "forward": "move the robot forward",
    "back   ": "move the robot back",
    "right  ": "make the robot do a right-turn",
    "left   ": "make the robot do a left-turn",
    "sprint ": "make the robot sprint forward"
    }
    return comm_dict


def display_help_information(comm_dict):
    """Displays the available commands to the user if they input "help".

    Args:
        comm_dict (dictionary): Taken from the help_command function.
    """
    print("I can understand these commands:")
    for (item, value) in comm_dict.items():
        print(item.upper(), "-", value)


#Step 5: Enable FORWARD command and update relevant functions
def forward_command(instruction, direction, robot_name):
    """If the user inputs "forward" with a number, it moves the robot forward depending on the number of steps
    provided by the user. Updates the x and y co-ordinates. Does not allow the robot to move beyond the fixed area.


    Args:
        instruction (string): Taken from the get_command function consisting of "forward" and a number of steps(integer).
        direction (string): Determines which of the x and y values will be updated.
        robot_name (string): Name taken from the naming_robot function.
    """
    global x
    global y

    if direction == "north":
        if y + int(instruction.split()[1]) > 200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)

        else:
            y= y + int(instruction.split()[1])
            print(" >", robot_name, "moved forward by", instruction.split()[1], "steps.")
            display_position(robot_name)

    elif direction == "east":
        if x + int(instruction.split()[1]) > 100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)
        
        else:
            x= x + int(instruction.split()[1])
            print(" >", robot_name, "moved forward by", instruction.split()[1], "steps.")
            display_position(robot_name)

    elif direction == "south":
        if y - int(instruction.split()[1]) < -200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)
        
        else:
            y= y - int(instruction.split()[1])
            print(" >", robot_name, "moved forward by", instruction.split()[1], "steps.")
            display_position(robot_name)

    elif direction == "west":
        if x - int(instruction.split()[1]) < -100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)

        else:
            x= x - int(instruction.split()[1])
            print(" >", robot_name, "moved forward by", instruction.split()[1], "steps.")
            display_position(robot_name)


#Step 7: Enable BACK command and update relevant functions
def back_command(instruction, direction, robot_name):
    """If the user inputs "back" with a number, it moves the robot back depending on the number of steps provided
    by the user. Updates the x and y co-ordinates. Does not allow the robot to move beyond the fixed area.

    Args:
        instruction (string): Taken from the get_command function consisting of "back" and a number of steps(integer).
        direction (string): Determines which of the x and y values will be updated.
        robot_name (string): Name taken from the naming_robot function.
    """
    global x
    global y

    if direction == "north":
        if y - int(instruction.split()[1]) < -200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)

        else:
            y= y - int(instruction.split()[1])
            print(" >", robot_name, "moved back by", instruction.split()[1], "steps.")
            display_position(robot_name)

    elif direction == "east":
        if x - int(instruction.split()[1]) < -100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)

        else:
            x= x - int(instruction.split()[1])
            print(" >", robot_name, "moved back by", instruction.split()[1], "steps.")
            display_position(robot_name)

    elif direction == "south":
        if y + int(instruction.split()[1]) > 200:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)

        else:
            y= y + int(instruction.split()[1])
            print(" >", robot_name, "moved back by", instruction.split()[1], "steps.")
            display_position(robot_name)

    elif direction == "west":
        if x + int(instruction.split()[1]) > 100:
            print(robot_name + ": Sorry, I cannot go outside my safe zone.")
            display_position(robot_name)

        else:
            x= x + int(instruction.split()[1])
            print(" >", robot_name, "moved back by", instruction.split()[1], "steps.")
            display_position(robot_name)


#Step 8: Enable RIGHT command and update relevant functions
def right_command(direction, instruction, robot_name):
    """If the user inputs "right", it makes the robot do a 90 degree turn to the right.

    Args:
        instruction (string): Taken from the get_command function.
        direction (string): Determines which of the x and y values will be updated.
        robot_name (string): Name taken from the naming_robot function.

    Returns:
        [string]: Determines which of the x and y values will be updated.
    """
    if direction == "north" and instruction.split()[0] == "right":
        direction = "east"
        print(" >", robot_name, "turned right.")
        display_position(robot_name)

    elif direction == "east" and instruction.split()[0] == "right":
        direction = "south"
        print(" >", robot_name, "turned right.")
        display_position(robot_name)

    elif direction == "south" and instruction.split()[0] == "right":
        direction = "west" 
        print(" >", robot_name, "turned right.")
        display_position(robot_name)

    elif direction == "west" and instruction.split()[0] == "right":
        direction = "north" 
        print(" >", robot_name, "turned right.")
        display_position(robot_name)

    return direction


#Step 9: Enable LEFT command and update relevant functions
def left_command(direction, instruction, robot_name):
    """If the user inputs "left", it makes the robot do a 90 degree turn to the left.

    Args:
        instruction (string): Taken from the get_command function.
        direction (string): Determines which of the x and y values will be updated.
        robot_name (string): Name taken from the naming_robot function.

    Returns:
        [string]: Determines which of the x and y values will be updated.
    """
    if direction == "north" and instruction.split()[0] == "left":
        direction = "west"
        print(" >", robot_name, "turned left.")
        display_position(robot_name)

    elif direction == "west" and instruction.split()[0] == "left":
        direction = "south"
        print(" >", robot_name, "turned left.")
        display_position(robot_name)

    elif direction == "south" and instruction.split()[0] == "left":
        direction = "east" 
        print(" >", robot_name, "turned left.")
        display_position(robot_name)

    elif direction == "east" and instruction.split()[0] == "left":
        direction = "north" 
        print(" >", robot_name, "turned left.")
        display_position(robot_name)

    return direction


#Step 11: Enable SPRINT command and update relevant functions
def sprint_command(direction, instruction, steps, robot_name):
    """If the user inputs "sprint" with a number, the robot starts moving forward the number of steps provided by the
    user. Then it moves forward one step less than the previous move forward. This process is repeated until the number
    of steps reach zero. Updates the x and y co-ordinates. Does not allow the robot to move beyond the fixed area.

    Args:
        instruction (string): Taken from the get_command function consisting of "forward" and a number of steps(integer).
        direction (string): Determines which of the x and y values will be updated.
        steps (string): Determines how far the robot moves forward.
        robot_name (string): Name taken from the naming_robot function.
    """
    global x
    global y

    if steps == 0:
        display_position(robot_name)

    else:
        if direction == "north":
            if y + steps > 200:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                display_position(robot_name)

            else:
                y= y + steps
                print(" >", robot_name, "moved forward by", steps, "steps.")
                sprint_command(direction, instruction, steps - 1, robot_name) 

        elif direction == "east":
            if x + steps > 100:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                display_position(robot_name)

            else:
                x= x + steps
                print(" >", robot_name, "moved forward by", steps, "steps.")
                sprint_command(direction, instruction, steps - 1, robot_name)

        elif direction == "south":
            if y - steps < -200:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                display_position(robot_name)

            else:
                y= y - steps
                print(" >", robot_name, "moved forward by", steps, "steps.")
                sprint_command(direction, instruction, steps - 1, robot_name)

        elif direction == "west":
            if x - steps > -100:
                print(robot_name + ": Sorry, I cannot go outside my safe zone.")
                display_position(robot_name)

            else:
                x= x - steps
                print(" >", robot_name, "moved forward by", steps, "steps.")
                sprint_command(direction, instruction, steps - 1, robot_name)


#Step 6: Track position of the robot and display to the user
def display_position(robot_name):
    """Tracks the x and y co-ordinates of the robot and displays the updated co-ordinates.

    Args:
        robot_name (string): Name taken from the naming_robot function.
    """
    print(" >", robot_name, "now at position", "(" + str(x) + "," + str(y)+ ")" + ".")


def loop_commands(robot_name):
    """Firstly, sets the starting direction as up. Certain parts of the code will run based on user input. The loop
    will continue until the user selects the "off" command. 

    Args:
        robot_name (string): Name taken from the naming_robot function.
    """
    direction = "north"
    Boolean = True

    while Boolean == True:
        instruction = get_command(robot_name)

        if len(instruction.split()) == 1:
            if instruction.split()[0].lower() == "off":
                off_command(robot_name)
                break

            elif instruction.split()[0].lower() == "help":
                comm_dict = help_command()
                display_help_information(comm_dict)

            elif instruction.split()[0].lower() == "right":
                direction = right_command(direction, instruction, robot_name)

            elif instruction.split()[0].lower() == "left":
                direction = left_command(direction, instruction, robot_name)

        elif len(instruction.split()) == 2:
            steps = int(instruction.split()[1])
            if instruction.split()[0].lower() == "forward":
                forward_command(instruction, direction, robot_name)

            elif instruction.split()[0].lower() == "back":
                back_command(instruction, direction, robot_name)

            elif instruction.split()[0].lower() == "sprint":
                sprint_command(direction, instruction, steps, robot_name)


if __name__ == "__main__":
    robot_start()