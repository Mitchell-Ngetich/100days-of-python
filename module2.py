import random
import os

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/OS X
        os.system('clear')

def random_num():
    num_generated = random.randint(0, 100)
    print(num_generated)
    return num_generated

def condition_counter(num_generated, count):
    number = int(input("Make a guess: "))
    
    if number == num_generated:
        print("Bravo!, you have guessed it correctly")
        return False # tells the program to stop running
    elif number > num_generated:
        print("Too high.")
        print("Guess again")
    elif number < num_generated:
        print("Too low.")
        if count > 1:
            print("Guess again")
    return True

def guessing_game():
    count = 10
    count_hard = 5
    print("Welcome to the Number guessing game")
    print("I'm thinking of a number between 1 and 100")
    user_input = input("Choose a difficulty. Type 'easy' or 'hard' ")
    num_generated = random_num()
    while True:
        if user_input == "easy":
            print(f"You have {count} attempts remaining to guess the number.")
            guess_game = condition_counter(num_generated, count)
            count -= 1
        elif user_input == "hard":
            print(f"You have {count_hard} attempts remaining to guess the number")
            guess_game = condition_counter(num_generated, count_hard)
            count_hard -= 1
        else:
            print("Invalid input.")
            return
        if not guess_game:
            break
        
        if count < 1 or count_hard < 1:
            print("You have run out of guesses, you lose")
            print()
            print()
            break
        
    final_input = input("Do you want to restart the game? Type 'yes' or 'no' ")
    while final_input == "yes":
        clear_screen()
        guessing_game()
        # final_input = input("Do you want to restart the game? Type 'yes' or 'no' ")

guessing_game()