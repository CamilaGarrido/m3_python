import random
import sys

# Paso 1: Definir las opciones válidas para el juego
opciones_validas = ['piedra', 'papel', 'tijera']

# Paso 2: Verificar si se proporcionó un argumento y si es válido
if len(sys.argv) != 2 or sys.argv[1].lower() not in opciones_validas:
    
    # Paso 3: Mostrar un mensaje de error si el argumento no es válido
    print("Argumento inválido. Debe ser piedra, papel o tijera.")
    sys.exit(1)
else:
    # Paso 4: Mostrar un mensaje de que los datos fueron ingresados correctamente
    print("Datos ingresados correctamente!")

# Paso 5: Obtener la elección del usuario y la elección aleatoria del computador
eleccion_usuario = sys.argv[1].lower()  # Convertir a minúsculas
eleccion_computadora = random.choice(opciones_validas)

# Paso 6: Imprimir las elecciones del usuario y del computador
print("El usuario escogió:", eleccion_usuario)
print("La computadora escogió:", eleccion_computadora)

# Paso 7: Determinar el resultado del juego
if eleccion_usuario == eleccion_computadora:
    print("¡Es un empate!")
elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or \
    (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
    (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
    print("¡El usuario gana!")
else:
    print("¡La computadora gana!")

# Paso 8: Imprimir mensaje de fin del juego
print("Fin del juego")