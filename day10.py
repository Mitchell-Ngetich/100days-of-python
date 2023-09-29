import random

# def format_name(f_name, l_name):
#     title_case1 = f_name.title()
#     title_case2 = l_name.title()
#     return f"{title_case1} {title_case2}"
# output = format_name("mitchell","ngetich")
# print(output)

# def is_leap_year(year):
#     '''Checks if the year is a leap year or not'''
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else: return False
#         else: return True
#     else: return False

# def days_in_month(year, month):
#     '''Store the number of days in a month and return 29 for feb if its a leap year'''
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
#     if is_leap_year(year) and month == 2   :
#         return 29
#     else:return month_days[month - 1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calc():
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)
        
    is_calculator = False
    while not is_calculator:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? "))

        if operation_symbol in operations:
            calculation = operations[operation_symbol]
            answer = calculation(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}") 
            new_input =input(f"Type 'y' to continue calculating with {answer}, type 's' to start a new calculation or type 'n' to exit.:")
            if new_input == 'y':
                num1 = answer
            elif new_input == 's':
                is_calculator = True
                calc()
            else: 
                is_calculator = True
                print("Exiting....Goodbye!")
        else: "Invalid choice"
calc()