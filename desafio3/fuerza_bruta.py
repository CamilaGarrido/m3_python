# Paso 1: Importar
from string import ascii_lowercase # letras minúsculas del alfabeto 
import getpass # módulo para solicitar contraseñas de forma oculta

# Paso 2: Definir la función para el ataque de fuerza bruta
def fuerza_bruta(contraseña):
    intentos = 0  # contador de intentos
    for letra in contraseña:  # Iterar sobre cada letra de la contraseña
        for elemento in ascii_lowercase:  # Iterar sobre cada letra minúscula del alfabeto
            if letra == elemento:  # Si la letra de la contraseña coincide con la letra del alfabeto
                intentos += 1  # Incrementar el contador de intentos
                break  
            else:
                intentos += 1  # Si no coinciden, incrementar el contador de intentos
    return intentos  # total de intentos

# Paso 3: Solicitar la contraseña (de forma oculta) 
print("Bienvenido")
contraseña = getpass.getpass("Ingrese la contraseña: ").lower()

# Paso 4: Realizar el ataque de fuerza bruta y almacenar el número de intentos
intentos = fuerza_bruta(contraseña)

# Paso 5: Mostrar el resultado del ataque
print(f"La contraseña fue forzada en {intentos} intentos")