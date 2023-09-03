# my_age = 22

# sentence = str(my_age) + "is ma age"

# in_123879 = my_age + 123879

# sentence_two = f"you will be {in_123879}"

# print(sentence)
# print(sentence_two)

# first_name = "raquel"
# last_name = "boujnah"
# full_name = first_name + " " + last_name 
# sentence_three = f"my full name is {first_name} {last_name}"
# print(sentence_three)


user_choice = int(input("how much miles \n" ))
km = user_choice *2
print(km)

name = 'John Doe'
if len(name) > 20:
    print(f"Name '{name}' is more than 20 chars long")
    length_description = 'long'
elif len(name) > 15:
    print(f"Name '{name}' is more than 15 chars long")
    length_description = 'semi long'
elif len(name) > 10:
    print(f"Name '{name}' is more than 10 chars long")
    length_description = 'semi long'
elif 10>= len(name) >=8:
    print(f"Name '{name}' is 8, 9 or 10 20 chars long")
    length_description = 'semi short'
else: 
    print(f"Name '{name}' is a short name")
    length_description = 'short'
