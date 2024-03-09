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

#Metodo count (sirve para contar un caracter dentro de un string)
print("Saitama".count("a"))
print(nombre.count("i"))
#Metodo upper--> rodo el string a mayuscula y lower --> todo el string a minuscula
print("Saitama".upper())# SAITAMA
print("SaItAmA".lower())#saitama
print(nombre.upper())# CAMILA
print(nombre.lower())#camila
#Metodo title -> solo la primera letra a mayuscula 
print("saItAmA".title()) #Saitama
print("14564saItAmA".title()) #14564Saitama

# len() -> contar los caracteres de un string  
print(len(" camila garrido 2024")) #20 (es considerado el espacio)

#join -> unir elementos separados en un string
print(", ".join(["a","b","c"]))
print(", ".join(["camila","garrido","barrientos"]))
print(",".join(["camila","garrido","barrientos"]))

print("al\nfin\nviernes")
"""
al
fin
viernes
"""

mi_direccion = ""
miDireccion=""
#1miDireccion="" esto esta malo, no poner un numero delante, ni espacios en blancos
cantidad_alumnos= 30
peso = 85.5
verdadero= True


#Tipo de datos type (nombre_variable)-> me dice al tipo de variable que pertenece
#print(type(nombre_variable))
print(type(nombre)) #<class 'str'>
print(type(año)) #<class 'str'>
print(type(mes)) # <class 'int'>
print(type(peso)) #<class 'float'>
print(type(verdadero)) #<class 'bool'>

type(verdadero) # no imprime el tipo de dato

#Manipulacion Variables

numero = 2 #si la variable esta a la izq es una asignacion 
numero = numero + 3 #numero = 2 + 3 #si esta a la derecha es para evaluar (sacarle el valor)
print(numero)#5

nombre = nombre + "Garrido" # estoy concatenando, #nombre = "Camila"+"Garrido"
print(nombre) #CamilaGarrido

#precision de datos
print(5/9) #0.5555555555555556
print(f"resultado de la division {5/9:.2f}")
print("el resultado de la division",round(5/9,3))

# al trabajar con input el valor ingresado es de tipo string

nombre = input("ingrese su Nombre: ")
print("Tu nombre es",nombre)
print(f"Tu nombre es {nombre}")
edad = input("ingrese su Edad: ")
print("Tu tienes",edad,"años")
print(type(edad)) #<class 'str'>

