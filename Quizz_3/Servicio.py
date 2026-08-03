from old_db import old_db
from Person import Guest, StaffMember
from Product import Product
from Provider import Provider

class Servicio():
    def __init__(self):
        self.old_bd = old_db

    def Start(self):
        self.iniciar_objetos()
        while True:
            print()
            print("Bienvenido a ServiMet!")
            print("Selecciona una opcion: ")
            print("\t 1- Ver invitados")
            print("\t 2- Ver proveedores")
            print("\t 3- Confirmar asistencia de invitado")
            print("\t 4- Productos en lista de alergias de los invitados")
            print("\t 5- Costo total de la boda")
            print("\t 6- Salir")

            opcion = int(input("Ingrese su eleccion(1-6): "))

            if opcion == 1: 
                for guest in self.guests:
                    print()
                    guest.show_attr()
            elif opcion == 2:
                for provider in self.providers:
                    print()
                    provider.show_attr()
            elif opcion == 3:
                invitado_id = int(input("Ingrese su Id para confirmar asistencia: "))
                encontrado = False

                for guest in self.guests:
                    if guest.id == invitado_id:
                        guest.confirmar_boleto()
                        encontrado = True
                        print(f" Asistencia confirmada con exito!")
                if not encontrado:
                    print("\n No se encontro ningun invitado registrado bajo ese id")
            elif opcion == 4:
                self.ver_alergias()
            elif opcion == 5:
                self.costo_boda()
            elif opcion == 6:
                print("Gracias por Jugar!")
                break

    def iniciar_objetos(self):
        guest_dic = self.old_bd["Guests"]
        staff_dic = self.old_bd["Staff"]
        providers_dic = self.old_bd["Providers"]
        products_dic = self.old_bd["Products"]

        self.guests = []
        self.staff = []
        self.providers = []
        self.products = []

        for guest in guest_dic:
            self.guests.append(Guest(guest["id"], guest["name"], guest["seat"], guest["allergies"], guest["confirmed"]))

        for staff in staff_dic:
            self.staff.append(StaffMember(staff["id"], staff["name"], staff["salary"]))

        for product in products_dic: 
            self.products.append(Product(product["id"], product["name"], product["quantity"], product["price"]))

        for provider in providers_dic:
            productos_encontrados = []
            
            for product in self.products:
                if product.id in provider["products"]:
                    productos_encontrados.append(product)

            self.providers.append(Provider(provider["id"], provider["name"], productos_encontrados))

    def ver_alergias(self):
        allergies_list = []
        encontrado = False
        
        for guest in self.guests:
            for allergies in guest.allergies:
                if allergies not in allergies_list:
                    allergies_list.append(allergies)
        print(f"Lista alergias de invitados: {allergies_list}")

    def costo_boda(self):
        costo_total = 0

        costo_productos = 0
        for product in self.products:
            costo_productos += product.quantity * product.price

        costo_salarios = 0
        for staff_member in self.staff:
            costo_salarios += staff_member.salary

        costo_total = costo_productos + costo_salarios
        print(f" El costo de la boda es: {costo_total}")

                   


