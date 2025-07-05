class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account(101, "pass123")
print(acc1.acc_no)  # This will work, as acc_no is public
# print(acc1.__acc_pass)  # This will raise an AttributeError, as __acc_pass is private

acc1.reset_pass()  # This will work, as reset_pass can access the private attribute  

class person:
    __name = "Sanjay"
    def __hello(self):
        print("Hello")
    def welcome(self):
        self.__hello()
    
p1 = person()
# print(p1.__name)  # This will raise an AttributeError, as __name is private
# print(p1.__hello()) # This will raise an AttributeError, as __hello is private

p1.welcome()  # This will work, as welcome can access the private method __hello