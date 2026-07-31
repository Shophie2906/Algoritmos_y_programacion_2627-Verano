'''

Programacion Modular - Parcial 2_Practica 1

MET RACING - Juego de autos de carrera (Solucion Modular)

'''

import autos as db_autos
import gestion_autos as gestor_autos

def mostrar_estado_autos(lista_autos):
    print("\n === Estado de los autos de carrera ===")
    print("="*70)
    if not lista_autos:
        print("No hay autos de carrera en el garaje.")
        return

    for i in range(len(lista_autos)):
        idx = i + 1
        auto = lista_autos[i]

        estado_str = "ENCENDIDO" if auto["encendido"] else "APAGADO"
        compite_str = "SI" if gestor_autos.puede_competir(auto) else "NO (Requiere al menos 1 mejora para competir)"
        rpm_str = auto["componentes"]["motor"]["rpm"]

        print(f"  Auto {idx}: {auto['marca']} {auto['modelo']}| Estado: {estado_str} | Puede competir: {compite_str}")
        print(f"  IP: {auto['ip']:.2f} | Vmax: {auto['velocidad_actual']:.1f} Km/h | Tmax: {auto['tmax']} seg | Dmax: {auto['dmax']} m")
        print(f"  Sujeción: {auto['sujecion']:.2f} grips | Potencia: {auto['pt']:.1f} Hp")
        print(f"  Encendido: {'Sí' if auto['encendido'] else 'No'}")
        print(f"  Velocidad actual: {auto['velocidad_actual']} Km/h | RPM del motor: {rpm_str} RPM")
        print(f"  Mejoras --> Motor: {auto['mejoras']['motor']}/3 | Transmisión: {auto['mejoras']['transmision']}/2 | Carrocería: {auto['mejoras']['carroceria']}/3 | Llantas: {auto['mejoras']['llantas']}/3")
        print("-"*70)

def menu_agregar_auto(lista_autos):
   if len(lista_autos) >= 4:
       print("\n Se ha alcanzado el limite maximo de 4 autos de carrera en el juego") 
       return
   
   marcas = list(db_autos.MARCAS_Y_MODELOS)
   print("\n --- Seleccione una marca ---")
   for i in range(len(marcas)):
       print(f"{i + 1}. {marcas[i]}")

   idx_marcas = int(input("Seleccione una marca:")) -1 # el -1 es por que el cuenta desde 0 y en las opcioens desde 1
   marca_sel = marcas[idx_marcas]

   modelos = db_autos.MARCAS_Y_MODELOS[marca_sel]
   print(f"\n --- Modelos disponibles de {marca_sel} ---")
   for i in range(len(modelos)):
       print(f"{i + 1}. {modelos[i]}")

   idx_modelo = int(input("Seleccione un modelo:"))-1
   modelo_sel = modelos[idx_modelo]

   nuevo_auto = gestor_autos.crear_auto_carrera(marca_sel, modelo_sel)
   lista_autos.append(nuevo_auto)
   print(f"\n [+] Se ha agregado el auto {marca_sel} {modelo_sel} a la lista de autos de carrera")

def seleccionar_auto(lista_autos):
    if not lista_autos:
        print("\n No hay autos de carrera disponibles. Agregue un auto primero.")
        return None
    print("\n --- Seleccione un auto de carrera ---")
    for i in range(len(lista_autos)):
        auto = lista_autos[i]
        print(f"{i + 1}. {auto['marca']} {auto['modelo']}")
    idx_auto = int(input("Seleccione un auto:")) - 1
    return lista_autos[idx_auto] 

def menu_agregar_mejora(lista_autos):
    auto = seleccionar_auto(lista_autos)
    if not auto:
        return

    tipos = {"motor", "transmision", "carroceria", "llantas"}
    print("\n --- Tipos de mejoras disponibles ---")
    for i, tipo in enumerate(tipos):
        print(f"{i + 1}. Mejora de {tipo.capitalize()}")

    idx_tipo = int(input("Seleccione un tipo de mejora:")) - 1
    tipo_sel = list(tipos)[idx_tipo]  

    exito, msg = gestor_autos.agregar_mejora(auto, tipo_sel)
    print(f"\n [Resultado]: {msg}")

def main():
    autos_carrera=[]
    while True:

        print("\n === MET RACING - MENU PRINCIPAL ===")
        print("1. Agregar auto de carrera")
        print("2. Agregar mejoras a un auto de carreras")
        print("3. Encender el auto")
        print("4. Apagar el auto")
        print("5. Acelerar el auto")
        print("6. Frenar el auto")
        print("7. Salir del juego")

        opcion = int(input("Seleccione una opcion (1-7): "))

        if opcion== 1:
            menu_agregar_auto(autos_carrera)
        elif opcion==2:
            menu_agregar_mejora(autos_carrera)
        elif opcion==3:
           auto = seleccionar_auto(autos_carrera)
           if auto:
               __, msg = gestor_autos.encender_auto(auto)
               print(f"\n [Resultado]: {msg}")
        elif opcion==4:
           auto = seleccionar_auto(autos_carrera)
           if auto:
               __, msg = gestor_autos.apagar_auto(auto)
               print(f"\n [Resultado]: {msg}")
        elif opcion==5:
            auto = seleccionar_auto(autos_carrera)
            if auto:
                inc = float(input("Ingrese el incremento de velocidad (Km/h): "))
                __, msg = gestor_autos.acelerar_auto(auto, inc)
                print(f"\n [Resultado]: {msg}")
        elif opcion==6:
            auto = seleccionar_auto(autos_carrera)
            if auto:
                dec = float(input("Ingrese el decremento de velocidad (Km/h): "))
                __, msg = gestor_autos.frenar_auto(auto, dec)
                print(f"\n [Resultado]: {msg}")
        elif opcion==7:
            # salir del juego
            print("\n Gracias por jugar a MET RACING!")
            break

if __name__ == "__main__":
    main()       


