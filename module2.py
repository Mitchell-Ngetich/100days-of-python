# import random
# import os

# def clear_screen():
#     if os.name == 'nt':  # For Windows
#         os.system('cls')
#     else:  # For Linux/OS X
#         os.system('clear')

# def random_num():
#     num_generated = random.randint(0, 100)
#     return num_generated

# def condition_counter(num_generated, count):
#     number = int(input("Make a guess: "))
    
#     if number == num_generated:
#         print("Bravo!, you got it The answer is {num_generated}}")
#         return False # tells the program to stop running
#     elif number > num_generated:
#         print("Too high.")
#         print("Guess again")
#     elif number < num_generated:
#         print("Too low.")
#         if count > 1:
#             print("Guess again")
#     return True

# def guessing_game():
#     count = 10
#     count_hard = 5
#     print("Welcome to the Number guessing game")
#     print("I'm thinking of a number between 1 and 100")
#     user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     num_generated = random_num()
#     while True:
#         if user_input == "easy":
#             print(f"You have {count} attempts remaining to guess the number.")
#             guess_game = condition_counter(num_generated, count)
#             count -= 1
#         elif user_input == "hard":
#             # print(f"You have {count_hard} attempts remaining to guess the number")
#             guess_game = condition_counter(num_generated, count_hard)
#             count_hard -= 1
#         else:
#             print("Invalid input.")
#             return
#         if not guess_game:
#             break
        
#         if count < 1 or count_hard < 1:
#             print("You have run out of guesses, you lose")
#             print()
#             print()
#             break
        
#     final_input = input("Do you want to restart the game? Type 'yes' or 'no': ")
#     while final_input == "yes":
#         clear_screen()
#         guessing_game()


# guessing_game()

#Debbugging
############DEBUGGING#####################

# Describe Problem

# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

# number = int(input("Which number do you want to check? "))

# if number % 2 ==0:
#     print("This is an even number.")
# else: print("This is a odd number.")

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else: print("Not a leap year")