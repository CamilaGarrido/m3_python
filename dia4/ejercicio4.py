"""
Solicitar al usuario el ingreso de 3 numeros 
y determinar cuales de ellos es mayor que 33
el usuario solo puede escribir numeros del 1 al 100 enteros
y determinar cual es mayor y cual es menor 

1. Analizar el problema
Se captura 3 datos numericos del usuario solicitando solo numeros enteros del 1 al 100, 
usuario ingresa primer numero, y validar si cumple con los requisitos anteriores, si cumple se continua 
con el ingreso del segundo numero de lo contrario arrojar un mensaje de error y solicitar el reingreso de un numero 
repetir el procedimiento de validacion con los siguiente numero 

lo segundo es realizar el proceso para determinar si el primer, segundo y tercer numero ingresado es mayor que 33
si alguno cumple este requisito

el tercer proceso determinar cual es mayor y cual es menor

2. Descomponer el problema en partes

solicitar al usuario el ingreso de 3 numeros: 
determinar cuales de ellos es mayor que 33
solo numeros enteros del 1 al 100
determinar cual es mayor y cual es menor

3. Resolver el problema
Determinar cual es mayor y cual es menor
mostrar resultados

numero < 33
promedio >=40.0
promedio < 40.0
promedio > 39.5


Realizar el calculo promedio de las 3 notas con 2 decimales

Inicio
leer nota1
leer nota2
leer  nota3

promedio (nota1+not2+not3)/3
imprimir variable promedio con 2 decimales
Fin

"""
# ingresar las notas
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# promedio
promedio = (nota1 + nota2 + nota3) / 3

# resultado con dos decimales
print("El promedio de las tres notas es: {:.2f}".format(promedio))
