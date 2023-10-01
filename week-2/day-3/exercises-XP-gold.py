#exercise-1 + 2 + 3
# birthdays = {
#     "raquel" : "22/08/2001",
#     "ezra" : "21/09/2001",
#     "elliot" : "23/08/2007",
#     "judith" : "29/12/1996",
#     "lea" : "25/01/1994"
# }

# add_name = input('Would you like to add some name to your friend list? type a name: \n')
# if add_name in birthdays.keys():
#     print(f'your already added this friend his birthday is {birthdays[add_name]}')
# else:
#     add_bd = input('now add his birthday (YYYY/MM/DD): \n')
#     birthdays[add_name] = add_bd
# print(list(birthdays))
# user_bd_name = input("here you can look over for the birthday of your friends, name a friend\n")
# if user_bd_name in birthdays.keys():
#     print(f"{user_bd_name} is {birthdays[user_bd_name]}'s birthday")    
# else:
#     print(f"sorry you didn't added {user_bd_name} to your friend list")

#exercise-4
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
print(f'the banana is {items["banana"]}$, the apple is {items["apple"]}$, the orange is {items["orange"]}$ and the pear is {items["pear"]}$')


items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0
for item_name, item_info in items.items():
    price = item_info["price"]
    stock = item_info["stock"]
    cost = price * stock
    total_cost += cost

print(f"The total cost to buy everything in stock is ${total_cost}")