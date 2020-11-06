

# TODO: Decompose into functions

def move_square(size, degrees):

    '''
    (Literal, Literal) -> None

    Takes the parameters given and displays instuctions for the robot 
    to move in the shape of a square. It uses size and degrees as the 
    two paramters to determine the scale of the movement. The variables 
    can easily be changed in the move function.
    '''

    print("Moving in a square of size "+str(size))
    for i in range(4):
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length, width, degrees):

    '''
    (Literal, Literal, Literal) -> None

    Takes the parameters given and displays instuctions for the robot 
    to move in the shape of a rectangle. It uses length, width and 
    degrees as the three paramters to determine the scale of the 
    movement. The variables can easily be changed in the move function.
    '''

    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle(length, degrees):

    '''
    (Literal, Literal) -> None
    
    Takes the parameters given and displays instuctions for the robot 
    to move in the shape of a circle. It uses length and degrees as the 
    two paramters to determine the scale of the movement. The variables 
    can easily be changed in the move function.
    '''

    print("Moving in a circle")
    for i in range(360):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def move_square_dancing(length):

    '''
    (Literal) -> None
    
    Takes the parameters given and displays instuctions for the robot 
    to perfrom a square dance. It calls the move_square function three 
    times. As such, it uses the size and degrees paramters from the 
    move_sqaure function. Additionally, it uses length to determine 
    the space it moves between each square. The variables can easily 
    be changed in the move function.
    '''

    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(20, 90)


def move_crop_circles():

    '''
    Takes the parameters given and displays instuctions for the robot 
    to move in the shape of crop circles. It calls the move_circle 
    function four times. As such, it uses the length and degrees 
    paramters from the move_circle function. The variables can easily
    be changed in the move function.
    '''

    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward 20")
        move_circle(1, 1)


def move(): #Calls other functions and provides required parameters

    '''
    I think call_functions is a better name as it states clearly what 
    the function does. The function itself has no parameters but it 
    provides them for the other functions wherever they are needed. 
    After that it calls the corresponding function.
    '''

    size= 10
    degrees= 90
    move_square(size, degrees)

    length= 20
    width= 10
    degrees= 90
    move_rectangle(length, width, degrees)

    length= 1
    degrees= 1
    move_circle(length, degrees)

    length= 20
    move_square_dancing(length)

    move_crop_circles()


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
