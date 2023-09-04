list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1)

position_of_20 = list1.index(20)
print("the position of the number 20 is", position_of_20)
list1[position_of_20] = 200
print(list1)
