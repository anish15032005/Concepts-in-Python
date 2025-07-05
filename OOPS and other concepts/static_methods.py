#Static methods are those who don't use self parameter
#They are used when we don't need to access any instance or class variables
#They work at class level

class Student:
    
    def __init__(self, name):
        self.name = name
    
    
    @staticmethod
    def college():
        print("College of Engineering and Technology")
        
        
# Example usage
s1 = Student("Alice")
print(s1.name)
s1.college()  # Calling static method using instance
