
class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def show(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")

class Bebida(Producto):
    def __init__(self, id, nombre, precio, stock, volumen, alcoholica):
        super().__init__(id, nombre, precio, stock)
        self.volumen = volumen
        self.alcoholica = alcoholica

    def show(self):
        super().show()
        print(f"Volumen: {self.volumen}")
        print(f"Alcoholica: {self.alcoholica}")

class Alimento(Producto):
    def __init__(self, id, nombre, precio, stock, porcion, cant_personas):
        super().__init__(id, nombre, precio, stock)
        self.porcion = porcion
        self.cant_personas = cant_personas

    def show(self):
        super().show()
        print(f"Porción: {self.porcion}")
        print(f"Cantidad de personas: {self.cant_personas}")