
class Farm:
    def __init__(self, name):
        self.name = name
        self.list_animal = {}
        
    def add_animal(self, animal, amount = 1):
        if animal in self.list_animal:
            self.list_animal[animal] += amount
        else:
            self.list_animal[animal] = amount
        
        
    def get_info(self):
        print(f"{self.name}'s farm \n\n")
        for animal, amount in self.list_animal.items():
           print(f"{animal} : {amount}")
        print("\n \n E-I-E-I-0!")
    
    def get_animal_types(self):
        list_types = list(self.list_animal.keys())
        return list_types
        
    def get_short_info(self):
        print(f"{self.name}'s farm has {macdonald.get_animal_types()[0]}s, {macdonald.get_animal_types()[2]}s and {macdonald.get_animal_types()[1]}")
        
        


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_animal_types()
macdonald.get_short_info()
