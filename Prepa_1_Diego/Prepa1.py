# Prepa 1. Prepa larga Martes 21, julio 2026
# Prepador: Diego Arreaza.
'''
def mifuncion():
    x = input(" ")
    print("mi funcion")

x = input()
y = 2+2

mifuncion()
'''
# Prog modular
'''
import modular as M  #llamo a un archivo externo para alguna funcion

M.ejem()
M.ejem2()
'''

# Programacion Orientada a Objetos
'''
class caballo():
    def __init__(self):
        self
'''



# EJERCICIO 1. Haz una calculadora haciendo uso de funciones
'''
def main():
    def suma():
        a = int(input())
        b = int(input())
        print(f"El resultado es:\n {a + b}")

    def resta():
        a = int(input())
        b = int(input())
        print(f"El resultado es:\n {a - b}")
    
    def multiplicacion():
        a = int(input())
        b = int(input())
        print(f"El resultado es:\n {a * b}")

    def division():
        a = float(input())
        b = float(input())
        print(f"El resultado es:\n {a / b}")

    print("Bienvenido a la calculadora \nEscriba la operacion que desea hacer\n 1 -suma\n 2- resta \n3- Multiplicacion \n 4- Division")
    operacion = int(input("Escriba la operacion que desea hacer:\n"))
    if(operacion == 1):
        suma()
    if(operacion == 2):
        resta()
    if(operacion == 3):
        multiplicacion()
    if(operacion == 4):
        division()

main()
'''

# EJERCICIO 2. 
'''Haz un programa que con funcion modular se le escriba 2 
numeros distintos y se encarge de averiguar cual de los numeros es mayor
'''
import main2 as mm

a = int(input("Termino a:"))
b = int(input("Termino b:"))

mm.identifica(a,b)  
