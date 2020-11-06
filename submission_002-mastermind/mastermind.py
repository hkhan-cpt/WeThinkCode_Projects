import random


def run_game():
    """
    TODO: implement Mastermind code here
    """

    #Step 1: Generate a random 4-digit code and store it in a list
    code_list=[] #Creating empty list to store code
    while len(code_list) < 4: #Loop runs until list contains 4 numbers
        random_number= str(random.randint(1, 8)) #Generating a random number between 1 and 8
        if random_number not in code_list: #Avoid duplicates by only adding number not found in list 
            code_list.append(random_number)

    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")


    #Step 4:
    turns_left= 12 #Setting game to start with 12 guesses
    while turns_left >0: #Loop runs while user has turns left

        #Step 2: Get user input and enforce restrictions
        guess= input("Input 4 digit code: ") #Get user input
        while guess.isdigit()==False or len(guess) != 4 or "9" in guess or "0" in guess: #Restrictions
            print("Please enter exactly 4 digits.")
            guess= input("Input 4 digit code: ")

        #Step 3: Providing feedback based on user input
        correct_guesses= 0 #Initialize variable
        correct_number_wrong_place= 0 #Initialize variable
        for counter in range(0, len(code_list)): #Using for loop to compare individual characters of both strings
            if guess[counter] == code_list[counter]: #Checking for correct guess
                correct_guesses +=1
            elif guess[counter] in code_list: #Checking for correct number in incorrect place
                correct_number_wrong_place +=1

        #Displaying feedback
        print("Number of correct digits in correct place:     " +str(correct_guesses))
        print("Number of correct digits not in correct place: " +str(correct_number_wrong_place))

        if correct_guesses == 4: #Positive feedback if all 4 numbers guessed correctly
            print("Congratulations! You are a codebreaker!\nThe code was: " + "".join(code_list))
            break #Exit code if user won the game
        elif correct_guesses != 4:
            turns_left -=1 #Reducing number of turns left
            print("Turns left: " + str(turns_left)) #Displaying number of turns left
            if turns_left ==0: #Negative feedback if user has no turns left
                print("Game over!")

if __name__ == "__main__":
    run_game()
