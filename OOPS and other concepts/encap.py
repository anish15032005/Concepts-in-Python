#Encapsulation means hiding the internal state and requiring all interaction to be performed through an object's methods.
# Encapsulation can be achieved by using private variables and methods.
#it is writing data and functions together in a single unit called class.

class Account:
    def __init__(self,balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print(f"Debited {amount}. New balance: {self.balance}") 
    #credit method
    def credit(self,amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")
        
    #get_balance method
    def get_balance(self):
        return self.balance       
acc1 = Account(1000, 123456789)
acc1.debit(100)
acc1.credit(200)
print(f"Account balance: {acc1.get_balance()}")  # Accessing balance through method