
class Persona:
    def __init__(self, id, nombre, cedula, telefono):
        self.id = id
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        
    def show(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Cedula: {self.cedula}")
        print(f"Telefono: {self.telefono}")
    
class Piloto(Persona):
    def __init__(self, id, nombre, cedula, telefono, tipo_avion, años_experiencia):
        super().__init__(id, nombre, cedula, telefono)
        self.tipo_avion = tipo_avion
        self.años_experiencia = años_experiencia
    
    def show(self):
        super().show()
        print(f"Tipo de avion: {self.tipo_avion}")
        print(f"Años de experiencia: {self.años_experiencia}")
        
class Pasajero(Persona):
    def __init__(self, id, nombre, cedula, telefono, millas, confirmado):
        super().__init__(id, nombre, cedula, telefono)
        self.millas = millas
        self.confirmado = confirmado
        
    def show(self):
        super().show()
        print(f"Millas: {self.millas}")
        print(f"Boleto confirmado: {self.confirmado}")
        
       
       
        