#exercise-1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# new_list = zip(keys, values)
# print(dict(new_list))

#exercise-2
# total = 0
# names = input("give a name and separated by a space").split()
# ages = input("give me your ages seperated by a space").split()
# zip_family = zip(names, ages)
# family = dict(zip_family)


# for age in family.values():
#     if int(age) < 3:
#         total += 0
#     elif 3 <= int(age) <= 12:
#         total += 10
#     elif int(age) > 12:
#         total += 15
        
# print(f'{total} is the total')

#exercise-3
magasin = {
    'name' : 'Zara',
    'creation date' : 1975,
    'creator name' : 'Amancio Ortega Gaona',
    'type of clothes' :['men', 'women', 'children', 'home'],
    'international competitors': ['Gap', 'H&M', 'Benetton'],
    'number stores' : 7000,
    'major color' :{
        'France' : 'blue',
        'spain' : 'red',
        'US' : ['pink', 'green']
    }
        
}

#magasin['number stores'] = 2
#print(f'zara clients are mostly {" ".join(magasin["type of clothes"][:-1])}')
#magasin['contry creation'] = 'spain'
# if 'international competitors' in magasin.keys():
#     magasin['international competitors'].append("Desigual")
#del magasin['creation date']
#print(magasin['international competitors'][-1])
#print(magasin['major color']['US'])
#print(len(magasin))
#print(magasin.keys())

# more_on_zara = {
#     'creation date': 1975,
#     'number stores' : 10000
# }
#magasin.update(more_on_zara)
#print(magasin['number stores'])
##it changes the value to the value of the second dictionary

#exercise-4
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#for index,value in enumerate(fruits):
    #fruits[index] += "s"

# disney_users_a = {name: index for index, name in enumerate(users)}
# print(disney_users_a)

# disney_users_b = {index: name for index, name in enumerate(users)}
# print(disney_users_b)

# new_list = sorted(users)
# disney_users_c = {name: index for index, name in enumerate(new_list)}
# print(disney_users_c)

# disney_users_d = {name: index for name, index in disney_users_a.items() 
#                   if 'i' in name
#                   if name[0] in ('M', 'P')
#                   }
# print(disney_users_d)



