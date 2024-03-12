"""Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().
"""

#Paso 1: Captura de datos
precio_suscripcion = float(input("Ingrese el precio de suscripcion: "))
num_usuario_normal = int(input("Ingrese cantidad de usuarios normales: "))
num_usuario_premium = int(input("Ingrese cantidad de usuarios premium: "))
gastos_totales = float(input("Ingrese los gastos totales: "))

#Paso 2: Calculo de utilidades
utilidades = (precio_suscripcion * num_usuario_normal + (1.5 * precio_suscripcion)* num_usuario_premium)- gastos_totales

#Paso 3: Entrega de resultados
print(f"Las utilidades del proyecto son:{utilidades}")