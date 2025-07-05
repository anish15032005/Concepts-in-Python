class Employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.dept}, Salary: {self.sal}")
        
e1 = Employee("Software Engineer", "IT", 60000)
e1.showDetails()  # Role: Software Engineer, Department: IT, Salary: 60000
e2 = Employee("Data Scientist", "Analytics", 80000)
e2.showDetails()  # Role: Data Scientist, Department: Analytics, Salary: 80000

#let's create an Engineer class that inherits from Employee but it has an additional attribute for name and age
class Engineer(Employee):
    def __init__(self, role, dept, sal, name, age):
        self.name = name 
        self.age = age
        super().__init__(role, dept, sal)
        
    def showDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Department: {self.dept}, Salary: {self.sal}")
        
e3 = Engineer("Software Engineer", "IT", 60000, "Alice", 30)
e3.showDetails()  # Name: Alice, Age: 30, Role: Software

