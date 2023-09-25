import random
# from math import *
#  print("Hello" + " Mitch")

# print("Day 1 - String Manipulation")  
# print('String Conctenation is done with the "+" sign.')
# print('e.g. print("hello" + "world")')
# print("New lines can be created with a bcakslash and n.")

# Input method
# input("what is your name?")
# print("Hello " + input("what is your name?"))

# def main(name):
#     my_name = len(name)
#     return my_name

# name = "Mitchell"
# print(main(name))

# or you can use print(len(input()));
# print(len(raw_input("what is your name? "))) 
# use raw_input instead of input alone
  
# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /   |")
# print("/____|")

# character_name = "Tim"
# characters_age = 40

# print("There once was a man named " + character_name + ",")
# print("he was " + str(characters_age) + " years old.") 
# # you cannot concatenate string and integers in python
# print("He really liked the name " + character_name)
# print("but didn't like being " + str(characters_age) + " years old")  

# phrase = "Giraffe Academy"
# print(phrase.replace("Giraffe", "Elephant")) 

# my_num = -5
# print(sqrt(64))

# name = raw_input("Enter your name: ")
# print("Hello " + name + "!")

# num1 = raw_input("Enter a number: ")
# num2 = raw_input("Enter another number: ")
# print(int(num2) + int(num1))

# mad libs
# color = raw_input("Enter a color: ")
# plural_noun = raw_input("Enter a plural noun: ")
# my_love = raw_input("Enter your love: ")

# print("Roses are " + color)
# print( plural_noun + " are blue")
# print("I love " + my_love)

# Lists = array

# friends = ["Mitch", "Ruth", "Mercy", "Oscar", "Brayo"]
# numbers = [1, 3, 5, 6, 8, 9]
# friends.reverse()
# print(friends)
# like slice method in JS => takes index 1 element to index 3.

# Tuples => cannot be modified
# cordinates = (4,5)
# print(cordinates[1])

# Tip calculator
# bill = 124.56
# tip = 12
# num_people = 7

# ans = (bill * 1.12) / num_people
# # we can use format or round
# # ans1 = round(ans, 2) => both works the same.
# ans1 = "{:.2f}".format(ans)
# print(ans1)

# code challenge
# age = int(raw_input("What is your age? "))
# years = int(90 - age)
# days = int(365 * years)
# weeks = int(52 * years)
# months = int(years * 12)
# message = "you have " + str(days) + " days, " + str(weeks) + " weeks, " + str(months) + " months, " + str(years) + "years."
# print(message)

# height = raw_input("enter your height in m: ")
# weight = raw_input("enter your weigh in kg: ")

# answer = (int(weight) / (float(height)) ** 2)
# print(int(answer))

# age = int(input("What is your age? "))
# years = int(90 - int(age))
# months = years * 12
# weeks = years * 52
# days = years * 365

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
# two_digit = input("Type a two digit number: ")
# print(int(two_digit[0]) + int(two_digit[1]))
# print(type(two_digit)) => check if it is a string or an integer 


# Functions

# def my_function(name):
#     print("Hello, how are you feeling today " + name + "?")

# my_function("Mitchell")

# conditional statements
# is_tall = True
# is_male = False
# is_handsome = True

# if is_tall and is_male and is_handsome:
#     print("I love this Man!")
# elif is_tall and is_male or is_handsome and is_male:
#     print("I still love him")
# else:
#     print("She is a girlfriend!")

# if statements and comparisons.


# Day 3

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age > 18:
#         print("Please pay $12.")
#     elif age >= 12 and age <= 18:
#         print("Please pay $7.")
#     else: print("Please pay $5.")
# else: 
#     print("You cannot ride the rollercoaster")


# number = int(input("Which number do you want wanna divide?  "))

# if number % 2 == 0:
#     print("This number is an even number")
# else:
#     print("This number is an odd number")

# name = raw_input("Enter your name: ")

# print(name)

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / (height ** 2))

# print(bmi)

# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, You are underweight.")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have a normal weight")
# elif bmi < 30:
#     print(f"Your bmi is {bmi},you are overweight")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, You are obese")
# else: print(f"Your bmi is {bmi}, You are clinically obese")

# year = int(input("Which years do yo want to check? "))

# if year % 4 == 0:
#     print("This is a leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("This year is a leap year")
# else:
#     print("This year is not a leap year")

 
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("This year is a leap year")
#         else: print("This year is not a leap year")
#     else: print("This year is a leap year")
# else: print("This year is not a leap year")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 3
#         print("pay $3")
#     elif age <= 18:
#         bill = 7
#         print("pay $7")
#     elif age >= 45 and age <= 55 :
#         print("Free ride")
#     else:
#         bill = 12 
#         print("pay $12")
      
#     want_photo = input("Do you wany a photo taken? Y or N ")
#     if want_photo == "Y":
#         bill += 3
#     print(f"Your final ${bill}")
# else: print("Sorry, you can't ride") 

# print("Welcome to Python Pizza Deliveries!")
# order = input("Do you want to order? Y or N ")
# size = input("What size pizza do you want? S, M, or L ")
# bill = 0


