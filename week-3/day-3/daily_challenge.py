import math
class Circle:
    
    def __init__(self, diameter = None, radius = None):
        if diameter is not None:
            self.diameter = diameter / 2
        elif radius is not None:
            self.radius = radius 
        
    def set_radius(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def set_diameter(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2
        
    def caculate_area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        if self.diameter is not None:
            return f"the circle is based on a diameter of {self.diameter}"
        elif self.radius is not None:
            return f"the circle is based on a radius of {self.radius}"
        
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(radius = new_radius)
    
    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

circle1 = Circle(diameter = 4)
circle2 = Circle(radius = 6)
circle1.set_diameter(4)
print(circle1.__str__())
circle2.set_radius(6)
print(circle2.__str__())
print(circle1.caculate_area())
print(circle2.caculate_area())
circle3 = circle1 + circle2
print(circle3.radius)
print(circle2.__gt__(circle1))




        