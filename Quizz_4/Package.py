
class Package():
    def __init__(self, id, address, delivered):
        self.id = id
        self.address = address 
        self.delivered = delivered

    def show_attr(self):
        print(f" Id: {self.id}")
        print(f" Address: {self.address}")
        print(f" Delivered: {self.delivered}")

    def confirmar_entrega(self):
        self.delivered = True