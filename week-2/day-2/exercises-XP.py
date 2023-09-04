#exercise-1
# my_fav_numbers = {22, 18, 21}
# my_new_fav_numbers = [23, 2]
# my_fav_numbers.update(my_new_fav_numbers)
# print(my_fav_numbers)

# my_fav_numbers.remove(23)
#you can also do that
# my_fav_numbers = set(list(my_fav_numbers)[:-1])
# print(my_fav_numbers)

# friend_fav_numbers = {1, 4, 21}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

#exercise-2
#no you can't because tuples are immutable

#exercise-3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("kiwi")
# basket.insert(0, "Apples")
# apples = basket.count("Apples")
# basket.clear()
# print(apples)
# print(basket)

#exercise-4
#An integer is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place.
#arange()
# number = 1 
# new_list = []
# for x in range(8):
#     number += 0.5
#     new_list.append(number)
    
# print(new_list)

#exercise-5
# for num in range(21) :
#     if num % 2 == 0 :
#         print(num)
        
#exercise-6
# you can also user_name = ""
# my_name = "raquel"
# while True:       # you can also user_name != my_name
#     user_name = input("what is your name\n")
#     if user_name == my_name:
#         print("we have the same name!")
#         break

#exercise-7
# user_fruits = input("what is your favorite fruit? if you have several ones please separate them with a single space\n")
# list_fruit = user_fruits.split()
# print(list_fruit)
# random_fruit = input("now choose a random fruit\n")
# if random_fruit in list_fruit:
#     print("you choose one of your favorite fruits! enjoy")
# else:
#     print("you choose a new fruit. i hope you enjoy")


# exercise-8
# list_topping = []
# price = 10
 
# while True: 
#     user_topping = input("what would you like as a topping for your pizza? if you feel you put enough topping write 'quit' \n")
#     if user_topping == 'quit': 
#         print("your pizza will be ready in 10 min")
#         prompt = "bye"
#         break
       
#     else:
#         list_topping.append(user_topping)
#         price += 2.5
#         print(f"you added {user_topping} to your pizza")
        
# print(f'you added {" ".join(list_topping)} so your total price is {price}')

#exercise-9
# total_price = 0
# while True:
#     member_family_age = int(input("what is your age?\n"))
#     if member_family_age < 3:
#         total_price += 0
#         print(f"your ticket is free - your total price is {total_price}")
#     elif 3<= member_family_age <= 12:
#         total_price += 10
#         print(f"your ticket will be 10 dollar - your total price is {total_price}")
#     elif member_family_age > 12:
#         total_price += 15
#         print(f"your ticket will be 15 dollar - your total price is {total_price}")

# name_list = ["raquel", "sarah", "hanna"]
# print(name_list)
# while True:
#     teen_name = input("what is your name?")
#     if teen_name in name_list:
#         print("okay lets continue")
#     else:
#         print("you are not on the list")
#         break
#     teen_age = int(input("what is your age"))
#     if not 16 <= teen_age <= 21:
#         name_list.remove(teen_name)
#         print("you are not allowed to enter")
#         print(name_list)
        
        
        
#exercise-10

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# finished_sandwiches = []
# finished_sandwiches.append("Tuna sandwich")
# sandwich_orders.remove("Tuna sandwich")
# finished_sandwiches.append("Pastrami sandwich")
# sandwich_orders.remove("Pastrami sandwich")
# finished_sandwiches.append("Avocado sandwich")
# sandwich_orders.remove("Avocado sandwich")
# finished_sandwiches.append("Pastrami sandwich")
# sandwich_orders.remove("Pastrami sandwich")
# finished_sandwiches.append("Egg sandwich")
# sandwich_orders.remove("Egg sandwich")
# finished_sandwiches.append("Chicken sandwich")
# sandwich_orders.remove("Chicken sandwich")
# finished_sandwiches.append("Pastrami sandwich")
# sandwich_orders.remove("Pastrami sandwich")

# print(sandwich_orders)
# print(finished_sandwiches)

# print(f"i made your Tuna sandwich")
# print(f"i made your Pastrami sandwich")
# print(f"i made your Avocado sandwich")
# print(f"i made your Pastrami sandwich")
# print(f"i made your egg sandwich")
# print(f"i made your Chicken sandwich")
# print(f"i made your Pastrami sandwich")











