


def main():

    while True:
        print()
        print("Bienvenido a Metro Racing!")
        print("Seleccione una opción:")
        print("\t 1- Agregar auto de carreras")
        print("\t 2- Agregar mejoras a un auto")
        print("\t 3- Acelerar un auto")
        print("\t 4- Frenar un auto")
        print("\t 5- Encender un auto")
        print("\t 6- Apagar un auto")
        print("\t 7- Salir")

        opcion = int(input("Ingrese una opcion (1-7): "))

        if opcion == 1: 
            el_garage.agregar_auto()
        elif opcion == 2: 
            el_garage.agregar_mejora()
        elif opcion == 3:
            el_garage.acelerar_auto()
        elif opcion == 4:
            el_garage.frenar_auto()
        elif opcion == 5:
            el_garage.encender_auto()
        elif opcion == 6:
            el_garage.apagar_auto()
        elif opcion == 7:
            print("Gracias por usar Metro Racing!")
            break

if __name__ == "__main__":
    main()