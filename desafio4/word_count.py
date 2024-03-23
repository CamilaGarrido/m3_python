#Paso 1: Importar sys y obtener el nombre del archivo de texto desde los argumentos de la línea de comandos.
import sys
archivo = sys.argv[1]

# Paso 2: Verificar que se proporcionó el nombre del archivo como argumento.
if len(sys.argv) != 2:
    print("Debes ingresar python word_count.py lorem_ipsum.txt")
    sys.exit(1)

# Paso 3: Importar el texto del archivo.
try:
    with open(archivo, "r") as file:
        texto = file.read()

#Paso 3.1: Generar un mensaje si no se encuentra el archivo.
except FileNotFoundError:
    print(f"No se pudo encontrar el archivo: {archivo}")
    sys.exit(1)

# Paso 4: Definir una función para contar caracteres distintos en el texto.
def contar_caracteres(texto):
    return len(set(texto))

#Paso 5: Definir una función para contar palabras distintas en el texto.
def contar_palabras(texto):
    palabras = texto.split(" ")
    return len(set(palabras))

#Paso 6: Contar la cantidad de caracteres y palabras distintas.
numero_caracteres, numero_palabras = contar_caracteres(texto), contar_palabras(texto)

# Paso 7: Imprimir los resultados.
print("El número de caracteres distintos es:", numero_caracteres)
print("El número de palabras distintas es:", numero_palabras)