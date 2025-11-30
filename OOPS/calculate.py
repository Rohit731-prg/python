# create a class for claculator

class calculator:
    def __init__(self, num1: int, num2: int) -> None:
        self.num1 = num1
        self.num2 = num2

    def addtion(self) -> int:
        return self.num1 + self.num2
    
    def subtraction(self) -> int:
        return self.num1 - self.num2
    
    def multiplication(self) -> int:
        return self.num1 * self.num2

    def divition(self) -> int:
        return self.num1 // self.num2

    def modulas(self) -> int:
        return self.num1 % self.num2
    
    def __del__(self):  # destructor call autometic after finishing task..
        print("Task finished..")

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
c1 = calculator(num1, num2)
print("\nAddition: \t", c1.addtion())
print("subtraction: \t", c1.subtraction())
print("multiplication: ", c1.multiplication())
print("divition: \t", c1.divition())
print("modulas: \t", c1.modulas())