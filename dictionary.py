# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades = {}

# for key, value in student_scores.items(): # for student in student_scores:
#     #use can use student instedd of key, value, then you will avoid using .items()
#     #then set student_grades[student] = score
#     if value >= 91: 
#         student_grades[key] = "Outstanding"
#     elif value >= 81:
#         student_grades[key] ="Exceeds Expectations"
#     elif value >= 71:
#         student_grades[key] = "Acceptable"
#     else: student_grades[key] = "Fail"
# print(student_grades)


# travel_log = {
#     "France": {"cities_visited":["Paris","Lille", "Dijon"]},
#     "Kenya": {"cities_visited":["Nairobi","Eldoret","Mombasa", "Nakuru"], "next-plan": ["Kisumu", "Lamu"]},
# }
# print(travel_log["Kenya"])

# travel_log = [
#     {
#         "country": "Kenya",
#         "visits": 12,
#         "cities": ["Nairobi","Eldoret","Mombasa"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     }
# ]

# def add_new_country(countrie, visits, cities):
#     new_entry = {"country": countrie, "visits": visits, "cities": cities}
#     travel_log.append(new_entry)
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# print(travel_log)

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

new_person = []

def bid_game(name, price):
   
    new_entry = {"name": name, "price": price}
    new_person.append(new_entry)

max_bid = 0
winner_name = ""
end_game = False
while not end_game:
    name = input("Enter your name ")
    price = int(input("How much do you want to bid? $"))
    bid_game(name, price)
    
    new_user = input("Are there any other bider? type 'yes' or 'no' ").lower()
    if new_user == "yes":
        clear_console()
    elif new_user == "no":
        for entry in new_person:
            if entry["price"] > max_bid:
                max_bid = entry["price"]
                winner_name = entry["name"]
        print(f"The winner of this bid occasion is {winner_name}, with a bid of ${max_bid}")
        end_game = True
print(new_person)  