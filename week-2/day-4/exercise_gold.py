#exercis-1
# def get_user_age(year, month):
#    current_year = 2023
#    current_month = 9
#    user_age = current_year - year
#    if month > current_month:
#        user_age -= 1
#    return user_age
   
# def can_retire(gender, date_birth):
#     if gender == "Female":
#        if date_birth >= 62:
#            print('you can retire')
#        else:
#            print('you cannot retire')
#     elif gender == "Male":
#         if date_birth >= 67:
#             print('you can retire')
#         else:
#             print('you cannot retire')
#     elif gender != "Female" or "Male":
#         print("your gender is not correct")

# year = int(input("in witch year were you born?\n"))
# month = int(input("in witch month were you born\n"))
# gender = input("choose a gender: Female or Male\n")
# date_birth = get_user_age(year, month)
# can_retire(gender, date_birth)

#exercise-2
# def calculate(x: int):
#     item1 = x
#     item2 = str(x)*2
#     item3 = str(x)*3
#     item4 = str(x)*4
#     return item1 + int(item2) + int(item3) + int(item4)
    
# print(calculate(3))
    
#exercise-3
import random
def throw_dice():
    return random.randint(1, 6)
    
def throw_until_doubles():
    count = 0
    dice1 = 0
    dice2 = 1
    while dice1 != dice2:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
    return count

def main():
    trouws = []
    for _ in range(throw_until_doubles(), 100):
        trouws.append(throw_until_doubles())
    total_sum = sum(trouws)
    print(f"for making 100 doubles it take us {total_sum} tries")
    average = total_sum / len(trouws)
    print(f'the average of tries for each double is {round(average, 2)}')
main()
        

    