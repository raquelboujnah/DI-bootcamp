class MenuItems:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.items = {}
        
    def delete(self):
        self.items.remove(self)
        
    def save(self):
        self.items[self.name] = [self.price]
        
    def update(self, name, price):
        if name in self.items.keys():
            return
        else:
            self.items[name] = price
           
        if price in self.items.values():
            return
        else:
            self.items[name] = price 
    
          
        