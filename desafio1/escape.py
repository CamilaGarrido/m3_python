#Velocidad de escape
import math #proporciona funciones matemáticas estándar, incluida la función sqrt() que necesitaremos para calcular la raíz cuadrada.
def calcular_velocidad_escape(radio, constante_gravitacional): #define una función llamada calcular_velocidad_escape() que toma dos parámetros: radio y constante_gravitacional.
    velocidad_escape = math.sqrt(2 * constante_gravitacional * radio)
    return velocidad_escape

def main(): #se define otra función llamada main()
    print("Ingrese el radio en Kilómetros:")
    radio_km = float(input()) # función input() para solicitar al usuario que ingrese el radio del planeta en kilómetros y la constante gravitacional.
    print("Ingrese la constante de gravedad del planeta en [mt/s]:")
    constante_gravitacional = float(input())

    # Convertir el radio de kilómetros a metros, multiplicando por 1000 (ya que 1 km=1000m).
    radio_m = radio_km * 1000
    
    # Calcular la velocidad de escape, con los valores ingresados y almacena el resultado en la variable velocidad_escape.
    velocidad_escape = calcular_velocidad_escape(radio_m, constante_gravitacional)
    
    print(f"La velocidad de Escape es {velocidad_escape:.1f} [m/s]") #Finalmente, imprime el resultado.

if __name__ == "__main__": #Llama a la función main(), lo que inicia la ejecución del programa.
    main()