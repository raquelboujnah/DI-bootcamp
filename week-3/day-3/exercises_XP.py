#exercise-1
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
        
#     def __str__(self):
#         return f"{self.amount} {self.currency}"
        
#     def __int__(self):
#         return self.amount
    
#     def __repr__(self):
#         return f"curency : {self.currency} amount : {self.amount}"
    
#     def __add__(self, other):
#         try:
#             if self.currency == other.currency:
#                return self.amount + other.amount
#             else:
#                 TypeError("Cannot add between Currency type <self.currency> and <other.currency>")
#         except:
#             return self.amount + other
    
#     def __iadd__(self, other):
#         try:
#             self.amount += other.amount
#             return self
#         except:
#             self.amount += other
#             return self
    

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)
# c1.__str__()
# print(c1.__int__())
# print(c1 + c2)
# print(c1 + 2)
# print(c1.amount)
# c1 += 5
# print(c1.amount)


# #exercise-2
# import func

# #exercise-3
import random
# def random_num():
#     user_num = int(input("choose a number between 1-100"))
#     random_number = random.randint(1, 101)
#     if user_num == random_number:
#         print("we choose the same number")
#     else:
#         return

#exercise-4
import string
def random_str():
    word = ''.join(random.choices(string.ascii_letters, k=5))
    print(word)
    
random_str()

#exercise-5
from datetime import datetime
def what_time():
    time = datetime.now().date()
    print(time)
what_time()
    
#exercise-6
from math import ceil
def until_jan():
    current_date = datetime.now()
    target_date = datetime(current_date.year + 1, 1, 1)
    time_difference = target_date - current_date
    days = time_difference.days
    hours = ceil(time_difference.seconds/3600)
    minutes = hours*60
    print(f"the 1st of January is in {days} days, {hours} hours, {minutes} minutes ")
until_jan()


#exercise-7
def birthdate(day, month, year):
    year = datetime.now().year - year 
    year_minute = year * 525600
    month_minute = month * 43820
    day_minute = day * 1440
    minutes = year_minute + month_minute + day_minute
    print(minutes)
birthdate(22, 8, 2001)

#exercise-8
list_1 = []

    
    
    



