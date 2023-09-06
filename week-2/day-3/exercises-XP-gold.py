#exercise-1
birthdays = {
    "raquel" : "22/08/2001",
    "ezra" : "21/09/2001",
    "elliot" : "23/08/2007",
    "judith" : "29/12/1996",
    "lea" : "25/01/1994"
}
user_name = input("type a name")
user_date = input("type his birthdate")
birthdays[user_name] = user_date
print(list(birthdays.keys()))
user_bd_name = input("here you can look over for the birthday of your friends, name a friend\n")
for name,bd in birthdays.items():
    if user_bd_name in name:
        print(f"{bd} is {name}'s birthday")
        
    else:
        print(f"sorry you didn't added {name} to your friend list")
        
