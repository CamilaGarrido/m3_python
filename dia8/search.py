import random,sys

buscar = int(sys.argv[1])
print(buscar,type(buscar))

#RANDOM.SHUFFLE => DESORDENAR LA LISTA
lista_numeros = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista_numeros)

print(lista_numeros)
posicion = 0
for numero in lista_numeros:
    
    if buscar == numero:
        print("Numero encontrado!!")
        print(f"la posicion es {posicion}")
        break #salir de for
    posicion+=1    #incrementar en 1

print("fin del programa")