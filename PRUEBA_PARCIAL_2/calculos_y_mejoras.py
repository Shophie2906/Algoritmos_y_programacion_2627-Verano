#calculos_y_mejoras.py

# Funciones para calcular aumentos y disminuciones porcentuales
def calcular_ip_inicial(vmax, tmax):
    # el IP inicial es igual a: 5% de Vmax + Tmax
    return (0.05 * vmax) + tmax


def incrementar_pct(valor, pct):
    return valor * (1 + pct)


def disminuir_pct(valor, pct):
    return valor * (1 - pct)


def aplicar_calculo_mejora(auto, tipo_mejora):
    vmax = auto["vmax"]
    tmax = auto["tmax"]
    dmax = auto["dmax"]
    sujecion = auto["sujecion"]
    pt = auto["pt"]
    ip = auto["ip"]
    mejoras = auto["mejoras"]

    if tipo_mejora == "motor":
        nivel_actual = mejoras["motor"]
        inc_ip = ((nivel_actual + 1) * 0.07 + vmax * 0.07 + pt) / tmax
        auto["ip"] = ip + inc_ip
        auto["vmax"] = incrementar_pct(vmax, 0.08)
        auto["tmax"] = disminuir_pct(tmax, 0.04)
        auto["pt"] = incrementar_pct(pt, 0.05)
        auto["mejoras"]["motor"] = nivel_actual + 1

    elif tipo_mejora == "transmision":
        nivel_actual = mejoras["transmision"]
        inc_ip = ((nivel_actual + 1) * 0.03 + vmax * 0.03 + pt) / tmax
        auto["ip"] = ip + inc_ip
        auto["vmax"] = incrementar_pct(vmax, 0.09)
        auto["tmax"] = disminuir_pct(tmax, 0.03)
        auto["pt"] = incrementar_pct(pt, 0.06)
        auto["mejoras"]["transmision"] = nivel_actual + 1

    elif tipo_mejora == "carroceria":
        valores_z = [2, 4, 6]
        nivel_actual = mejoras["carroceria"]
        z = valores_z[nivel_actual]

        inc_ip = (z * 0.02) + (vmax * 0.02) + (dmax * 0.03) + sujecion
        auto["ip"] = ip + inc_ip
        auto["vmax"] = incrementar_pct(vmax, 0.03)
        auto["tmax"] = disminuir_pct(tmax, 0.025)
        auto["dmax"] = incrementar_pct(dmax, 0.03)
        auto["sujecion"] = incrementar_pct(sujecion, 0.05)
        auto["mejoras"]["carroceria"] = nivel_actual + 1

    elif tipo_mejora == "llantas":
        valores_w = [0.1, 0.2, 0.3]
        nivel_actual = mejoras["llantas"]
        w = valores_w[nivel_actual]
        inc_ip = (w * 0.02 + sujecion)
        auto["ip"] = ip + inc_ip
        auto["sujecion"] = incrementar_pct(sujecion, 0.08)
        auto["mejoras"]["llantas"] = nivel_actual + 1

    else:
        raise ValueError(f"Tipo de mejora inválido: {tipo_mejora}")