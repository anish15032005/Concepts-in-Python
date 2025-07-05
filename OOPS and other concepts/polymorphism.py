#let's get the concept with an example of polymorphism
print(1+3)  # integer addition
print("Hello " + "World")  # string concatenation
print([1, 2] + [3, 4])  # list concatenation

print(type(1)) # <class 'int'>
#so, basically the class int has a method __add__ that is called when we use the + operator
#same goes for string and list
#this is called implicit polymorphism


#let's do with this our own classes
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")
    # def add(self,num2):
    #     newReal = self.real+num2.real 
    #     newImg = self.imag + num2.imag
    #     return Complex(newReal,newImg)     
    #let's define a dunder method __add__ to allow using the + operator
    def __add__(self,num2):
        newReal = self.real+num2.real 
        newImg = self.imag + num2.imag
        return Complex(newReal,newImg)     
    def __sub__(self,num2):
        newReal = self.real-num2.real 
        newImg = self.imag - num2.imag
        return Complex(newReal,newImg)     
num1 = Complex(1, 2)
num1.showNumber()  # 1i + 2j

num2 = Complex(3, 4)

# num3 = num1.add(num2)
# num3.showNumber()  # 4i + 6j

# num4 = num1 + num2  # this will not work, we need to define __add__ method

num3  = num1 + num2  # now this works because we defined __add__
num3.showNumber()  # 4i + 6j

num4 = Complex(5, 6)
num5 = num4 - num3  # using __sub__ method
num5.showNumber()  # 1i + 0j