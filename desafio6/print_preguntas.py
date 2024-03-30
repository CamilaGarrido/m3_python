import preguntas as p

def print_pregunta(enunciado, alternativas):
# Paso 1: Imprimir enunciado
    print(f'{enunciado[0]}\n')
        # [['alt_1', 0], ['alt_2', 1], ['alt_3', 0], ['alt_4', 0]]

# Paso 2: Imprimir alternativas
    for letra, (alternativa, _) in zip("ABCD", alternativas):
        print(f'{letra}. {alternativa}')

if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4