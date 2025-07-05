class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (22/7)*self.radius*self.radius
    def perimeter(self):
        return 2*(22/7)*self.radius
    
    
    
    
c1 = Circle(21)
print(c1.area())  # 1386
print(c1.perimeter())  # 132.0