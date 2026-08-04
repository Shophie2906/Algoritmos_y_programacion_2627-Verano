
class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_attr(self):
        print(f" Id: {self.id}")
        print(f" Name: {self.name}")

class Worker(Person):
    def __init__(self, id, name, role, dispatches):
        super().__init__(id, name)
        self.role = role
        self.dispatches = dispatches

    def show_attr(self):
        super().show_attr()
        print(f" Role: {self.role}")
        print(f" Dispatches: {self.dispatches}")

class Client(Person):
    def __init__(self, id, name, address):
        super().__init__(id, name)
        self.address = address

    def show_attr(self):
        super().show_attr()
        print(f" Address: {self.address}")
        

