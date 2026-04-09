# multi - level inheritence

class Base1:
    def __init__(self, name) -> None:
        self.grant_parant = name

class Base2(Base1):
    def __init__(self, name1, name2) -> None:
        super().__init__(name1)
        self.parant = name2

class Child(Base2):
    def __init__(self, name1, name2, name3) -> None:
        super().__init__(name1, name2)
        self.child = name3

    def display(self):
        print("Grant Parant Name: ", self.grant_parant)
        print("Parant Name: ", self.parant)
        print("Child Name: ", self.child)

name1 = input("Enter grant parant Name: ")
name2 = input("Enter parant Name: ")
name3 = input("Enter child Name: ")

ob = Child(name1, name2, name3)
ob.display()