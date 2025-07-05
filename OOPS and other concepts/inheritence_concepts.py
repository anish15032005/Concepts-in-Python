#when one class(child/derived) derives the properties & methods of another class(parent/base) is called inheritance.
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("Car stopped")
    
    
class ferrari(Car):
    def __init__(self, brand, type):
        super().__init__(type)  # calling parent class constructor
        self.brand = brand
        
    

car1 = ferrari("Ferrari F8","Diesel")
car1.start()  # Inherited method from Car class

#The upper one is an example of single inheritance where the child class `ferrari` inherits from the parent class `Car`.
# In Python, a class can inherit from multiple classes, which is known as multiple inheritance.


#here is an example of multi-level inheritance where `ferrari` inherits from `Car`, and `purosangue` inherits from `ferrari`.
class purosangue(ferrari):
    def __init__(self, brand):
        self.brand = brand
        super().start()  # calling start method from Car class
        
car2 = purosangue("2025F5")
car2.start()  # Inherited method from Car class

#let's see an example of multiple inheritance where a class can inherit from multiple parent classes.
class a:
    varA = "Variable A"
    
class b:
    varB = "Variable B"
    
class c(a, b):
    varC = "Variable C"
c1 = c()
print(c1.varA)  # Output: Variable A
print(c1.varB)  # Output: Variable B
print(c1.varC)  # Output: Variable C


#Let's see an example of super() function which is used to call the parent class methods.

car3 = ferrari("Ferrari F8","Electric")
print(car3.type)  # Output: Electric