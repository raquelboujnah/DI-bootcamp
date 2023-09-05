fruits = ["apple","pear", "banana"]
# print(fruits[0])

# fruits[0] += "s"
# print(fruits)
# [0,1,2]

for num in range(len(fruits)):
    fruits[num] += "s"

print(fruits)

# print(list(enumerate(fruits)))
# [(0, 'apple'), (1, 'pear'), (2, 'banana')]

for index,value in enumerate(fruits):
    fruits[index] += "s"

print(fruits)

# 1st loop
# index = 0
# value = "apple"
# fruits[index] += "s"
# --> fruits[0] += "s"
# -->


# for value in fruits:
#     print(value)

# print(fruits)


fruits = ["apple", "banana", "pear"]
prices = [1.3, 0.5, 1.6]
colors = ["red", "yellow", "red"]

all = zip(fruits, prices, colors)

print(list(all))

all2 = zip(fruits, prices)
dict1 = dict(all2)
print(dict1)
# {'apple': 1.3, 'banana': 0.5, 'pear': 1.6}


employees = [
    {
        "username" : "Jon",
        "monthly_salary" : 2000
    },
    {
        "username" : "Emma",
        "monthly_salary" : 5000
    },
    {
        "username" : "Paul",
        "monthly_salary" : 1300
    }
]

high_salary_people = [person["username"] for person in employees if person["monthly_salary"] > 1500]
print(high_salary_people)

# Syntax
# [what_to_add for_loop condition]