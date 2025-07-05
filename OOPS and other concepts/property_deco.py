# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.avg = (self.phy + self.chem + self.math)/3
        
# stu1 = Student(80, 90, 85)
# print(stu1.avg)  # Output: 85.0

# stu1.phy = 95
# print(stu1.avg)  # Output: 85.0 (average is not updated)


class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.avg = (self.phy + self.chem + self.math)/3
    def calc_avg(self):
        self.avg =  (self.phy + self.chem + self.math)/3
        return self.avg
    
st1 = Student(80, 90, 85)
print(st1.calc_avg())  # Output: 85.0

st1.phy = 95
print(st1.calc_avg())  # Output: 90.0 (average is updated)



#we use property decorator on any method in the case to use the method as a property
class Student2:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.avg = (self.phy + self.chem + self.math)/3
    # def calc_avg(self):
    #     self.avg =  (self.phy + self.chem + self.math)/3
    #     return self.avg
    @property
    def percentage(self):
        return (self.phy + self.chem + self.math)/3


st2 = Student2(80, 90, 85) 
print(st2.percentage)  # Output: 85.0

st2.phy = 95
print(st2.percentage)  # Output: 90.0 (average is updated)