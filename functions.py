import random
import math

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
    
# greet_with("Mitchell", "Nairobi")
test_h = int(input("Height of a wall: "))
test_w = int(input("width of a wall: "))
coverage = 5

def calc_wall(height, width):
   cover = test_h * test_w / coverage
   #round it up coz no 9.4 cans of paint.
   print(f"You will need {math.ceil(cover)} cans of paint")
calc_wall(height = test_h, width = test_w)
    
    
