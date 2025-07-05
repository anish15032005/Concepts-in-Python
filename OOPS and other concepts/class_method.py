class person:
    name = "Anonymous"
    def changename(self,name):
        self.name = name
        
p1 = person()
p1.changename("John")
print(p1.name)  # Output: John
print(person.name)  # Output: Anonymous (class variable remains unchanged)

#let's see an example of class method which is used to access the class variable.
class Person:
    name = "Anonymous"
    def changename(self,name):
        Person.name = name
        
p2 = Person()
p2.changename("Alice")
print(p2.name)  # Output: Alice
print(Person.name)  # Output: Alice (class variable is changed)


#Another approach
class Person2:
    name = "Anonymous"
    @classmethod
    def changename(cls, name):
        cls.name = name
        
p3 = Person2()
p3.changename("Sophia")
print(p3.name)  # Output: Alice
print(Person2.name)  # Output: Alice (class variable is changed)