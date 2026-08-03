from componentes import * 

class AutoEstandar:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Parametros estandar
        self.vmax = 180.0   #Km/h
        self.tmax = 14.0    #segundos
        self.dmax = 80.0    # metros    
        self.sujecion = 1.0 # grips
        self.pt = 150.0     # Nm
        self.ip = calcular_ip_inicial()
        self.encendido = False
        self.velocidad_actual = 0.0
        #  Relación de Composición
        self.motor = Motor(marca, modelo)
        self.transmision = Transmision(marca, modelo)
        self.carroceria = Carroceria(marca, modelo)
        # 
        self.ruedas = []
        self.agregar_ruedas()

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_vmax(self):
        return self.vmax

    def set_vmax(self, valor):
        self.vmax = valor

    def get_tmax(self):
        return self.tmax

    def set_tmax(self, valor):
        self.tmax = valor

    def get_dmax(self):
        return self.dmax

    def set_dmax(self, valor):
        self.dmax = valor

    def get_sujecion(self):
        return self.sujecion

    def set_sujecion(self, valor):
        self.sujecion = valor

    def get_pt(self):
        return self.pt 

    def set_pt(self, valor):
        self.pt = valor

    def get_ip(self):
        return self.ip

    def set_ip(self, valor):
        self.ip = valor

    def get_encendido(self):
        return self.encendido

    def get_velocidad(self):
        return self.velocidad_actual

    def get_motor(self):
        return self.motor

    def get_transmision(self):
        return self.transmision

    def get_carroceria(self):
        return self.carroceria

    def instalar_ruedas(self, lista_ruedas):
        if len(lista_ruedas) == 4: 
            self.ruedas = lista_ruedas

    def calcular_ip_inicial(self):
        return ((self.get_vmax()*0.5) + self.get_tmax())

    def encender(self):
        if not self.encendido:
            self.encendido = True
            self.actualizar_componentes()
            print(f"El auto {self.get_marca()} {self.get_modelo()} ha sido encendido.")
        else:
            print(f"El auto {self.get_marca()} {self.get_modelo()} ya está encendido.")

    def apagar(self):
        if self.velocidad_actual == 0:
            self.encendido = False
            self.actualizar_componentes()
            return True, "Auto apagado."
        else: 
            return False, "No se puede apagar el auto mientras está en movimiento."

    def actualizar_componentes(self):
        if not self.encendido:
            vel = 0 
        else: 
            vel = self.velocidad_actual
        self.motor.actualizar_dinamica(vel, self.vmax)
        self.transmision.actualizar_dinamica(self.pt, self.motor.get_rpm())
        for rueda in self.ruedas:
            rueda.actualizar_dinamica(vel)



    



