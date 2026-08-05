

class Product():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def show(self):
        print(f" Nombre: {self.nombre}")
        print(f" Precio: {self.precio}")
        print(f" Cantidad: {self.cantidad}")

class Alimento(Product):
    def __init__(self, nombre, precio, cantidad, fecha_caducidad):
        super().__init__(nombre, precio, cantidad)
        self.fecha_caducidad = fecha_caducidad

    def show(self):
        super().show()
        print(f" Fecha de Caducidad: {self.fecha_caducidad}")

class Bebida(Product):
    def __init__(self, nombre, precio, cantidad, volumen, con_gas):
        super().__init__(nombre, precio, cantidad)
        self.volumen = volumen
        self.con_gas = con_gas

    def show(self):
        super().show()
        print(f" Volumen: {self.volumen}")
        print(f" Con Gas: {self.con_gas}")
