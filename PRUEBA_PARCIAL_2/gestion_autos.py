import autos as db_autos


def crear_auto_carrera(marca, modelo):
    specs = db_autos.PARAMETROS_ESTANDAR.copy()
    # ip_inicial = calcular_ip_inicial(specs["vmax"], specs["tmax"])

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
        "sujecion": specs["pt"],
        "ip": 20,
        "encendido": False,
        "velocidad_actual": 0.0,
        "componentes":{
            "motor": {"marca":marca, "modelo": modelo, "rpm": 0}, 
            "transmision": {"marca": marca, "modelo": modelo, "tipo": "sincronica", "torque": 0.0},
            "carroceria": {"marca": marca, "modelo": modelo, "peso_kg": 1200},
            "ruedas": ruedas_auto
        },
        "mejoras": {
            "motor": 0,
            "transmision": 0, 
            "carroceria": 0, 
            "llantas": 0
        }
    }