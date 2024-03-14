# Paso 1: Solicitar al usuario ingresar el peso en kilogramos (Kg) y su altura en centimetros (cm).

peso_kg = float(input("Ingrese su peso en kilogramos (Kg): ")) #Solicitar al usuario que ingrese su peso en kg y se almacena en la variable peso_kg.
altura_cm = float(input("Ingrese su altura en centimetros (cm): ")) #Solicitar al usuario que ingrese su altura en (cm) y se almacena en la variable altura_cm.

# Paso 2: Convertir la altura (centímetros a metros).

altura_m = altura_cm / 100 #Convertir la altura de (cm) a (m) dividiendo entre 100 y se almacena en la variable altura_m.

# Paso 3: Calcular el IMC 

imc = peso_kg / (altura_m ** 2)  #Fórmula IMC: peso_kg/(altura_m ^2) y se almacena en la variable imc.

# Paso 4: Redondear el resultado a dos decimales.

imc = round(imc, 2) 

# Paso 5: clasificar el IMC según la OMS.
if imc < 18.5: 
    clasificacion = "Bajo Peso" #IMC es menor que 18.5, la persona tiene "Bajo Peso".
    
elif 18.5 <= imc < 25:  
    clasificacion = "Adecuado"#IMC está entre 18.5 y 25, la persona tiene un IMC "Adecuado".
    
elif 25 <= imc < 30:  
    clasificacion = "Sobrepeso"#IMC está entre 25 y 30, la persona tiene "Sobrepeso".
    
elif 30 <= imc < 35:  
    clasificacion = "Obesidad Grado I"#IMC está entre 30 y 35, la persona tiene "Obesidad Grado I".
    
elif 35 <= imc < 40:  
    clasificacion = "Obesidad Grado II"#IMC está entre 35 y 40, la persona tiene "Obesidad Grado II".
    
else: 
    clasificacion = "Obesidad Grado III" #IMC es igual o mayor a 40, la persona tiene "Obesidad Grado III".

# Paso 6: Mostrar el resultado del IMC y su clasificación al usuario.

print(f"Su indice de masa corporal (IMC) es: {imc}")  #Imprime el valor del IMC.
print(f"Su clasificación según la OMS es: {clasificacion}")  #Imprime la clasificación del IMC según la OMS.