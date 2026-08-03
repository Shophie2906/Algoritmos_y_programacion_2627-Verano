
class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_attr(self):
        print(f" Id: {self.id}")
        print(f" Name: {self.name}")

class Guest(Person):
    def __init__(self, id, name, seat, allergies, confirmed):
        super().__init__(id, name)
        self.seat = seat
        self.allergies = allergies
        self.confirmed = confirmed

    def show_attr(self):
        super().show_attr()
        print(f" Seat: {self.seat}")
        print(f" Allergies: {self.allergies}")
        print(f" Confirmed: {self.confirmed}")

    def confirmar_boleto(self):
        self.confirmed = True  

class StaffMember(Person):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def show_attr(self):
        super().show_attr()
        print(f" Salary: {self.salary}")

