from math import *
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

age = int(input("What is your age? "))
years = int(90 - int(age))
months = years * 12
weeks = years * 52
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
two_digit = input("Type a two digit number: ")
print(int(two_digit[0]) + int(two_digit[1]))
print(type(two_digit))


# Functions

