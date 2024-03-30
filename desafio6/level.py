# Paso 1: Definir la función choose_level
def choose_level(n_pregunta, p_level):
    # Paso 2: Construir lógica para escoger el nivel.
    ##################################################
    p_level = int(p_level)  # Convertir el nivel de preguntas a entero
    
    if n_pregunta <= p_level: 
        level = 'basicas'  # El nivel es 'basicas'
    elif n_pregunta <= 2 * p_level: 
        level = 'intermedias'  # El nivel es 'intermedias'
    else: 
        level = 'avanzadas'  # El nivel es 'avanzadas'
    ##################################################
    return level  # Devolver el nivel seleccionado

if __name__ == '__main__':
    # Paso 3: Verificar los resultados de la función.
    print(choose_level(2, 2))  # básicas
    print(choose_level(3, 2))  # intermedias
    print(choose_level(7, 2))  # avanzadas
    print(choose_level(4, 3))  # intermedias