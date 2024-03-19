#Paso 1: Importar el módulo sys
import sys 

# Paso2: Definir el diccionario de ventas proporcionado
ventas = {
    "Enero": 15000, 
    "Febrero": 22000, 
    "Marzo": 12000,
    "Abril": 17000, 
    "Mayo": 81000, 
    "Junio": 13000,
    "Julio": 21000, 
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500, 
    "Noviembre": 91000, 
    "Diciembre": 21000,
}

#Paso 3:Convertir el primer argumento de la línea de comandos en un entero (umbral)
try:
    umbral = int(sys.argv[1])
except (IndexError, ValueError):
    # Si no se proporciona el argumento o no se puede convertir a entero, mostrar un mensaje y salir del programa
    print("Por favor escribe: python .\desafio3\mayor_a.py valor_umbral")
    sys.exit(1)

# Paso 4: Filtrar las ventas que superan el umbral y almacenarlas en un diccionario llamado ventas_filtradas
ventas_filtradas = {mes: monto for mes, monto in ventas.items() if monto > umbral}

#Paso 5: Verificar si hay ventas filtradas.
# Si hay ventas filtradas, imprimir el diccionario de ventas_filtradas.
if ventas_filtradas:
    print(ventas_filtradas)
else:
    # Si no hay ventas filtradas, mostrar un mensaje. 
    print("No hay meses con ventas superiores al umbral.")