from old_bd import old_bd
from Package import Package
from Person import Worker, Client
from DispatcherCompany import DistpatcherCompany

class Gestora():
    def __init__(self):
        self.old_bd = old_bd

    def Start(self):
        self.iniciar_objetos()
        while True:
            print()
            print("Bienvenid@ a Metro Gestora!")
            print("Selecciona una opcion: ")
            print("\t 1- Ver trabajadores")
            print("\t 2- Ver companias de despacho")
            print("\t 3- Confirmar entrega")
            print("\t 4- Salir")

            opcion = int(input("Elige una opcion(1-4): "))

            if opcion == 1: 
                for worker in self.workers:
                    print()
                    worker.show_attr()
            elif opcion == 2:
                for dispatcher_company in self.dispatcher_companies:
                    print()
                    dispatcher_company.show_attr() 
            elif opcion == 3:
                paquete_id = int(input(" Indicar Id del paquete a confirmar: "))
                encontrado = False

                for package in self.packages:
                    if package.id == paquete_id:
                        package.confirmar_entrega()
                        encontrado = True
                        print(f" Paquete recibido con exito!")
                if not encontrado:
                    print("\n No se encontro ningun registro de paquete con ese Id")
            elif opcion == 4:
                print("Gracias por elegirnos!")
                break

    def iniciar_objetos(self):
        clients_dic = self.old_bd["clients"]
        workers_dic = self.old_bd["workers"]
        distpatchercompanies_dic = self.old_bd["dispatcher_companies"]
        packages_dic = self.old_bd["packages"]

        self.clients = []
        self.workers = []
        self.dispatcher_companies = []
        self.packages = []

        for client in clients_dic:
            self.clients.append(Client(client["id"], client["name"], client["address"]))

        for worker in workers_dic:
            self.workers.append(Worker(worker["id"], worker["name"], worker["role"], worker["dispatches"]))

        for package in packages_dic:
            self.packages.append(Package(package["id"], package["address"], package["delivered"]))

        for dispatcher_company in distpatchercompanies_dic:
            # packages is a list
            paquete_encontrado = []

            for package in self.packages:
                if package.id in dispatcher_company["packages"]:
                    paquete_encontrado.append(package)

            self.dispatcher_companies.append(DistpatcherCompany(dispatcher_company["id"], dispatcher_company["name"], paquete_encontrado))



