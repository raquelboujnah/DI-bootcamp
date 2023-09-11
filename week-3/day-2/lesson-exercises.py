# class Employee :
#     def __init__(self, firstname, lastname, age, job, salary):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.job = job
#         self.salary = salary
    
#     def get_fullname(self) :
#         return f"{self.firstname} {self.lastname}"
    
#     def happy_birthday(self):
#         self.age += 1
    
#     def get_promotion(self, new_promotion) :
#         self.salary += new_promotion

#     def show_info (self) :
#         print(f"{self.get_fullname()} is {self.age} years old, his job is {self.job} and his salary is {self.salary}")
    
    
# import random
    
# def random_person():
#     lst_names = ["John", "Lea", "Emma", "Josh", "Eli"]
#     lst_lastnames = ["Cohen", "Smith", "Doe", "Sevi", "Swtazh"]
#     lst_jobs = ["developer", "dancer", "cowboy", "tennis player", "doctor"]
#     list_employee = []
#     for _ in range(10):
#         fst_name = random.choice(lst_names)
#         last_name = random.choice(lst_lastnames)
#         job = random.choice(lst_jobs) 
#         age = random.randint(18, 67)
#         salary = random.randint(10000, 45000)
#         person = Employee(fst_name, last_name, age, job, salary)
#         person.show_info()
#         list_employee.append(person)
# random_person()

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
    
# Using the Employee class of yesterday

# 1. Create a Developer class, that inherits from the Employee class with the attributes :
# - firstname, lastname, age,
# - job is developer as default,
# - salary is 15000 by default,
# - coding skills (a list by default) : all developers should start with an empty list of skills

# 2. Create 2 developers objects and display their attribute
# - Tom Cruiz 30 years old
# - Angelina Jolie 23 years old

# 3. Add those methods to the class

# - add_skills(self, *skills) : receives a tuple of skills and append them to the coding skills list
# - coding(self) : print a nice sentence with all the coding languages the developer knows
# - coding_with_partner(self, other_developer) : print a nice sentence with the name of both developers, and their skills
# - override the get_promotion(self, promotion_amount) : that multiplies the salary of the user by the promotion

# 4. Call all the methods, also those from the Employee Class



class Developer(Employee):
    
    def __init__(self, user_firstname, user_lastname, user_age):
        super().__init__(user_firstname, user_lastname, user_age, "developer", 1500)
        self.coding_skills = []

    def add_skills(self, *skills):
        self.coding_skills.extend(skills)
        
    def coding(self):
        print(f"{super().get_fullname()} coding skills are {', '.join(self.coding_skills)}")
        
    def coding_with_partner(self, other_developer):
        self.coding()
        other_developer.coding()
       
developer_1 = Developer("Tom", "Cruiz", 30)
developer_2 = Developer("Angelina", "Jolie", 23)

developer_1.add_skills("Javascript")
developer_2.add_skills("Python", "React")


developer_1.coding_with_partner(developer_2)   