"""
REVISION CONJUNTA DEL DESAFIO

pesos_kilogramos=float(input("Ingresa tu peso en kilogramos"))
estatura = float(input("Ingresa tu estatura en cm"))/100
estatura = estatura/100 convirtiendo centimetros a metros

"""

import sys
#se ejecuta en la terminal: python dia7/imc.py 81 178
peso_kilogramos= sys.argv[1]
estatura = sys.argv[2]

print(sys.argv)  #['dia7/imc.py', '81', '178']
print(sys.argv[1]) #81
print(sys.argv[2]) #178

#float string a un numero

peso_kilogramos= float(sys.argv[1])
estatura = float(sys.argv[2])/100

print(type(peso_kilogramos))
print(type(estatura))

#hacer validacion de la estatura

#calculo del IMC 
#imc = peso_kilogramos/ (estatura * estatura)
imc = peso_kilogramos/ (estatura **2)
print(f"Tu imc es de {round(imc,2)}")
#print(f"Tu imc es de {imc:.2}")

"""
if imc < 18.5: 
    print ("Tu clasificación según la OMS es: Bajo Peso")
elif imc >18.5 and imc < 25:
    print("Tu clasificación según la OMS es: Adecuado")
elif imc < 30:
    print("Tu clasificación según la OMS es: Sobrepeso")
elif imc < 35:

"""
#Otra forma 
if imc < 18.5: 
    print ("Tu clasificación según la OMS es: Bajo Peso")
elif imc >18.5 and imc < 25:
    clasificacion = "Adecuado"
elif imc < 30:
    clasificacion = "Sobrepeso"
elif imc < 35:
    clasificacion = "Obesidad grado I"
elif imc < 40:
    clasificacion = "Obesidad grado II"
elif imc>=40:
    clasificacion = "Obesidad grado III"

print(f"Tu clasificación según la OMS es: {clasificacion}")

    