# class student:
#     name = "Sanjay"
#     occupation = "Soldier"
    

# s1 = student()
# print(s1.name)
# print(s1.occupation)


#All classes has a function called __init__ which is called when the class is created


#the self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# class student:
#     name = "Sanjay"
#     def __init__(self):#baiscally, we are calling our object self
#         print("This is the init function")
#         print(self.name)
        
# s1 = student()
# print(s1.name)





#This implementation is not valid, as it will not allow us to create multiple instances with different names and occupations.
# class student:
#     #this is parameterized constructor
#     #called when the class is created
#     def __init__(self):
#         pass
    
#     #this is parameterized constructor
#     def __init__(self, name, occupation):
#         self.name = name
#         self.occupation = occupation
#         print("Adding new person in database....")
      
class student:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        print("Adding new person in database....")
 
     
s1 = student("Sanjay", "Soldier")
s2 = student("Ravi", "Engineer")