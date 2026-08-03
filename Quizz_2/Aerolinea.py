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
                pass
            elif menu == 2:
                pass
            elif menu == 3:
                pass
            elif menu == 4:
                pass
            elif menu == 5:
                print("Gracias por jugar MetroTour")
                break
            
    def iniciar_objetos(self):
        pilotos_dic = self.bd["pilotos"]
        vuelos_dic = self.bd["vuelos"]
        pasajeros_dic = self.bd["pasajeros"]
        
        
        
        
    
            