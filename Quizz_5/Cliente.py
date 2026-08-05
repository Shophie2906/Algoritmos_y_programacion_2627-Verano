class Cliente():
    def __init__(self, nombre, cedula, telefono, compras, monto_total):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.compras = compras
        self.monto_total = monto_total

    def show(self):
        print(f" Nombre: {self.nombre}")
        print(f" Cedula: {self.cedula}")
        print(f" Telefono: {self.telefono}")
        print(f" Compra: {self.compras}")
        print(f" Monto Total: {self.monto_total}")
        