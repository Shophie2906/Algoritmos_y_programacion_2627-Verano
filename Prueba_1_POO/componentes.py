
class Componente: 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.cant_mejoras = 0
        self.max_mejoras = 0

    def actualizar_dinamica(self, *args, **kwargs):
        pass

    def get_numero_mejoras(self):
        return self.cant_mejoras

    def get_max_mejoras(self):
        return self.max_mejoras

    def aplicar_mejora(self):
        if self.get_numero_mejoras()+1 > self.get_max_mejoras():
            return False
        else: 
            self.set_mejora()
            return True

    def set_mejora(self):
        self.numero_mejoras+=1

class Motor(Componente):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.rpm = 0
        self.max_mejoras = 3

    def get_rpm(self):
        return self.rpm

    def actualizar_dinamica(self, vel, vmax):
        if vel > 0 :
            self.rpm = (vel /)
    