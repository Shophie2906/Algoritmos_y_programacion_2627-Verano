# PREPA 1. FUNDAMENTOS DE PYTHON
# PREPARADOR: CHRISTIAN 

# EJERCICIO 1. Calculo del IMC
"""
peso = int(input("solicitud de peso:"))
altura = int(input("solicitud de altura:"))
imc = peso/(altura*2)
print("Su IMC es: " +str(round(imc,2)))
"""

# EJERCICIO 2. Conversor tiempo
"""
minuto = 60 
hora = 3600

tiempo = int(input("cantidad de segundos a transformar:"))
horas = tiempo//hora
rest_horas = tiempo%horas
minutos = rest_horas//minuto
segundos = rest_horas%minutos

print("la cantidad de horas es:" +str(horas)+",minutos" +str(minutos) +",segundos" +str(segundos))
"""

# EJERCICIO 3. Cuenta Restaurant


# EJERCICIO 4. Numero par y positivo


# EJERCICIO 5. Acceso por Edad


# EJERCICIO 6. Validacion clave


# EJERCICIO 7. Clasificacion clima
"""
celsius = int(input("celsius:"))

if celsius<10 :
    print("Hace mucho frio")
elif celsius>=10 and celsius<=25 :
    print("Esta templado")
else:
    print("Esta haciendo mucho calor") 
"""

# EJERCICIO 8. Descuentos


# EJERCICIO 9. Cajero Automatico


# RETO INTERACTIVO 1. La formula resolvente
"""
print("La ecuacion cuadratica es: Ax^2 + Bx + C = 0")

a = int(input("Ingrese A: "))
b = int(input("Ingrese B: "))
c = int(input("Ingrese C: "))

discriminante = (b**2)-(4*a*c)
if discriminante==0:
    print("Tiene solucion unica y es:")
    resultado = (-b)/(2*a)
    print(resultado)
elif discriminante>0:
    print("Tiene dos soluciones reales, las cuales son:")
    raiz = discriminante**0.5
    resultado_1 = ((-b)-raiz)/(2*a)
    resultado_2 = ((-b)+raiz)/(2*a)
    print(str(resultado_1) + "y" + str(resultado_2))
else: 
    raiz = (-discriminante)**0.5
    parte_entera = (-b)/(2*a)
    raiz_fraccionaria = raiz/(2*a)
    print("El sistema tiene dos soluciones reales, las cuales son:")
    print(str(parte_entera) + "-" + str(raiz_fraccionaria) + "i y " + str(parte_entera) + "+" + str(raiz_fraccionaria) + "i")
"""

# RETO INTERACTIVO 2. Clasificador de triangulos


