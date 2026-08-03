from Product import Product

class Provider():
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def show_attr(self):
        print(f" Id: {self.id}")
        print(f" Name: {self.name}")
        print(f" Products: ")
        for product in self.products:
            print(f"\t {product.name}")

