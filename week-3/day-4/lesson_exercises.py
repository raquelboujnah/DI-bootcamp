class Employee:
    
    def __init__(self, user_firstname, user_lastname, user_age, user_job, user_salary, adress):
        self.firstname = user_firstname
        self.lastname = user_lastname
        self.age = user_age
        self.job = user_job
        self.salary = user_salary
        self.__adress = adress
        
    def get_fullname(self):
        return self.firstname + self.lastname

    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, promotion_amout):
        self.salary += promotion_amout
    
    def show_info(self):
        print(f"hi ma name is {self.get_fullname()} im {self.age} my job is {self.job} and my salary is {self.salary} ")
    
    @property
    def adress(self):
        return self.__adress
    
    @adress.setter
    def adress(self, new_adress):
        if self.job == "developer":
            self.__adress = new_adress
            
emp1 = Employee("Raquel", "Boujnah", 22, "developer", 15000, "hahela 4")
print(emp1.adress)
emp1.adress = "hadera 4"
print(emp1.adress)