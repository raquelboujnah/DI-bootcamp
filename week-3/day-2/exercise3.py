from exercisesXP import Dog 
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__( name, age, weight)
        self.trained = trained
        
    def train(self):
        self.bark()
        self.trained = True
    
    def play(self, *dogs):
        print(f"{self.name}, {', '.join(dogs)} all play together")
    
    def do_a_trick(self):
      list_print = ["stands on his back legs", "shakes your hand", "plays dead", "does a barrel roll"]
      if self.trained == True:
          choice = random.choice(list_print)
          print(f"{self.name} {choice}")
          
my_dog_1 = PetDog("momo", 10, 6)
my_dog_2 = PetDog("momi", 2, 4)
my_dog_3 = PetDog("momu", 12, 8)
my_dog_1.train()
my_dog_1.do_a_trick()



