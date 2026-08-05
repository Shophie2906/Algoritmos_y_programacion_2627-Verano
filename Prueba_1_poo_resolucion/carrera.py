from garage import Garage



#class Carrera:




def main():
    
    el_garage = Garage()
    while True:
        el_garage.mostrar_estado_autos()
        print("\n=== MET RACING - MENÚ PRINCIPAL ===")
        print("1. Agregar auto de carrera")
        print("2. Agregar mejoras a un auto de carrera")
        print("3. Encender auto")
        print("4. Apagar auto")
        print("5. Acelerar auto")
        print("6. Frenar auto")
        print("7. Salir del juego")

        opcion = int(input("Seleccione una opción (1-7): "))

        if opcion == 1:
            el_garage.menu_agregar_auto()
        elif opcion == 2:
            el_garage.menu_agregar_mejora()
        elif opcion == 3:
            auto = el_garage.seleccionar_auto()
            if auto:
                _, msg = auto.encender()
                print(f"\n[Resultado]: {msg}")
        elif opcion == 4:
            auto = seleccionar_auto(autos_carrera)
            if auto:
                _, msg = apagar_auto(auto)
                print(f"\n[Resultado]: {msg}")
        elif opcion == 5:
            auto = seleccionar_auto(autos_carrera)
            if auto:
                inc = float(input("Ingrese la magnitud de aceleración (Km/h): "))
                _, msg = acelerar_auto(auto, inc)
                print(f"\n[Resultado]: {msg}")
        elif opcion == 6:
            auto = seleccionar_auto(autos_carrera)
            if auto:
                dec = float(input("Ingrese la magnitud de frenado (Km/h): "))
                _, msg = frenar_auto(auto, dec)
                print(f"\n[Resultado]: {msg}")
        elif opcion == 7:
            print("\n¡Gracias por jugar a Met Racing!")
            break

if __name__ == "__main__":
    main()