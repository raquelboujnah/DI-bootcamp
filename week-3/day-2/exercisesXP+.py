##exercise-1
class Family:
    
    def __init__(self, last_name):
        self.members = [{'name':'Michael','age':35,'gender':'Male','is_child':False},
                        {'name':'Sarah','age':32,'gender':'Female','is_child':False}]
        self.last_name = last_name

    def born(self, **child):
        self.members.append(child)
        print("Congrats!!")
        print(self.members)
        
    def is_18 (self, name):
        for member in self.members:
            if member['name'] == name and member['age'] >= 18:
                return True
            else:
                return False
            
    def family_presentation(self):
        for member in self.members:
            print(f"{self.last_name} {member['name']}")
        
    
# family_1 = Family("Boujnah")
# family_1.born(name = 'Marie', age = 0, gender = 'Female', is_child  = True)
# family_1.family_presentation()
        

##exercise-2
class TheIncredibles(Family):
    
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]
        
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name and member['age'] >= 18:
                print(f"{member['power']}")
            else:   
                print("you are not 18")
                
    def incredible_presentation(self):
        super().family_presentation()
        for member in self.members:
            print(f"{member['power']} {member['name']}")
    

        
family_2 = TheIncredibles("Israel")
family_2.use_power("Michael")
print(family_2.incredible_presentation())
family_2.born(name ='jack', age = 0, gender = 'Male', is_child = True, power = 'Unknow Power', incredible_name = 'BabyJack')
print(family_2.incredible_presentation())

        
    