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

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    plain_text = []
    for char in text:
        if char in alphabets:
            index = alphabets.index(char)
            if direction == 'encode':
                new_index = (index + shift) % len(alphabets)
            else: new_index = (index - shift) % len(alphabets)
            plain_text.append(alphabets[new_index])  
        else: plain_text.append(char)
    final_text = "".join(plain_text)
    print(f"Your {direction}d text is: {final_text}")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caeser(text, shift, direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_end = True
        print("Goodbye!")



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
    