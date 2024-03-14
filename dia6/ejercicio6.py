
"""Determinar si un numero ingresado por el usuario 
    es par o impar
    utilizamos el modulo
"""
#Paso 1: Solicitar de ingreso de datos
numero = input("Ingresa el valor a evaluar\n")

#Paso 2: Transformar string a numeros (a input numero enteros)
numero = int(numero)

#Paso 3 : Evaluar con nuestras condicionales
if numero%2 == 0:
    print("El numero ingresado es par")
    
elif numero == 0:
    print("El numero ingresado es par")
    
else: 
    print("El numero ingresado es impar")

# 0/2 = 0
0
#-35/2 = -17
1