import sys 
"""Para desarrollar la funcionalidad se le entrega a usted un diccionario de prueba para verificar sus resultados."""
precios = {'Notebook': 700000,
            'Teclado': 25000,
            'Mouse': 12000,
            'Monitor': 250000,
            'Escritorio': 135000,
            'Tarjeta de Video': 1500000}
# Paso 1: Verificar la cantidad de argumentos.
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Por favor, ingrese un argumento válido.")
    sys.exit()

# Paso 2: Obtener el umbral del primer argumento y establecer la dirección del filtro.
umbral = int(sys.argv[1])
direccion = 'mayor' if len(sys.argv) == 2 else sys.argv[2]

# Paso 3: Definir las funciones para filtrar y mostrar resultados
def filtrar_productos(precios, umbral, direccion='mayor'):
    productos_filtrados = {}
    for producto, precio in precios.items():
        if direccion == 'mayor':
            if precio > umbral:
                productos_filtrados[producto] = precio
        elif direccion == 'menor':
            if precio < umbral:
                productos_filtrados[producto] = precio
        else:
            print("Lo sentimos, no es una operación válida")  
            return None
    return productos_filtrados
def mostrar_resultado(productos_filtrados, direccion):
    if direccion == 'mayor':
        print("Los productos mayores al umbral son:", ', '.join(productos_filtrados.keys()))
    elif direccion == 'menor':
        print("Los productos menores al umbral son:", ', '.join(productos_filtrados.keys()))
# Paso 4: Filtrar productos y mostrar los resultados.
productos_filtrados = filtrar_productos(precios, umbral, direccion)
if productos_filtrados:
    mostrar_resultado(productos_filtrados, direccion)