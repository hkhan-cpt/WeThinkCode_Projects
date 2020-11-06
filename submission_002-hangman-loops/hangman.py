import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ').lower()


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word 


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_index= random.randint(0, len(word)-1) #generating interger for position of random letter
    letter_list= list(word) #converting to list

    for counter in range (0, len(word)): #using for loop to check entire word for random letter
        if counter != random_index: #comparing position intergers
            letter_list[counter]="_" #replacing other letters with underscore

    return "".join(letter_list) #combines underscores with randomly selected letter


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    counter_original=0 #initializing variable
    counter_answer=0 #initializing variable
    for counter in range (0, len(original_word)): #using for loop to check enitre original word for guessed letter
        if char == original_word[counter]: #comparing position intergers
            counter_original +=1 #incrementing

    for counter in range (0, len(answer_word)): #using for loop to check entire answer word for guessed letter
        if char == answer_word[counter]: #comparing position intergers
            counter_answer +=1 #incrementing

    if counter_original == counter_answer: #comparing position intergers
        return False
    else:
        return True

# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    answer_as_list= list(answer_word) #converts answer to list
    for counter in range(0, len(original_word)): #using for loop to check entire word for random letter
        if char == original_word[counter] and char != answer_word: #checks if guess is in chosen word and not used already
            answer_as_list[counter] = char
        else:
            counter+=1 #incrementing

    return "".join(answer_as_list) #replaces underscores with correct guesses


def do_correct_answer(original_word, answer, guess): 
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses): #updates figure for each incorrect guess
    if number_guesses==4:
        print("""
/----
|
|
|
|
_______""")

    elif number_guesses==3:
        print("""
/----
|   0
|
|
|
_______""")

    elif number_guesses==2:
        print("""
/----
|   0
|   |
|   |
|
_______""")

    elif number_guesses==1: #use additional backslashes to "escape" special characters
        print("""
/----
|   0
|  /|\\
|   |
|
_______""")
    
    elif number_guesses==0: #use additional backslashes to "escape" special characters
        print("""
/----
|   0
|  /|\\
|   |
|  / \\
_______""")



# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):

    print("Guess the word: "+answer)
    counter=5 #set number of guesses to 5
    while counter >0: #start of while loop
            
        guess = get_user_input()
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess) #runs if user guessed correctly
            if word == answer: #using if loop to exit code if user guessed word correctly
                break

        elif guess == "quit" or guess == "exit": #allow user to end game at anytime using break
            print("Bye!")
            break

        else: 
            counter-=1 #decrementing
            do_wrong_answer(answer, counter) #runs if user guessed incorrectly
            if counter==0: #checks if number of guesses left is 0 
                print("Sorry, you are out of guesses. The word was: " +word) #inform user they have no guesses left and exits the code
                break


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    
    if len(sys.argv) >1: #checking length of list
        words_file = sys.argv[1] #assigning file in list 
    else:
        words_file = ask_file_name() #if blank or not listed, use skeleton prompt

    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

    
    