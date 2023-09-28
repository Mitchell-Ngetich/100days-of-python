import random
import math

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

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# if direction != 'encode' and direction != 'decode': print("Invalid direction: try again!")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))
plain_text = []

def caeser(text, shift, direction):
    for letter in text:
        if letter in alphabets:
            index = alphabets.index(letter)
            if direction == 'encode':
                new_index = (index + shift) % len(alphabets)
            else: new_index = (index - shift) % len(alphabets)
            plain_text.append(alphabets[new_index])  
        else: plain_text.append(letter)
    final_text = "".join(plain_text)
    print(f"Your {direction}d text is: {final_text}")
caeser(text, shift, direction)



# def decrypt(text, shift):
#     for letter in text:
#         index2 = alphabets.index(letter)
#         index3 = (index2 - shift) % len(alphabets)
#         plain_text += alphabets[index3]
#     print(f"The decoded text is {plain_text}")

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
    