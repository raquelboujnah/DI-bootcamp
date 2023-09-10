#exercise-1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# def oldest_cat(list_cat):
#     oldest_cat = list_cat[0]
#     for cat in list_cat:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     print(f"the oldest cat is {oldest_cat.name} and is {oldest_cat.age}")  
              
# cat_1 = Cat("miaou", 2)
# print(cat_1.age)
# cat_2 = Cat("minou", 4)
# cat_3 = Cat("greg", 3)

# list_cat = [cat_1, cat_2, cat_3]

# oldest_cat(list_cat)


# exercise-2
# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height
        
#     def bark(self):
#         print(f"{self.name} goes wouf!")
        
#     def jump(self):
#         print(f"{self.name} jump {(self.height * 2)} cm hight")
 
# def bigger_dog(list_dog):
#     big_dog = list_dog[0]
#     for dog in list_dog:
#         if dog.height > big_dog.height:
#             big_dog = dog
#     print(f"the bigger dog is {big_dog.name} and is {big_dog.height} cm high")  
    

# david_dog = Dog("Rex", 50)
# sarah_dog = Dog("teacup", 20)
# list_dog = [david_dog, sarah_dog]

# print(f"{david_dog.name} is {david_dog.height} cm high")
# david_dog.bark() 
# david_dog.jump()

# print(f"{sarah_dog.name} is {sarah_dog.height} cm high")
# sarah_dog.bark() 
# sarah_dog.jump()

# bigger_dog(list_dog)


#exercise-3
# class Song:
#     def __init__(self, lyrics:list):
#         self.lyrics = lyrics
        
#     def sing_me_a_song(self):
#         for item in self.lyrics:
#             print(item)
        
# stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
# stairway.sing_me_a_song()

#exercise-4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = [] 
    
    def add_animal(self, *new_animals):
        for new_animal in new_animals:
            self.animals.append(new_animal)
        
    def get_animal(self):
        print(f"{' '.join(self.animals)}")
        
    def sell_animal(self, sold_animal):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)
        
    def sort_animal(self):
        group_animals = {}
        sorted_animals = sorted(self.animals)
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in group_animals:
                group_animals[first_letter] = []
            group_animals[first_letter].append(animal)

        return group_animals
    
    def get_group(self):
        group_dict = {}
        group = self.sort_animal()
        for i, item in enumerate(group):
            group_dict[i + 1] = group[item]
        return group_dict
            
ramat_gan_safari = Zoo("ramat_gan")
ramat_gan_safari.add_animal("girafe", "turtle", "lion", "baboon", "bear")
ramat_gan_safari.get_animal()
s_animal = ramat_gan_safari.sort_animal()
print(s_animal)
print(ramat_gan_safari.get_group())

