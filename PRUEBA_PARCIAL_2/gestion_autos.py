# gestion_autos.py
from calculos_y_mejoras import calcular_ip_inicial, aplicar_calculo_mejora
import autos as db_autos

def crear_auto_carrera(marca, modelo):
    specs = db_autos.PARAMETROS_ESTANDAR.copy()
    ip_inicial = calcular_ip_inicial(specs["vmax"], specs["tmax"])

    # Creamos las 4 ruedas mediante un bucle for tradicional
    ruedas_auto = []
    for i in range(4):
        ruedas_auto.append({"marca":"Generic", "modelo":"Sport", "rpm":0})

    nuevo_auto = {
        "marca": marca,
        "modelo": modelo,
        "vmax": specs["vmax"],
        "tmax": specs["tmax"],
        "dmax": specs["dmax"],
        "sujecion": specs["sujecion"],
        "pt": specs["pt"],
        "ip": ip_inicial,
        "encendido": False,
        "velocidad_actual": 0.0,
        "componentes":{
            "motor": {"marca":marca, "modelo": modelo, "rpm": 0}, 
            "transmision": {"marca": marca, "modelo": modelo, "tipo": "sincronica", "torque": 0.0},
            "carroceria": {"marca": marca, "modelo": modelo, "peso_kg": 1200},
            "ruedas": ruedas_auto
        },
        "mejoras": {
            "motor": 0,       # Maximo 3 mejoras
            "transmision": 0, # Maximo 2 mejoras
            "carroceria": 0,  # Maximo 3 mejoras
            "llantas": 0      # Maximo 3 mejoras
        }
    }

    #print(json.dumps(nuevo_auto, indent=4))  # Para depuración
    return nuevo_auto

def puede_competir(auto):
    # Un auto puede competir si tiene al menos 1 mejora en cualquier componente
    total_mejoras = sum(
        auto["mejoras"]["motor"],
        auto["mejoras"]["transmision"],
        auto["mejoras"]["carroceria"],
        auto["mejoras"]["llantas"]
    )
    return total_mejoras > 0

def actualizar_componentes_dinamicos(auto):
    # Calcular las RPM del motor, torque y RPM de las ruedas en funcion de la velocidad actual del auto.
    velocidad = auto["velocidad_actual"]
    vmax = auto["vmax"]

    if not auto["encendido"]:
        rpm_motor = 0
        torque = 0.0
        rpm_ruedas = 0
    else:
        if velocidad > 0:
            rpm_motor = 900 + int((velocidad / vmax) * 6100)  # RPM del motor entre 900 y 6100
        else:
            rpm_motor = 900  # RPM mínima del motor cuando está encendido pero detenido 
        torque = auto["pt"]*(rpm_motor/1000)
        rpm_ruedas = int((velocidad*1000)/(60*2.0))

    auto["componentes"]["motor"]["rpm"] = rpm_motor
    auto["componentes"]["transmision"]["torque"] = torque
    for rueda in auto["componentes"]["ruedas"]:
        rueda["rpm"] = rpm_ruedas

def encender_auto(auto):
    if auto['encendido']:
        return False, "El auto ya está encendido."
    auto['encendido'] = True
    actualizar_componentes_dinamicos(auto)
    return True, f"El {auto['marca']} {auto['modelo']} ha sido encendido."

def apagar_auto(auto):
    if not auto['encendido']:
        return False, "El auto ya está apagado."
    if auto['velocidad_actual'] > 0:
        return False, "No se puede apagar el auto mientras está en movimiento."
    auto['encendido'] = False
    actualizar_componentes_dinamicos(auto)
    return True, f"El {auto['marca']} {auto['modelo']} ha sido apagado."

def acelerar_auto(auto, incremento):
    if not auto["encendido"]:
        return False, "ERROR! El auto está apagado. Enciéndalo primero."

    nueva_velocidad = auto["velocidad_actual"] + incremento
    if nueva_velocidad > auto["vmax"]:
        auto["velocidad_actual"] = auto["vmax"]
        actualizar_componentes_dinamicos(auto)
        return True, f"El auto ha alcanzado su velocidad máxima de {auto['vmax']} Km/h."

    auto["velocidad_actual"] = nueva_velocidad
    actualizar_componentes_dinamicos(auto)
    return True, f"El auto ha acelerado a {auto['velocidad_actual']} Km/h."

def frenar_auto(auto, decremento):
    if not auto["encendido"]:
        return False, "ERROR! El auto está apagado. Enciéndalo primero."

    nueva_velocidad = auto["velocidad_actual"] - decremento
    if nueva_velocidad < 0:
        auto["velocidad_actual"] = 0
        actualizar_componentes_dinamicos(auto)
        return True, "El auto se ha detenido por completo."

    auto["velocidad_actual"] = nueva_velocidad
    actualizar_componentes_dinamicos(auto)
    return True, f"El auto ha frenado a {auto['velocidad_actual']} Km/h."

def agregar_mejora(auto, tipo_mejora):
    limites_mejoras = {"motor": 3, "transmision": 2, "carroceria": 3, "llantas": 3}
    actual = auto["mejoras"][tipo_mejora]

    if actual >= limites_mejoras[tipo_mejora]:
        return False, f"No se puede mejorar más el componente '{tipo_mejora}'. Ya alcanzó el máximo de mejoras."

    aplicar_calculo_mejora(auto, tipo_mejora)
    return True, f"Mejora de {tipo_mejora} aplicada exitosamente. Nuevo IP: {auto['ip']}"