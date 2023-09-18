import math
#exercise-1
class Circle:
    
    def __init__(self, radius = 1.0):
        self.radius = radius
        
    def calculate(self):
        area_circle = math.pi * self.radius **2
        return area_circle
    
    @staticmethod
    def defition_circle():
        print("A circle is a set of all points equidistant from a central point.")

#exercise-2
class Mylist:
    
    def __init__(self, mylist):
        self.mylist = mylist
        
    def reverse_li(self):
        list1 = mylist.reverse()
        return list1
    
    def order_li(self):
        return sorted(self.mylist)
                       
mylist = Mylist([1, 5, 3, 2, 8, 9, 7])

print(mylist.reverse_li())
print(mylist.order_li())

#exercise-3
class MenuManager:
    
    def __init__(self):
        self.menu = [
            {'name': 'Soup', 'price': 10, 'spice': 'B', 'gluten': False},
            {'name': 'Hamburger', 'price': 15, 'spice': 'A', 'gluten': True},
            {'name': 'Salad', 'price': 18, 'spice': 'A', 'gluten': False},
            {'name': 'French Fries', 'price': 5, 'spice': 'C', 'gluten': False},
            {'name': 'Beef bourguignon', 'price': 25, 'spice': 'B', 'gluten': True}
        ]
        
    def add_items(self, name, price, spice, gluten):
        new_dish = {"name" : name, "price" : price, "spice" : spice, "gluten" : gluten}
        self.menu.append(new_dish)
        
    def update_itemd(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
        else:
            print("the dish is not on the menu")
        return self.menu
            
    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
              self.menu.remove(dish)
        else:
            print("this dish is not in the menu")
        return self.menu
            
manager = MenuManager()
        
    