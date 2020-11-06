"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', "replay"]

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#Initializing global variables
history = []
silent, reverse = False, False

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    global silent, reverse
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    instruction = command
    if " silent" in command:
        command = command.replace(" silent", "")
        silent = True
    if " reversed" in command:
        command = command.replace(" reversed", "")
        reverse = True

    if " SILENT" in command:
        command = command.replace(" SILENT", "")
        silent = True
    if " REVERSED" in command:
        command = command.replace(" REVERSED", "")
        reverse = True

    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+instruction+"'.")
        command = input(prompt)
        instruction = command
        silent = False
        reverse = False

        if " silent" in command:
            command = command.replace(" silent", "")
            silent = True
        if " reversed" in command:
            command = command.replace(" reversed", "")
            reverse = True

    if " SILENT" in command:
        command = command.replace(" SILENT", "")
        silent = True
    if " REVERSED" in command:
        command = command.replace(" REVERSED", "")
        reverse = True

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1].split("-")
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is a digit or not
    :param value: a string value to test
    :return: True if it is a digit
    """
    # try:
    #     int(value)
    #     return True
    # except ValueError:
    #     return False

    check_if_int = list(map(lambda value: value.isdigit(), value))
    if False in check_if_int:
        return False
    return True


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


#Update help every time new function added
def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK    - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT   - turn right by 90 degrees
LEFT    - turn left by 90 degrees
SPRINT  - sprint forward according to a formula
REPLAY  - make the robot redo movement commands
REPLAY SILENT          - make the robot redo movement commands but only display final position
REPLAY REVERSED        - make the robot redo movement commands in reverse order
REPLAY REVERSED SILENT - make the robot redo movement commands in reverse order but only display final position
"""


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


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
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

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


#Step 6: Update all replay functions to allow selection of commands

#Step 1: Keep a history of commands performed by the robot
#Steps 2-6: When a command is replayed, it should not be added to the history
def store_history(command, valid_command):
    """Keeps a history of valid commands given to the robot by storing it in a list.

    Args:
        command (string): the command entered by user

    Returns:
        [list]: all valid commands entered by the user 
    """
    global history
    (command_name, arg1) = split_command_input(command)
    if command_name in valid_commands and command_name != "replay":
        history.append(command)
        # print (history)
        return history

    return history


#Step 2: Only redo the movement commands
def do_replay(robot_name, history, command):
    """Filters out all non-movement commands and only redos the movement commands.

    Args:
        robot_name (string): 
        history (list): 
        command (string): 

    Returns:
        [Boolean, string]: (True, replay output text)
    """
    replayed_commands = 0
    (command_name, arg) = split_command_input(command)
    for command in history:
        if "help" in history:
            history.remove("help")
    # print(history)

    if len(arg) > 1:
        for command in history[len(history)-int(arg[0]) : len(history)-int(arg[1])]:
            handle_command(robot_name, command)
            replayed_commands +=1
    elif len(arg) == 1:
        for command in history[len(history)-int(arg[0]) : ]:
            handle_command(robot_name, command)
            replayed_commands +=1
    else:
        for command in history:
            handle_command(robot_name, command)
            replayed_commands +=1 

    return True, " > " +robot_name+ " replayed " +str(replayed_commands)+ " commands."


#Step 3: Replay function, but only display position changes.
def do_replay_silent(robot_name, history, command):
    """Filters out all non-movement commands and only redos the movement commands. It does not show the
    output of each command, only the number of commands replayed and the final position.

    Args:
        robot_name (string): 
        history (list): 
        command (string): 

    Returns:
        [Boolean, string]: (True, replay silent output text)
    """
    global silent
    replayed_commands = 0
    (command_name, arg) = split_command_input(command)
    for command in history:
        if "help" in history:
            history.remove("help")
    # print(history)

    if len(arg) > 1:
        for command in history[len(history)-int(arg[0]) : len(history)-int(arg[1])]:
            handle_command(robot_name, command)
            replayed_commands +=1
    elif len(arg) == 1:
        for command in history[len(history)-int(arg[0]): ]:
            handle_command(robot_name, command)
            replayed_commands +=1
    else:
        for command in history:
            handle_command(robot_name, command)
            replayed_commands +=1
    silent = False

    return True, " > " +robot_name+ " replayed " +str(replayed_commands)+ " commands silently."


#Step 4: Replay movement commands in reverse order 
def do_replay_reversed(robot_name, history, command):
    """Filters out all non-movement commands and redos the movement commands in reverse order. 

    Args:
        robot_name (string): 
        history (list): 
        command (string): 

    Returns:
        [Boolean, string]: (True, replay reversed output text)
    """
    global reverse
    replayed_commands = 0
    (command_name, arg) = split_command_input(command)
    for command in history:
        if "help" in history:
            history.remove("help")
    # print(history)

    history.reverse()
    if len(arg) > 1:
        for command in history[len(history)-int(arg[0]) : len(history)-int(arg[1])]:
            handle_command(robot_name, command)
            replayed_commands +=1
    elif len(arg) == 1:
        for command in history[len(history)-int(arg[0]): ]:
            handle_command(robot_name, command)
            replayed_commands +=1
    else:
        for command in history:
            handle_command(robot_name, command)
            replayed_commands +=1
    reverse = False

    return True, " > " +robot_name+ " replayed " +str(replayed_commands)+ " commands in reverse."


#Step 5: Replay movement commands in reverse order, silently
def do_replay_reversed_silent(robot_name, history, command):
    """Filters out all non-movement commands and redos the movement commands in reverse order. It does not show the
    output of each command, only the number of commands replayed and the final position.

    Args:
        robot_name (string): 
        history (list): 
        command (string): 

    Returns:
        [Boolean, string]: (True, replay reversed silent output text)
    """
    global reverse, silent
    replayed_commands = 0
    (command_name, arg) = split_command_input(command)
    for command in history:
        if "help" in history:
            history.remove("help")
    # print(history)

    history.reverse()
    if len(arg) > 1:
        for command in history[len(history)-int(arg[0]) : len(history)-int(arg[1])]:
            handle_command(robot_name, command)
            replayed_commands +=1
    elif len(arg) == 1:
        for command in history[len(history)-int(arg[0]): ]:
            handle_command(robot_name, command)
            replayed_commands +=1
    else:
        for command in history:
            handle_command(robot_name, command)
            replayed_commands +=1
    reverse, silent = False, False

    return True, " > " +robot_name+ " replayed " +str(replayed_commands)+ " commands in reverse silently."


def check_flags(robot_name, command):
    """Runs the required replay function based on combinations of silent and reverse being True or False.

    Args:
        robot_name (string): 
        command (string): 

    Returns:
        [Boolean, string]: (True, text output of specific replay function)
    """
    global silent, reverse, history
    if silent == False and reverse == False:
        (do_next, command_output) = do_replay(robot_name, history, command)

    if silent == True and reverse == False:
        (do_next, command_output) = do_replay_silent(robot_name, history, command)

    if silent == False and reverse == True:
        (do_next, command_output) = do_replay_reversed(robot_name, history, command)

    if silent == True and reverse == True:
        (do_next, command_output) = do_replay_reversed_silent(robot_name, history, command)

    return True, command_output


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)
    global history

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg[0]))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg[0]))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg[0]))

    elif command_name == "replay":
        (do_next, command_output) = check_flags(robot_name, command)

    if silent == False:
        print(command_output)
        show_position(robot_name)

    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history, silent, reverse

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0
    history = []
    silent, reverse = False, False

    command = get_command(robot_name)
    history = store_history(command, valid_commands)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
        history = store_history(command, valid_commands)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
