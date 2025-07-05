#Abstraction means hiding the implementation details and showing only the essential features of the object.
#Abstraction can be achieved by using abstract classes and interfaces.

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clct = False
        
    
    def start(self):
        self.acc = True
        self.clct = True
        print("Car started....")
        
car1 = car()
car1.start()