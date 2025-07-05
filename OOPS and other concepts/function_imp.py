class Student:
    def __init__(self, name, hometown, age):
        self.name = name
        self.hometown = hometown
        self.age = age
    college = "IIEST Shibpur"
    def display_info(self):
        print(f"{self.name} who is {self.age} years old from {self.hometown} is studying at {self.college}")
        
        
        
s1 = Student("Anish","Forbesganj", 20)
s1.display_info()

s2 = Student("Rohan", "Purulia", 20)
s2.display_info()