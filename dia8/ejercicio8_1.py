#len: para preguntar por el tamaño de la lista
#el tamaño de una lista vacia es cero
#comprension: comprimir el texto de escritura




# solicitamos el número de pares a generar
n = 10
# generamos una lista vacía para almacenar los pares
# el tamaño es cero
lista_par = []
print(len(lista_par))

for i in range(10):
# podemos hacer append de los valores generados
# en este caso partimos desde el 2
    lista_par.append(2*i + 2)
    print(f" lista_par {lista_par}")

# mostramos el resultado
print(lista_par)

### COMPREHENSION ###
#[formula for variable in iterable]
lista_par = [2*i + 2 for i in range(n)]
print(lista_par)

valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(f"divisibles {divisibles}")

divisibles2 = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores ]
print(divisibles2)

#####

print("")
lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas',5.1, 45.2, 1, 2, 0]
count_str = 0
lista_str= []
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)
        
print(f" cantidad de string {count_str}")
print(f" cantidad de string {len(lista_str)}")
#tarea es crear el list comprehension


claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
diccionario2= {k:v for k,v in zip(claves, valores)}
print(diccionario2)#{'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 33, 'altura': 1.75}

diccionario2.a