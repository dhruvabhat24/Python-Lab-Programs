import math
class Shape:
    def __int__(self):
        pass
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self,base,height):
        super().__init__()
        self.base=base
        self.height=height
        def area(slef):
            return 0.5*self.base*self.height
class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    
t=Triangle(10,20)
print("Area of Triangle:",t.area())
c=Circle(10)
print("Area of Circle:",c.area())
r=Rectangle(10,20)
print("Area of Rectangle:",r.area())
