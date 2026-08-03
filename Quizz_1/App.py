from db import db
from Trabajador import Trabajador
from Producto import Producto, Alimento, Bebida 
from Categoria import Categoria

class App: 
    def start(self):
        self.cargar_objetos()
        while True: 
            print()
            print("Bienvenido a MetroFoot!")
            print("Seleccione una opción:")
            print("\t 1- Ver productos")
            print("\t 2- Ver encargados")
            print("\t 3- Ver productos por categoria")
            print("\t 4- Cambiar Stock de los productos")
            print("\t 5- Eliminar producto")
            print("\t 6- Salir")
            opcion = int(input("Ingrese una opción (1-6): "))

            if opcion == 1: 
                for producto in self.productos:
                    print()
                    producto.show()
            elif opcion == 2: 
                for trabajador in self.trabajadores:
                    print()
                    trabajador.show()
            elif opcion == 3:
                for categoria in self.categorias:
                    print()
                    categoria.show()
            elif opcion == 4: 
                print()
                print("\n---Lista de productos---")
                for producto in self.productos:
                    producto.resumen()
                id_buscar = int(input("Indica el Id del producto al que deseas cambiarle el stock (1-11): "))

                encontrado = False
                for producto in self.productos:
                    if producto.id == id_buscar:
                        nuevo_stock = int(input("Ingrese la nueva cantidad disponible: "))
                        producto.cambiar_stock(nuevo_stock)
                        encontrado = True
                        print("\n El stock ha sido actualizado con éxito!")
                        break
                if not encontrado:
                    print("\n Error: El producto con ese Id no fue encontrado")
            elif opcion == 5:
                self.eliminar_producto()
            elif opcion == 6:
                print("Gracias por usar MetroFoot!")
                break

    def cargar_objetos(self):
        self.productos=[]
        self.categorias=[]
        self.trabajadores=[]

        for trabajador in db['trabajadores']:
            self.trabajadores.append(Trabajador(trabajador["id"], trabajador["nombre"], trabajador["cargo"], trabajador["edad"], trabajador["horas_trabajo_diarias"]))

        for producto in db['productos']:
            if producto["tipo"] == "alimento":
                self.productos.append(Alimento(producto["id"], producto["nombre"], producto["precio"], producto["cantidad_stock"], producto["porcion"], producto["personas"]))
            elif producto["tipo"] == "bebida":
                self.productos.append(Bebida(producto["id"], producto["nombre"], producto["precio"], producto["cantidad_stock"], producto["volumen"], producto["alcoholica"]))

        for categoria in db['categorias']:
            encargado = None
            for trabajador in self.trabajadores:
                if trabajador.id == categoria["id_encargado"]:
                    encargado = trabajador
            productos = []
            for producto in self.productos:
                for id_producto in categoria["productos"]:
                    if producto.id == id_producto:
                        productos.append(producto)
            self.categorias.append(Categoria(categoria["id"], categoria["nombre"], categoria["cantidad_productos"], encargado, productos))


    def eliminar_producto(self):
        print("\n--- Productos Disponibles ---")
        for producto in self.productos:
            producto.resumen()

        id_eliminar = int(input("\nIngrese el ID del producto que desea eliminar: "))

        encontrado = False
        for producto in self.productos:
            if producto.id == id_eliminar:
                self.productos.remove(producto)
                encontrado = True

                for categoria in self.categorias:
                    if producto in categoria.productos:
                        categoria.productos.remove(producto)
                        categoria.cantidad_productos -= 1

                print(f"\n[+] ¡El producto '{producto.nombre}' ha sido eliminado exitosamente!")
                break

        if not encontrado:
            print("\n[!] Error: No se encontró ningún producto con ese ID.")