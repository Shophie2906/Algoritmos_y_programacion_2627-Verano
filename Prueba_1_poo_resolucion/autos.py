from componentes import *

class AutoEstandar:
    """Clase base que representa un vehículo de calle. No puede competir."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # Parámetros estándar
        self.vmax = 180.0
        self.tmax = 14.0
        self.dmax = 80.0
        self.sujecion = 1.0
        self.pt = 150.0
        self.ip=self.calcular_ip_inicial()
        self.encendido = False
        self.velocidad_actual = 0.0

        # Relación de Composición: El auto crea sus propios componentes vitales
        self.motor = Motor(marca, modelo)
        self.transmision = Transmision(marca, modelo)
        self.carroceria = Carroceria(marca, modelo)
        
        # Relación de Agregación: Las ruedas se inician vacías y se agregan
        self.ruedas = []
        self.agregar_ruedas()
    def get_marca (self):
        return self.marca
    
    def get_modelo (self):
        return self.modelo
    
    def get_vmax (self):
        return self.vmax
    
    def set_vmax (self,  valor):
        self.vmax=valor

    def get_tmax (self):
        return self.tmax
    
    def set_tmax (self,  valor):
        self.tmax=valor

    def get_dmax (self):
        return self.dmax

    def set_dmax (self,  valor):
        self.dmax=valor

    def get_sujecion (self):
        return self.sujecion
    
    def set_sujecion (self,  valor):
        self.sujecion=valor

    def get_pt (self):
        return self.pt
    def set_pt (self,  valor):
        self.pt=valor

    def get_encendido(self):
        return self.encendido
    
    def get_velocidad_actual (self):
        return self.velocidad_actual

    def get_motor(self):
        return self.motor

    def get_ip (self):
        return self.ip

    def set_ip (self,  valor):
        self.ip=valor
     
    def instalar_ruedas(self, lista_ruedas):
        if len(lista_ruedas) == 4:
            self.ruedas = lista_ruedas

    def get_transmision(self):
        return self.transmision

    def get_carroceria(self):
        return self.carroceria

    def calcular_ip_inicial(self):
        """Calcula el IP inicial del auto estándar: 5% de Vmax + Tmax."""
        return (self.get_vmax() * 0.05) + self.get_tmax()
    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            self.actualizar_componentes()
            return True, f"{self.marca} {self.modelo} ha sido encendido"
        return False, "Ya está encendido."

    def apagar(self):
        if self.velocidad_actual == 0:
            self.encendido = False
            self.actualizar_componentes()
            return True, "Auto apagado."
        return False, "No puedes apagar en movimiento."

    def actualizar_componentes(self):
        """Uso de Polimorfismo: se envían mensajes a cada componente."""
        if not self.encendido:
            vel = 0
        else:
            vel = self.velocidad_actual

        self.motor.actualizar_dinamica(vel, self.vmax)
        self.transmision.actualizar_dinamica(self.pt, self.motor.rpm)
        for rueda in self.ruedas:
            rueda.actualizar_dinamica(vel)

    def agregar_ruedas(self):
        for i in range(4):
            rueda=Rueda()
            self.ruedas.append(rueda)

    def info_ruedas(self):
        respuesta=''
        for i, rueda in enumerate(self.ruedas):
            respuesta= respuesta + f"\n rueda {i+1} + Mejoras: {rueda.get_numero_mejoras()}/{rueda.get_max_mejoras()}"
        return respuesta

    def get_ruedas(self):
        return self.ruedas








class AutoCarrera(AutoEstandar):
    """Herencia: Un auto de carrera extiende al estándar y añade prestaciones."""
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
                      
       
       
    def puede_competir(self):
        total=0
        for rueda in self.ruedas:
            total+=rueda.get_numero_mejoras()
        return sum([self.get_motor().get_numero_mejoras(),self.get_transmision().get_numero_mejoras(),self.get_carroceria().get_numero_mejoras(),total ]) > 0

    def agregar_mejora(self, tipo):
      
        respuesta=False
        if tipo == "motor":
            respuesta=self.get_motor().aplicar_mejora()
        elif tipo=="transmision":
            respuesta=self.get_transmision().aplicar_mejora()
        elif tipo=="carroceria":
           respuesta=self.get_carroceria().aplicar_mejora()
        elif tipo=="ruedas":
            for rueda in self.get_ruedas():
                resul=0
                if rueda.aplicar_mejora():
                    resul+=1
            if resul==4:
                respuesta= True

        self.aplicar_calculo_mejora(tipo)


        if respuesta:
            return respuesta, f"Mejora {tipo} aplicada. Nuevo IP: {self.ip:.2f}"
        else: 
            return respuesta, f"Mejora {tipo} NO aplicada. "

    #Funciones estándar para calcular aumentos y disminuciones porcentuales
    def incrementar_pct(self, valor, pct):
        """Aumenta un valor en un porcentaje determinado."""
        return valor * (1 + pct)

    def disminuir_pct(self, valor, pct):
        """Disminuye un valor en un porcentaje determinado."""
        return valor * (1 - pct)

    def aplicar_calculo_mejora(self, tipo_mejora):
        """
        Actualiza el IP y los parámetros del diccionario 'auto' según la mejora aplicada.
        """
        vmax = self.get_vmax()
        tmax = self.get_tmax()
        dmax = self.get_dmax()
        sujecion = self.get_sujecion()
        pt = self.get_pt()
        ip = self.get_ip()
        #mejoras = auto["mejoras"]

        if tipo_mejora == "motor":
            x = self.get_motor().get_numero_mejoras()
            # Fórmula IP: IP = IP + (X * 7% + Vmax * 7% + PT) / Tmax
            inc_ip = (x * 0.07 + vmax * 0.07 + pt) / tmax
            self.set_ip(ip + inc_ip)
            self.set_vmax(self.incrementar_pct(vmax, 0.08))
            self.set_tmax(self.disminuir_pct(tmax, 0.04))
            self.set_pt(self.incrementar_pct(pt, 0.05))
            

        elif tipo_mejora == "transmision":
            y = self.get_transmision().get_numero_mejoras()
            # Fórmula IP: IP = IP + (Y * 3% + Vmax * 3% + PT) / Tmax
            inc_ip = (y * 0.03 + vmax * 0.03 + pt) / tmax
            self.set_ip(ip + inc_ip)
            self.set_vmax(self.incrementar_pct(vmax, 0.09))
            self.set_tmax(self.disminuir_pct(tmax, 0.03))
            self.set_pt(self.incrementar_pct(pt, 0.06))
            
        elif tipo_mejora == "carroceria":
            # Atributo Z según el nivel: nivel 1 -> Z=2, nivel 2 -> Z=4, nivel 3 -> Z=6
            valores_z = [2, 4, 6]
            nivel_actual = self.get_carroceria().get_numero_mejoras()
            z = valores_z[nivel_actual-1]
            # Fórmula IP: IP = IP + (Z * 2% + Vmax * 2% + Dmax * 3% + sujecion)
            inc_ip = (z * 0.02) + (vmax * 0.02) + (dmax * 0.03) + sujecion
            self.set_ip(ip + inc_ip)
            self.set_vmax(self.incrementar_pct(vmax, 0.03))
            self.set_tmax(self.disminuir_pct(tmax, 0.025))
            self.set_pt(self.incrementar_pct(pt, 0.03))
        elif tipo_mejora == "ruedas":
            ruedas=self.get_ruedas()
            # Atributo W según el nivel: nivel 1 -> W=0.1, nivel 2 -> W=0.2, nivel 3 -> W=0.3
            valores_w = [0.1, 0.2, 0.3]
            nivel_actual = ruedas[0].get_numero_mejoras()
            w = valores_w[nivel_actual]
            # Fórmula IP: IP = IP + (W * 2% + sujecion)
            inc_ip = (w * 0.02) + sujecion
            self.set_ip(ip + inc_ip)
            self.set_sujeción(self.incrementar_pct(sujecion, 0.08))