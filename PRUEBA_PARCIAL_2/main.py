import autos as db_autos
import gestion_autos as crear_auto_carrera

def menu_agregar_auto(lista_autos):
   if len(lista_autos) >= 4:
       print("\n Se ha alcanzado el limite maximo de 4 autos de carrera en el juego") 
       return
   marcas = list(db_autos.MARCAS_Y_MODELOS)
   print("\n --- Seleccione una marca ---")
   for i in range(len(marcas)):
       print(f"{i + 1}. {marcas[i]}")
   idx_marcas = int(input("Seleccione una marca:")) -1 # el -1 es por que el cuenta desde 0 y en las opcioens desde 1
   marcas_sel = marcas[idx_marcas]
   modelos = db_autos.MARCAS_Y_MODELOS[marcas_sel]
   print(f"\n --- Modelos disponibles de {marcas_sel} ---")
   for i in range(len(modelos)):
       print(f"{i + 1}. {modelos[i]}")
   idx_modelo = int(input("Seleccione un modelo:"))-1
   modelo_sel = modelos[idx_modelo]
   nuevo_auto = crear_auto_carrera(marcas_sel, modelo_sel)
   lista_autos.append(nuevo_auto)



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
            # menu_agregar_mejora()
            pass
        elif opcion==3:
            # encender auto
           pass
        elif opcion==4:
            # apagar auto
            pass
        elif opcion==5:
            # acelerar auto
            pass
        elif opcion==6:
            # frenar auto
            pass
        elif opcion==7:
            # salir del juego
            print("\n Gracias por jugar a MET RACING!")
            break

if __name__ == "__main__":
    main()       


