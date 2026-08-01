from db import db
from Trabajador import Trabajador
from Producto import Producto

class App: 
    def Start(self):
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
            opcion = int(input("Ingrese una opción (1-5): "))

            if opcion == 1: 
                pass
            elif opcion == 2: 
                pass
            elif opcion == 3:
                pass
            elif opcion == 4: 
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                print("Gracias por usar MetroFoot!")
                break

    def cargar_objetos(self):
        self.productos=[]
        self.categorias=[]
        self.trabajadores=[]

        for trabajador in db['trabajadores']:
            self.trabajadores.append(Trabajador(trabajador["id"], trabajador["nombre"], trabajador["cargo"], trabajador["edad"], trabajador["horas_de_trabajo"]))

        for producto in db['productos']:
            if producto['tipo'] == "alimento":
                self.productos.append(Alimento(producto["id"], producto["nombre"], producto["tipo"], producto["precio"], producto["cantidad_stock"]))