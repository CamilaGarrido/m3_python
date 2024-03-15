# Paso 1: Solicitar al usuario ingresar el peso en kilogramos (Kg) y su altura en centimetros (cm).
peso_kg = float(input("Ingrese su peso en kilogramos (Kg): "))
altura_cm = float(input("Ingrese su altura en centimetros (cm): "))

# Paso 2: Validación de la estatura
if altura_cm < 50 or altura_cm > 250:
    print("La altura ingresada no es válida. ")
    print("Por favor, ingresar una altura entre el rango de 50 cm a 250 cm.")
    exit()
# Paso 3: Convertir la altura (centímetros a metros).
altura_m = altura_cm / 100

# Paso 4: Calcular el IMC 
imc = peso_kg / (altura_m ** 2)
# Paso 5: Redondear el resultado a dos decimales.
imc = round(imc, 2)

# Paso 6: clasificar el IMC según la OMS.
if imc < 18.5:
    clasificacion = "Bajo Peso"
elif 18.5 <= imc < 25:
    clasificacion = "Adecuado"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
elif 30 <= imc < 35:
    clasificacion = "Obesidad Grado I"
elif 35 <= imc < 40:
    clasificacion = "Obesidad Grado II"
else:
    clasificacion = "Obesidad Grado III"

print(f"Su índice de masa corporal (IMC) es: {imc}") #Imprime el valor del IMC.
print(f"Su clasificación según la OMS es: {clasificacion}")  #Imprime la clasificación del IMC según la OMS