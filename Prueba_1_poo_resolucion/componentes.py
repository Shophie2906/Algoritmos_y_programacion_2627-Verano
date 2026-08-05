class Componente:
    """Clase base para todos los componentes (Herencia)."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.numero_mejoras=0
        self.max_mejoras=0
    def actualizar_dinamica(self, *args, **kwargs):
        pass  # Método que será sobrescrito (Polimorfismo)

    def get_max_mejoras(self):
        return self.max_mejoras

    def get_numero_mejoras(self):
        return self.numero_mejoras

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
        self.max_mejoras=3

    def get_rpm (self):
        return self.rpm

    def actualizar_dinamica(self, vel, vmax):
        # El motor actualiza sus RPM si el auto acelera o frena
        if vel > 0:
            self.rpm = 900 + int((vel / vmax) * 6100)
        else:
            self.rpm = 0

class Transmision(Componente):
    def __init__(self, marca, modelo, tipo="Sincronica"):
        super().__init__(marca, modelo)
        self.tipo = tipo
        self.torque = 0.0
        self.max_mejoras=2

    def actualizar_dinamica(self, pt, rpm_motor):
        # El torque depende de las revoluciones del motor
        self.torque = pt * (rpm_motor / 1000)

class Carroceria(Componente):
    def __init__(self, marca, modelo, peso_kg=1200):
        super().__init__(marca, modelo)
        self.peso_kg = peso_kg
        self.max_mejoras=3

class Rueda(Componente):
    def __init__(self, marca="Generic", modelo="Sport"):
        super().__init__(marca, modelo)
        self.rpm = 0
        self.max_mejoras=3

    def actualizar_dinamica(self, vel):
        # Las ruedas cambian sus RPM con la velocidad
        self.rpm = int((vel * 1000) / (60 * 2.0))