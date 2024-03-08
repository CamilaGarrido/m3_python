#la separacion de los float es un punto (.)
#la division entre integers, el resultado es un float

print(4/2) #2.0
print(5/2) #2.5
print(5/3.5) #1.4285714285714286
print(2.4*4) #9.6

nombre = "Camila"
año = "2024"
print(3*nombre) #CamilaCamilaCamila
print(año*2) #20242024
#print(nombre/2) #no se puede dividir un string

# Interpolacion de cadenas (otra forma de imprimir) print(f"{nombre_variable}")
mes = 3
dia = 7

print(f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia} ")

#string.format
#print("".format())
print("Hola{}, El año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#Interpolacion con % (%s para string y %d para numeros)
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))