# if order == "Y":
#     if size == "S": 
#         bill = 15
#     elif size == "M":
#         bill = 20
#     elif size == "L":
#         bill = 25
    
#     add_pepperoni = input("Do you want pepperoni? Y or N ")
#     if add_pepperoni == "Y":
#         if size == "S":
#             bill += 2
#         else: bill += 3
    
#     extra_cheese = input("Do you want extra cheese? Y or N ")
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your cheese is ${bill}")
# else: print("No order was made")

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is your name? \n").lower()
# combined = name1 + name2

# true = combined.count("t") + combined.count("r") + combined.count("u") + combined.count("e")
# love = combined.count("l") + combined.count("0") + combined.count("v") + combined.count("e") 

# print(true)
# print(love)
# love_count =  int(str(true) + str(love))
# # you have to change string into int so you can compare to given inter values
# print(love_count)

# if love_count < 10 or love_count > 90:
#     print(f"Your score is {love_count}, you go together like coke and mentos.")
# elif love_count >=40 and love_count <= 50:
#     print(f"Your score is {love_count}, you are alright together")
# else: print(f"your score is {love_count}")

# print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

# step1 = input("Which path do you want to take? Type 'left' or 'right' ").lower()

# if step1 == "left":
#     step2 = input("Do you want to swim or wait? Enter swim or wait  ").lower()
#     if step2 == "wait":
#         step3 = input("Which door do you wish to open? choose one color among red, blue, and yellow ").lower()
#         if step3 == "yellow":
#             print("You win!")
#         else: print("Game Over")
#     else: print("Game Over")
# else: print("Ooops! Game Over")

# ran_integer = random.randint(10, 30)
# print(ran_integer)
# my_random = random.random()
# print(my_random)
# my_num = random.uniform(10.0, 20.5)
# print(my_num)

# random_num = random.randint(0, 1)

# if random_num == 0:
#     print("Tails")
# else: print("Heads")

# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")
# using choice method to generate random name in a list
# random_name = random.choice(names) + " is going to buy the meal today!"
# print(random_name)

# we can also use random.randint(0, len(names - 1)) to generate random name too

# name = len(names)
# print(name)
# random_per = random.randint(0, name - 1 ) 
# print(random_per)
# person_pay = names[random_per] + " will buy the meal today!"
# print(person_pay)

# row1 = ["◻️", "◻️", "◻️"]
# row2 = ["◻️", "◻️", "◻️"]
# row3 = ["◻️", "◻️", "◻️"]
# map = [row1, row2, row3]
# print(f"{row1} \n{row2} \n{row3}")

# position = input("Where do you want to put the treasure? ")

# x = int(position[0])
# y = int(position[1]) 
# map[x - 1][y- 1] = "X"

# print(f"{row1} \n{row2} \n{row3}")
# random_num = [
# ''' 
# _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''',
# '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# ''',
# '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# ]
# random_num[0] == 0
# random_num[1] == 1
# random_num[2] == 2

# game = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors "))
# computer = random.choice(0, 2)

# def my_function():
#     print(random_num[0])
#     print(f"You choose {0}: you win")
#     print(random_num[2])
#     print(f"Computer choose: {2}")

# if game == random_num[0] and computer == random_num[2]:
#     my_function()
# elif game == random_num[2] and computer == random_num[1]:
#     my_function()
# elif game == random_num[1] and computer == random_num[0]:
#     my_function()
# elif int(computer) == game:
#     print(computer)
#     print(random_num(game))
#     print("Draw")
# elif game > 2 or game < 0:
#     print("Invalid input, you lost")
# else: 
#     print(random_num[game])
#     print("You lost")
#     print(computer)
#     print("Computer won")
#     end_game = input("This repl has exited, Play again? ")

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# Create a list of choices with corresponding ASCII art
# choices = [rock, paper, scissors]

# Map choices to integers for user input
# choice_map = {
#     0: "Rock",
#     1: "Paper",
#     2: "Scissors"
# }

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
# computer_choice = random.randint(0, 2)

# print("Your choice:")
# print(choices[user_choice])
# print("Computer's choice:")
# print(choices[computer_choice])

# if user_choice == computer_choice:
#     print("It's a draw!")
# elif (user_choice == 0 and computer_choice == 2) or \
#      (user_choice == 1 and computer_choice == 0) or \
#      (user_choice == 2 and computer_choice == 1):
#     print(f"You win! {choice_map[user_choice]} beats {choice_map[computer_choice]}.")
# else:
#     print(f"You lose! {choice_map[computer_choice]} beats {choice_map[user_choice]}.")

# play_again = input("Do you want to play again? (yes/no): ")
# if play_again.lower() == "no":
#     print("Thanks for playing!")

# student_heights = input("Input a list of student heights ").split()
# sum = 0
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     sum += int(student_heights[n])
# average = round(sum / len(student_heights))

# print(average)


student_scores = input("Input a list of student heights ").split()
max_value = int(student_scores[0])

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
for score in student_scores:
    if score > max_value:
        max_value = score
# print the score outside the loop
print(f"The highest score in the class is {max_value}")
    




