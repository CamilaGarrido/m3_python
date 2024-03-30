import preguntas as p  # Importar el módulo de preguntas y se renombra: 'p'

# Definimos la función 'verificar' que comprueba si la elección del usuario es correcta
def verificar(alternativas, eleccion):
    eleccion = ['a', 'b', 'c', 'd'].index(eleccion)  

    # Generar lógica para determinar respuestas correctas 
    ########################################################################################## 
    if alternativas[eleccion][1] == 1:  # Si la segunda entrada de la tupla de la alternativa seleccionada es 1
        print('Respuesta Correcta')  # Imprimimos que la respuesta es correcta
        correcto = True  # Asignamos True a la variable correcto
    else:
        print('Respuesta Incorrecta')  # Imprimir la respuesta es incorrecta
        correcto = False  # Asignar False a la variable correcto
    ##########################################################################################
    
    return correcto  # Devolver el valor de correcto (True o False)

if __name__ == '__main__':  
    from print_preguntas import print_pregunta  
    
    # Seleccionar una pregunta del módulo de preguntas 'p'
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    
    # Imprimir el enunciado y las alternativas.
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    
    # Solicitar al usuario que escoja la alternativa correcta
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    
    # Llamar a la función verificar.
    verificar(pregunta['alternativas'], respuesta)