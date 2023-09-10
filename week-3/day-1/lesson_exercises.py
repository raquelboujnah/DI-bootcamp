class Dog :

    def __init__(self, dog_name, dog_age, dog_color = "black", dog_energy = 100,) :
        self.name = dog_name
        self.age = dog_age
        self.color = dog_color
        self.energy = dog_energy
        # nb energypoints

    # method happybirthday increment the age by one
    def happy_birthday(self) :
        self.age += 1

    def show_info (self) :
        print(f"The dog name is {self.name}, his age is {self.age}, he is of color {self.color}")

    def go_to_groomer(self, owner_color) :
        self.color = owner_color


    def play (self, activity) :
        if activity == "ball":
            self.energy -= 10
        elif activity == "frisbee":
            self.energy -= 30
        elif activity == "another dog":
            self.energy -= 70
        if self.energy == 0:
            self.sleep()
            
    
    def sleep(self):
        self.energy = 100
        print("the dog has to sleep to bring back his energy to 100")    


lea_dog = Dog("Spock", 2,)
lea_dog.go_to_groomer("pink")
lea_dog.show_info()
# print(lea_dog.__dict__)

dan_dog = Dog("Rex", 4, "white")
# print(dan_dog.__dict__)
dan_dog.show_info()

# def play (self, activity) : ##we open a new function with self to be unique for each dog and a parameter activity to disign the dog's activity
#         if self.energy >= 10: ## if the dog's energie is equal or more to 10 then he can play
#             if self.energy >= 10 and activity == "ball" : ##if the dog's energie is equal or more to 10 and he want to play ball 
#                 self.energy -= 10 ##then we will dicrease 10 from his energy
#                 print(f"{self.name} is playing ball - he has {self.energy} energy left")
#             elif self.energy >= 30 and activity == "frisbee":
#                 self.energy -= 30
#                 print(f"{self.name} is playing frisbee - he has {self.energy} energy left")
#             elif self.energy >= 70 and activity.energy >= 70 and isinstance(activity, Dog) :
#                 self.energy -= 70 #lea_dog energy
#                 activity.energy -= 70 #activity is dan_dog
#                 print(f"{self.name} and {activity.name} are playing together - {self.name} has {self.energy} energy left - - {activity.name} has {activity.energy} energy left")
#             else :
#                 print(f"You have {self.energy} left - You don't have enough energy to play {activity} \n")
#                 self.play(input("Please choose another activity between ball, frisbee and play date \n"))
#         else :
#             self.sleep()


# Exercise 1 : Basic Classes
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary

# 1. Create 2 users object and display their attribute
# - Lea Smith 30 years old developer 25000 shekels
# - David Schartz 20 years old project manager 20000 shekels

# 2. Add those methods to the class
# - get_fullname(self) : that return the firstname + lastname
# - (self) : that return the age incremented by one
# - get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# - show_info(self) : that will print the information of the employee --> name, age, job, salary

# 3. Call all the methods on the 2 objects

class Employee:
    
    def __init__(self, user_firstname, user_lastname, user_age, user_job, user_salary):
        self.firstname = user_firstname
        self.lastname = user_lastname
        self.age = user_age
        self.job = user_job
        self.salary = user_salary
        
    def get_fullname(self):
        return self.firstname + self.lastname

    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, promotion_amout):
        self.salary += promotion_amout
    
    def show_info(self):
        print(f"hi ma name is {self.get_fullname()} im {self.age} my job is {self.job} and my salary is {self.salary} ")
        

    
employee_1 = Employee("Raquel", "Boujnah", 22, "developer", 10000)
employee_2 = Employee("Pamela", "Sousa", 21, "developer", 15000)
    