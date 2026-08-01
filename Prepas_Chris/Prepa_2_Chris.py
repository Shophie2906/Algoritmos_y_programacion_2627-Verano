# PREPA 2. BUCLES Y ESTRUCTURAS
# PREPARADOR: CHRISTIAN 

# LAB 1. Piramide Abstracta
"""for i in range(5, 0, -1):
    print('*'*i)"""

# LAB 2. Fibonacci
"""n = 8
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b """

# LAB 3. Conjetura de Collatz
"""
n = 9

print(n, end=" ")

while n > 1:
    if n % 2 == 0 :
        n = n // 2
    else: 
        n = 3 * n +1
    
    print(n, end=" ")
    
    """

# LAB 4. Reduccion Digital
"""
n = 98

while n >= 10:
    suma_digitos = 0
    temp = n

    while temp > 0:
        suma_digitos += temp % 10
        temp = temp // 10
    
    n = suma_digitos

print("La raiz digital es:", n)
"""

# LAB DE LISTAS. MODIFICACION
# EJERCICIO 1. ELIMINACION QUIRURGICA
"""
lista = {8, 7, -5, 6, 3, -1}
lista_negativos = []

for i in lista:
    if i < 0:
        lista_negativos.append(i)
    else: 
        continue
print(lista_negativos)

for j in lista_negativos:
    lista.remove(j)
print(lista)
"""

# EJERCICIO 2. Pila de Comandos 
"""
pila = []

while True : 
    comando = input("Ingresa comando o palabra de ingreso:")

    if comando == "pop": 
        if pila: 
            pila.pop()
            print("Ultimo elemento eliminado")
        else: 
            print("la lista ya esta vacia")
    elif comando == "invertir":
        pila.reverse()
        print("Se volteo el orden de la lista")
    else :
        pila.append(comando)

    print("Estado actual:", pila)
"""

# EJERCICIO 3. El espejo matematico


# LAB DE DICCIONARIOS. 
# EJERCICIO 4. Filtro Blockbuster









    
