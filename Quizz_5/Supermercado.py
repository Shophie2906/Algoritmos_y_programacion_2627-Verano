from db import db
from Product import Alimento, Bebida
from Cliente import Cliente

class Supermercado():
    def __init__(self):
        self.db = db
        self.productos = []
        self.ventas = [] # Almacenará los objetos Cliente que compren en el día
        # Diccionario para rastrear la cantidad vendida por producto (para las estadísticas)
        self.historial_ventas_productos = {} 
        self.alimentos_vendidos = 0
        self.bebidas_vendidas = 0

    def Start(self):
        self.iniciar_objetos()
        while True:
            print()
            print("Bienvenido al Supermercado!")
            print("Seleccione una opcion: ")
            print("\t 1- Ver productos disponibles")
            print("\t 2- Realizar compra")
            # el usuario debe registrarse, luego se deben mostrar los productos, debe indicar cantidad, imprimir factura, aplicar descuento si su cedula termina en 3 o 7, actualizar stock (cantidad)
            print("\t 3- Finalizar el dia (estadisticas)")
            print("\t 4-Salir")

            opcion = int(input("Ingrese su eleccion(1-4): "))

            if opcion == 1:
                print()
                self.mostrar_productos()
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                print("Gracias por su compra!")
                break


    def iniciar_objetos(self):
        productos_dic = self.db["productos"]

        self.productos = []

        for item in productos_dic:
            if item["tipo"] == "alimento":
                producto = Alimento(item["nombre"], item["precio"], item["cantidad"], item["fecha_caducidad"])
            elif item["tipo"] == "bebida":
                producto = Bebida(item["nombre"], item["precio"], item["cantidad"], item["volumen"], item["con_gas"])

            self.productos.append(producto)
            self.historial_ventas_productos[producto.nombre] = 0

    def registro(self):
        print(" === REGISTRO ===")
        nombre = input("Indique su nombre: ").strip()
        cedula = input(" Indique su cedula (eg. 31444777): ").strip()
        telefono = input(" Indique su numero de telefono (eg. 0424333555): ").strip()
        return nombre, cedula, telefono       

    def mostrar_productos(self):
        print(" === PRODUCTOS DISPONIBLES ===")
        for idx, p in enumerate(self.productos, 1):
            print(f"{idx}. {p.nombre} | Precio: ${p.precio} | Stock: {p.cantidad}")

    def realizar_compra(self):

        # se debe indicar cedula de registro
        # se debe indicar producto
        # se debe indicar cantidad del producto
        pass

    def aplicar_descuento(self, cedula, subtotal):
        #si su cedula termine en 3 o 7 se aplica un 10% 
        if cedula.endswith(('3', '7')):
            print(" Felicidades tu cedula termina en 3 o 7 ganaste un descuento!!")
            return subtotal*0.10
        return 0.0

    def actualizar_stock(self, producto, cantidad):
        producto.cantidad -= cantidad
    
    def imprimir_factura(self):
        print(" == FACTURA ==")
        print()
        print(" Nombre: {}")


