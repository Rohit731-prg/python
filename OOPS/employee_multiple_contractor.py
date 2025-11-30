# create a employee class with 2 constractor

class employee:
    def __init__(self) -> None:
        self.name = input("Enter Employee name: ")
        self.age = int(input("Enter Employee age: "))

    def display(self) -> None:
        print("Employee name: ", self.name)
        print("Employee age: ", self.age)

    def __del__(self): # calls 2 times..
        print("Task complite")

e1 = employee()
e1.display()

e2 = employee()
e2.display()