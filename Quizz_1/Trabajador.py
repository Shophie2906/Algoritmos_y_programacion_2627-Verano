
class Trabajador:
    def __init__(self, id, nombre, cargo, edad, horas_de_trabajo):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo 
        self.edad = edad
        self.horas_de_trabajo = horas_de_trabajo

    def show(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Edad: {self.edad}")
        print(f"Horas de trabajo: {self.horas_de_trabajo}")