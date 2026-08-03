from bd import db
from Vuelo import Vuelo
from Persona import Piloto, Pasajero

class Aerolinea:
    def __init__(self):
        self.bd=db 
    
    def Start(self):
        self.iniciar_objetos()
        while True:
            print()
            print("Bienvenido a la aerolinea MetroTour!")
            print("Seleccione una opción:")
            print("\t 1- Mostrar nomina")
            print("\t 2- Mostrar pasajeros")
            print("\t 3- Ver itinerario de aviones")
            print("\t 4- Confirmar docuemntacion de viaje")
            print("\t 5- Salir")
            
            menu = int(input("Ingresa una opcion (1-5):"))
            
            if menu == 1: 
                for piloto in self.pilotos:
                    print()
                    piloto.show()
            elif menu == 2:
                for pasajero in self.pasajeros:
                    print()
                    pasajero.show()
            elif menu == 3:
                for vuelo in self.vuelos:
                    print()
                    vuelo.show()
            elif menu == 4:
                cedula_ingresada = (input(" Introduce la cedula del pasajero a confirmar: "))
                encontrado = False

                for pasajero in self.pasajeros:
                    if pasajero.cedula.strip().upper() == cedula_ingresada.strip().upper():
                        pasajero.confirmar_boleto()
                        encontrado = True
                        print(f" Documentacion confirmada con exito para {pasajero.nombre} ")
                        break
                if not encontrado:
                    print("\n Error: No se encontró ningún pasajero registrado con esa cédula.")
            elif menu == 5:
                print("Gracias por jugar MetroTour")
                break
            
    def iniciar_objetos(self):
        pilotos_dic = self.bd["pilotos"]
        vuelos_dic = self.bd["vuelos"]
        pasajeros_dic = self.bd["pasajeros"]

        self.pilotos=[]
        self.vuelos=[]
        self.pasajeros=[]

        for piloto in pilotos_dic:
            self.pilotos.append(Piloto(piloto["id"], piloto["nombre"], piloto["cedula"], piloto["telefono"], piloto["tipo_avion"], piloto["años_experiencia"]))
        
        for pasajero in pasajeros_dic:
            self.pasajeros.append(Pasajero(pasajero["id"], pasajero["nombre"], pasajero["cedula"], pasajero["telefono"], pasajero["millas_vuelo"], pasajero["confirmado"]))

        for vuelo in vuelos_dic:

            piloto_encontrado = None
            for piloto in self.pilotos:
                if piloto.id == vuelo["id_piloto"]:
                    piloto_encontrado = piloto

            pasajeros_encontrados = []
            for pasajero in self.pasajeros:
                for ids_pasajeros in vuelo["ids_pasajeros"]:
                    if pasajero.id == ids_pasajeros:
                        pasajeros_encontrados.append(pasajero)

            self.vuelos.append(Vuelo(vuelo["id"], vuelo["fecha_salida"], vuelo["lugar_despegue"], vuelo["destino"], piloto_encontrado, pasajeros_encontrados))

   
             
                
    
            