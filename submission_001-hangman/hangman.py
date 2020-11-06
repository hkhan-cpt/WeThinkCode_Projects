#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    
    open_file= open(file_name, 'r')
    short_words= open_file.readlines()
    
    return short_words


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    random_word= random.randint(0,len(words)-1)
    word= list(words[random_word])

    letter_rep= random.randint(0,len(word)-2)
    word[letter_rep]= '_'
    new_word= ''.join(word)

    print ("Guess the word: " + new_word)

    return words[random_word]



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """

    user_guess= input("Guess the missing letter: ")
    return user_guess


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

