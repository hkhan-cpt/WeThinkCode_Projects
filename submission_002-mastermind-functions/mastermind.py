import random

#Initializing variables to enable use of global
code= []
answer= ""
correct_digits_and_position= 0
correct_digits_only= 0
turns = 0
correct= False

# TODO: Decompose into functions (Five)

def generate_code():
    '''
    Generates 4 random numbers and stores them in a list, without any duplicates. The numbers 
    range from 1 to 8.
    ''' 

    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    
    #print(code)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def get_user_input():
    '''
    Allow the user to input a guess. It checks whether the guess is the correct length i.e. 4 numbers.
    If not, it displays an error message and calls the function to ask the user for input.
    '''
    global answer

    answer = input("Input 4 digit code: ")
    if len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        get_user_input()


def check_result():
    '''
    Takes the user input and compares it to the generated code. It compares each number of the generated
    code with the entire guess of the user. It updates the appropriate feedback response based on any 
    numbers which are correct and in the correct position, as well as a correct number but in the wrong
    position. It uses code from generate_code and answer from get_user_input.
    '''
    global code
    global answer
    global correct_digits_and_position
    global correct_digits_only

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1


def display_feedback():
    '''
    Prints feedback for the user to make better guesses. Adds to the number of turns(until it reaches 12 or 
    the user has won the game). It uses correct_digits_and_position and correct_digits_only from check_result.
    '''
    global correct_digits_and_position
    global correct_digits_only
    global turns

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    turns += 1


def win_or_not():
    '''
    Constantly checks if the user has won the game or not using Boolean logic. If all 4 numbers of the guess are 
    correct and in the correct position, it displays a congratulatory message and exits the code. If not, it reduces
    the number of turns the user has left(until it reaches 12 or the user has won the game. It uses code from 
    generate_code, answer from get_user_input, correct_digits_and_position from check_result and turns from display_feedback.
    '''
    global code
    global correct_digits_and_position
    global turns
    global correct

    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
        
    else:
        print('Turns left: '+str(12 - turns))


def run_game():
    '''
    Main purpose of this function is to call all other functions. It runs the required functions while the user still has 
    turns left. Also prints the code at the end of the game, no matter the outcome. It uses correct from win_or_not.
    '''
    global correct

    correct = False
    
    generate_code()
    
    while not correct and turns <12:
        get_user_input()

        check_result()

        display_feedback()

        win_or_not()
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()
