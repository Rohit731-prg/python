# multi path inheritance

class Bill:
    def __init__(self, item, price) -> None:
        self.items = item
        self.price = price

class Cash(Bill):
    def __init__(self, item, price) -> None:
        super().__init__(item, price)

    def display(self):
        print("Total cash payment : ", self.items * self.price)

class Card(Bill):
    def __init__(self, item, price) -> None:
        super().__init__(item, price)

    def display(self):
        self.total = self.items * self.price
        print("Total cash payment : ", self.total - (self.total * 10 / 100))

class payment(Cash, Card):
    def __init__(self, item, price) -> None:
        Cash.__init__(self, item, price)
        Card.__init__(self, item, price)

    def display(self):
        Cash.display(self)
        Card.display(self)

items = int(input("Enter total items: "))
price = int(input("Enter price for each item: "))
ob = payment(items, price)
ob.display()