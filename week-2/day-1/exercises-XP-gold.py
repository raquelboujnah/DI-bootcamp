#exercise-1
print("hello world \n" " "*4 ,"i love python\n" " "*4)

#exercise-2
user_month = int(input("choose a month by typing a number between 1-12\n"))
if 3 <= user_month <= 5:
    print("the month you choose is in the spring")
elif 6 <= user_month <= 8:
    print("the month you choose is in the summer")
elif 9 <= user_month <= 11:
    print("the month you choose is in the autumn")
elif user_month == 12:
    print("the month you choose is in the winter")
elif 1 <= user_month <= 2:
    print("the month you choose is in the winter")
    
