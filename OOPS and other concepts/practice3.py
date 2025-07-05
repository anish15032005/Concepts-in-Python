#a class order which stores items and their prices
class Order:
    def __init__(self,item, price):
        self.item = item
        self.price = price
    def __gt__(self,ord2):
        return self.price > ord2.price
        
        
order1 = Order("Cookie", 20)
order2 = Order("Cake", 50)
print(order1 > order2)  # False, because 20 is not greater than 50
print(order2 > order1)  # True, because 50 is greater than 20