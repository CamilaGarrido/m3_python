# Paso 1: Definir la función validate
def validate(opciones, eleccion):
    
    # Paso 2: Definir validación de la elección del usuario
    while eleccion not in opciones:  
        eleccion = input('Opción no válida, ingrese una de las opciones válidas: ').lower()  
    # Paso 3: Retornar la opción validada
    return eleccion

if __name__ == '__main__':
    # Paso 4: Solicitar al usuario que ingrese una opción
    eleccion = input('Ingresa una Opción: ').lower()
    
# letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    # Paso 5: Definir la lista de opciones válidas
    numeros = ['0', '1']
    
    # Paso 6: Validar la elección del usuario llamando a la función validate
    opcion_validada = validate(numeros, eleccion)
    
    # Paso 7: Imprimir la opción validada
    print("La opción validada es:", opcion_validada)