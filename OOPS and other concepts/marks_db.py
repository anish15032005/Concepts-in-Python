class student:
    def __init__(self, name, maths, phy, chem):
        self.name = name
        self.maths = maths
        self.phy = phy
        self.chem = chem
        
    def avg(self):
        return(self.maths + self.phy + self.chem) / 3
    
    def show_marks(self):
        print(f"Hey {self.name}, your marks are:")
        print(f"Maths: {self.maths}")
        print(f"Physics: {self.phy}")
        print(f"Chemistry: {self.chem}")
        print(f"Average: {self.avg()}\n")
        
s1 = student("Alice", 85, 90, 88)

# s1.show_marks()


#another approach
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def avg(self):
        return sum(self.marks) / len(self.marks)
    def Show_marks(self):
        print(f"Hey {self.name}, your marks are:")
        for subject, mark in zip(["Maths", "Physics", "Chemistry"], self.marks):
            print(f"{subject}: {mark}")
        print(f"Average: {self.avg()}\n")
        
    
s2 = Student("Tony Stark",[88,95,99])
s2.name = "Robert Downey Jr."
s2.Show_marks()