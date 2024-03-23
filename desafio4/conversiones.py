#Paso 1:Importar sys.
import sys

# Paso 2: Verificar si se ingresan argumentos correctos.
if len(sys.argv) != 5:
    print("Debes ingresar python conversiones.py tasa_sol tasa_peso_arg tasa_dolar valor_en_peso_chileno")
else:
    try:
        #Paso 3: Tasas de conversión y valor en peso chileno.
        tasa_sol = float(sys.argv[1])
        tasa_peso_arg = float(sys.argv[2])
        tasa_dolar = float(sys.argv[3])
        valor_en_peso_chileno = float(sys.argv[4])

        # Paso 4: Conversiones en soles, pesos y dolares.
        valor_en_soles = valor_en_peso_chileno * tasa_sol
        valor_en_pesos_argentinos = valor_en_peso_chileno * tasa_peso_arg
        valor_en_dolares = valor_en_peso_chileno * tasa_dolar

        # paso 5: Imprimir los resultados.
        print("Los {} pesos equivalen a:".format(int(valor_en_peso_chileno)))
        print("{:.1f} Soles".format(valor_en_soles))
        print("{:.1f} Pesos Argentinos".format(valor_en_pesos_argentinos))
        print("{:.1f} Dólares".format(valor_en_dolares))

#Paso 6: Mensaje de error si no se ingresa argumento válido.
    except ValueError:
        print("Error: Debes ingresar números válidos como argumento.")