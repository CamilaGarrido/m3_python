import random,sys

buscar = int(sys.argv[1])
print(buscar,type(buscar))

#RANDOM.SHUFFLE => DESORDENAR LA LISTA
lista_numeros = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista_numeros)

print(lista_numeros)
""" 
posicion = 0
for numero in lista_numeros:
    if buscar == numero:
        print("Numero encontrado!!")
        print(f"la posicion es {posicion}")
        break #salir de for
    posicion+=1    #incrementar en 1
"""

for position, elemento in enumerate(lista_numeros):
# Si el elemento es igual a lo que buscamos terminamos el ciclo
    if elemento == buscar:
        print("¡Elemento encontrado! Se terminará del ciclo")
        break
    else:
# Si es que no es el elemento buscado lo reportamos
        print("Elemento no encontrado")

print("Ha terminado el ciclo")
print(f'El elemento {buscar} se encontró en la posición {position}')
print(f'La lista mezclada es: {lista_numeros}')