# class Employee:
    
#     def __init__(self, user_firstname, user_lastname, user_age, user_job, user_salary):
#         self.firstname = user_firstname
#         self.lastname = user_lastname
#         self.age = user_age
#         self.job = user_job
#         self.salary = user_salary
        
#     def get_fullname(self):
#         return self.firstname + self.lastname

#     def happy_birthday(self):
#         self.age += 1
    
#     def get_promotion(self, promotion_amout):
#         self.salary += promotion_amout
    
#     # def show_info(self):
#     #     print(f"hi ma name is {self.get_fullname()} im {self.age} my job is {self.job} and my salary is {self.salary} ")
    
#     def __gt__(self, other_emp):
#         if self.salary > other_emp.salary:
#             return self
#         else:
#             return other_emp
        
#     def __add__(self, other_emp):
#         return self.salary + other_emp.salary
    
#     def __str__(self):
#         return f"{self.get_fullname()} is {self.age} he is a {self.job} and he urn {self.salary} shekel"
                
# employee_1 = Employee("Raquel", "Boujnah", 22, "developer", 10000)
# employee_2 = Employee("Pamela", "Sousa", 21, "developer", 15000)
# print(employee_1 > employee_2)
# print(employee_1 + employee_2)

# Using the Employee class

# implement the gt dunder method that receives 2 different employees, and returns the employee with the highest salary

# implement the add dunder method that that receives 2 different employees, and returns the total salary of the 2 employees

# implement the str dunder method that introduce the employee

# Call all the methods

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
    
    @classmethod
    def create_best_employee(cls, salary):
        if salary > 30000:
            return cls("Ezra", "Israel", 22, "developer", salary)
            
        
# Using the Employee class
# implement a method create_best_employee that should create a new employee only if their salary is > 30000 --> class method
best_employee = Employee.create_best_employee(40000)
best_employee.show_info()