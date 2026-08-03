from Persona import Pasajero
class Vuelo:
    def __init__(self, id, fecha_salida, lugar_despegue, destino, piloto, pasajeros):
        self.id = id
        self.fecha_salida = fecha_salida
        self.lugar_despegue = lugar_despegue
        self.destino = destino
        self.piloto = piloto
        self.pasajeros = pasajeros
    
    def show(self):
        print(f"ID: {self.id}")
        print(f"Fecha de salida: {self.fecha_salida}")
        print(f"Lugar de despegue: {self.lugar_despegue}")
        print(f"Destino: {self.destino}")
        print(f"Piloto: {self.piloto.nombre}")
        print(f"Pasajeros: ")
        for pasajero in self.pasajeros:
            print(f" {pasajero.cedula} - {pasajero.nombre} ({pasajero.confirmado})")
        