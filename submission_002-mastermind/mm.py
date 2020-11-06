import random

def run_game():

    number_list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
    code_list= []

    for counter in range (0, 4):
        random_index= random.randint(0, len(number_list))
        code_list.append(random_index)
        print(code_list)

if __name__ == "_main_":
    run_game()
