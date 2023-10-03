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

print("This is a number guessing game, I'm thinking of a number between 1 to 20")
number = random.randint(1, 20)
print(number)

guess_game = 0

while guess_game < 6: #or use a for loop
    guess = int(input("Guess my secret number "))
    if number == guess:
        print("Bravo, you guessed correctly")
        break
    elif number > guess:
        print("Your guess is too low")
    elif number < guess:
        print("Your guess is too high")
    guess_game += 1
if guess != number:
    print(f"you have run out of guesses, the secret number was, {number}")
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

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

# from art import logo
# print(logo)