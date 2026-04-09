# multipale inheritence

class Base1:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    
class Base2:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
 
    def subtraction(self):
        return self.num1 - self.num2
    
class Child(Base1, Base2):
    def __init__(self, num1, num2) -> None:
        Base1.__init__(self, num1, num2)
        Base2.__init__(self, num1, num2)

    def addition(self):
        return Base1.addition(self)
    
    def subtraction(self):
        return Base2.subtraction(self)
    
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
ob = Child(num1, num2)
add = ob.addition()
sub = ob.subtraction()

print("Addition is : ", add)
print("Subtraction is : ", sub)