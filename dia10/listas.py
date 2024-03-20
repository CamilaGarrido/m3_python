#con diccionarios utilizamos llaves {}
#sys.argv para capturar el argumento

"""
LISTAS
1) son mutables, es decir pueden cambiar 
2) pueden tener distintos tipos de elementos
3) se usan los [] para definir una variable tipo lista
4) **indice => la posicion de los elementos

5) la primera posicion SIEMPRE ES CERO
6) la ultima posicion esta dada por, ultimaposicion= (cantidad_elementos -1) o lista[-1]
7) para acceder a los elementos utilizamos las posiciones; lista(posicion)

no exiten indices sin elementos en python

los metodos con __nombre__. se les llama magic built-in o dunders

"""

lista1 = [1,2,3,4]
print(f"La lista es: {lista1}")
print(f"nueva lista {[5,"Hola Mundo",7]}")

colores = ["verde","rojo","rosa","azul"] 
#¿Cuántos elementos tiene?: 4 elementos, por lo tanto el tamaño de esta lista es 4 -> el tamaño de la lista
#la ultima posicion = 4-1 -> 3

#print (la lista [la posición])
print(colores[0])#verde
print(colores[1])#rojo
print(colores[2])#rosa
print(colores[3])#azul
#print(colores[4]) #IndexError: list index out of range, cuando se imprime un dato fuera de la lista

#mismos elementos, pero a la inversa
print(colores[-1])#azul
print(colores[-2])#rosa
print(colores[-3])#rojo
#print(colores[-5])#IndexError: list index out of range, posicion que no exite, esta fuera de rango

##METODOS##
#print(colores.__dir__())#mostrar todos los metodos que contiene la lista

#Método append()
#append()-> agregar un elemento al final de la lista
colores.append("amarillo")#agregar un elemento
print(colores)#colores['verde', 'rojo', 'rosa', 'azul', 'amarillo']

#Método insert()
#insert(indice,elemento)-> agregar el elemento en una posicion especifica
# y si esta utilizada por otro elemento, este es desplazado en una posicion más

colores.insert(0,"blanco")
print(colores)#['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo']  
colores.insert(6,"negro")
print(colores)#['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro']
colores.insert(18,"cafe")#si el indice no existe le asigna la ultima posicion
print(colores)#['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro', 'cafe', 'cafe']
colores.insert(0,"cafe")


#Método pop()
#pop([indice])->elimina un elemento dentro de la lista
colores.pop(3)#elimina el color rosa de la lista
print(colores)#['blanco', 'verde', 'rojo', 'azul', 'amarillo', 'negro', 'cafe']


#Método remove()

#remove()->elimina un elemento especifico, pero el primero que encuentre
#colores.remove("cafe")
#print(colores)#['blanco', 'verde', 'rojo', 'azul', 'amarillo', 'negro']  
#colores.remove("cafes")#ValueError: list.remove(x): x not in list

#Método reverse

#reverse()->invierte el orden de los elementos de la lista,PERMANENTE
colores.reverse()
print(colores)#['cafe', 'negro', 'amarillo', 'azul', 'rojo', 'verde', 'blanco']

#Método sort()-> ordena los elementos de forma ascendente/alfabetico por defecto

colores.sort()
print(colores)#['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rojo', 'verde']


"""
En Python, cuando asignas una lista a otra variable utilizando el operador de asignación (=), estás creando una nueva 
referencia a la misma lista en la memoria, no una nueva lista. Por lo tanto, ambas variables (lista1 y lista2)
apuntan a la misma ubicación de memoria, lo que significa que cualquier cambio realizado en una de las variables 
también afectará a la otra.

lista2=lista1 ESTO NO ES UNA COPIA O RESPALDO DE LA LISTA, APUNTA AL MISMO ESPACIO DE MEMORIA
print(lista2)
lista2.append(5)
print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")
print(lista1)
"""

lista2 = lista1 #ESTO NO ES UNA COPIA O RESPALDO DE LA LISTA, APUNTA AL MISMO ESPACIO DE MEMORIA
lista3 = lista1.copy() #SI ES UN RESPLADO DE LOS DATOS
lista4 = lista1[:] #SI ES UN RESPLADO DE LOS DATOS (slice)
lista5 = list(lista1)#SI ES UN RESPLADO DE LOS DATOS, metodo o función list
lista7 = lista1 + [] #SI ES UN RESPLADO DE LOS DATOS,PERO NO ES TAN LIMPIO
lista8 = lista1 * 1 #para repetir listas


print(lista2)
lista2.append(5)
print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")
print(f"lista 3 {lista3}")
print(f"lista 4 {lista4}")
print(f"lista 5 {lista5}")

#Método sorted()

#sorted(lista, reverse= True) -> ordena descendentemente, no es permanente
print(sorted(colores,reverse=True))#['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rojo', 'verde']
print(sorted(colores))#['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rojo', 'verde']
print(colores)

#Método index()

#index() -> retorna el indice del elemento
print(colores.index('azul'))#1
print(colores.index('negro'))#4
#print(colores.index('pink'))#ValueError: 'pink' is not in list

colores.clear()# eliminar todos los elementos de la lista
print(colores)# lista vacia, de tamaño cero

print(len(colores))#0

##OPERACIONES#
lista6 = [20,30,40,50]

lista_concatenada = lista1 + lista6 
print(lista1)
print(lista6)
print(lista7)
print(lista8)
print(lista_concatenada)
lista6.append(60)
print(lista_concatenada)


#colores[8]="gris"
#print(colores)#