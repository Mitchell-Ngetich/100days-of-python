import random

# def format_name(f_name, l_name):
#     title_case1 = f_name.title()
#     title_case2 = l_name.title()
#     return f"{title_case1} {title_case2}"
# output = format_name("mitchell","ngetich")
# print(output)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: return False
        else: return True
    else: return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
    if is_leap_year(year) and month == 2   :
        return 29
    else:return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
