
class Categoria:
    def __init__(self, id, nombre, cantidad_productos, encargado, productos):
        self.id = id
        self.nombre = nombre
        self.cantidad_productos = cantidad_productos
        self.encargado = encargado
        self.productos = productos

    def show(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de productos: {self.cantidad_productos}")
        print(f"Encargado: {self.encargado.nombre}")
        print(f"Productos: ")
        for producto in self.productos:
            producto.resumen()

