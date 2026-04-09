# simple inheritence

class BaseClass:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

class ChildClass(BaseClass):
    def __init__(self, num1, num2):
        BaseClass.__init__(self, num1, num2)

    def add(self) -> int:
        return self.num1 + self.num2


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
ob = ChildClass(num1, num2)
result = ob.add()
print("Addition is: ", result)