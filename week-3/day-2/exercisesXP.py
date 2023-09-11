##exercise-1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
  
# cat_1 = Bengal("miaou", 2)  
# cat_2 = Chartreux("chocolat", 3) 
# cat_3 = Siamese("noisette", 1) 
# all_cats = [cat_1, cat_2, cat_3]
# sara_pets = Pets(all_cats)
# sara_pets.walk()


##exercise-2
class Dog:
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        print(f"{self.name} is barking")
    
    def run_speed(self):
        self.runing_speed = (self.weight/self.age*10)
        return self.runing_speed

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f"{self.name} is the winner")
        else:
            print(f"{other_dog.name} is the winner")
    
dog_1 = Dog("milki", 10, 12)
dog_2 = Dog("momo", 5, 7)
dog_3 = Dog("marko", 9, 9)
dog_1.bark()
dog_2.bark()
dog_3.bark()
dog_1.fight(dog_2)
