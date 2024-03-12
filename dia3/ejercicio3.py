from math import sqrt,ceil

"""Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
"""

#Paso 1: Capturar los datos (string), y conversion
#radio = float(input("Ingrese el radio en kilometros"))*1000 (no nos aseguramos si lo que ingreso el usuario este bien)

radio_kilometros = input("Ingrese el radio en kilometros")
radio_kilometros = float(radio_kilometros)
radio_metros = radio_kilometros * 1000

constante_gravitacional = input("Ingrese la constante de gravedad del planeta en [mt/s]")
constante_gravitacional = float(constante_gravitacional)#conversion de string a float

#Paso 2:Resolver la formula velocidad_escape = raiz_cuadrada(2* constante_gravitacional * radio_metros)
velocidad_escape = sqrt(2* constante_gravitacional * radio_metros)

#Paso 3: Mostrar el resultado final
print(f"La velocidad de Escape es {round(velocidad_escape,1)} [m/s]")