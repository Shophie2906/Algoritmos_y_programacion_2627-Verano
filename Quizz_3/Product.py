
class Product():
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def show_attr(self):
        print(f" Id: {self.id}")
        print(f" Name: {self.name}")
        print(f" Quantity: {self.quantity}")
        print(f" Price: {self.price}")

        