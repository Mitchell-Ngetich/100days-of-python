import random
import math
from cipher import logo

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
    
# greet_with("Mitchell", "Nairobi")
# test_h = int(input("Height of a wall: "))
# test_w = int(input("width of a wall: "))
# coverage = 5

# def calc_wall(height, width):
#    cover = test_h * test_w / coverage
#    #round it up coz no 9.4 cans of paint.
#    print(f"You will need {math.ceil(cover)} cans of paint")
# calc_wall(height = test_h, width = test_w)
    
# n = int(input("Check this number: "))

# def prime_checker(number):
#     if n > 1:
#         for integer in range(2, int(n/2) +1):
#         # since the largest divisibility of n is its half number eg 12 will be 6
#         #so if there's not number divisible from 2 to n/2, then its a prime number
#             if(n % integer == 0):
#                 print(f"It's not a prime number")
#                 break
#         else: print(f"It's a prime number")
    
# prime_checker(number = n)

# print(logo)

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caeser(text, shift, direction):
#     plain_text = []
#     for char in text:
#         if char in alphabets:
#             index = alphabets.index(char)
#             if direction == 'encode':
#                 new_index = (index + shift) % len(alphabets)
#             else: new_index = (index - shift) % len(alphabets)
#             plain_text.append(alphabets[new_index])  
#         else: plain_text.append(char)
#     final_text = "".join(plain_text)
#     print(f"Your {direction}d text is: {final_text}")

# should_end = True
# while should_end:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
    
#     caeser(text, shift, direction)
    
#     result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if result == "no":
#         should_end = False
#         print("Goodbye!")



# def decrypt(text, shift):
#     for char in text:
#         index2 = alphabets.index(letter)
#         index3 = (index2 - shift) % len(alphabets)
#         plain_text += alphabets[index3]
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)

# spam = 0
# while spam < 10:
#     print('Hello, world.')
#     spam = spam + 1
#     print(spam)

# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')


# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#          break
# print('Thank you!')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#        continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')   

# import random
# for i in range(5):
#     print(random.randint(1, 10))

#Build a guess game. where the user gueses the number

# print("This is a number guessing game, I'm thinking of a number between 1 to 20")
# number = random.randint(1, 20)
# print(number)

# guess_game = 0

# while guess_game < 6: #or use a for loop
#     guess = int(input("Guess my secret number "))
#     if number == guess:
#         print("Bravo, you guessed correctly")
#         break
#     elif number > guess:
#         print("Your guess is too low")
#     elif number < guess:
#         print("Your guess is too high")
#     guess_game += 1
# if guess != number:
#     print(f"you have run out of guesses, the secret number was, {number}")
# if guess == number:
#     print("Bravo, you guessed correctly")
# else:
#     print(f"You have guessed {guessNumber} times, the number you were looking for is {number}")


    
    ############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
    
import os
from art import logo 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def random_cards():
    random_cards = random.choice(cards)
    return random_cards

def add_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"
    
    
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    
    print(logo)
    
    is_game_over = False

    for _ in range(2):
        user_cards.append(random_cards())
        computer_cards.append(random_cards())
        
    while not is_game_over:
        user_score = add_score(user_cards)
        computer_score = add_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(random_cards())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random_cards())
        computer_score = add_score(computer_cards)

    print(f"Your final score: {user_cards}, final score: {user_score}")
    print(f"Computer's final score: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wish to play a game of blackjack? (y/n) ") == "y": 
    clear_console()
    user_cards = []
    computer_cards = []
    play_game()
