#paso 1: Calculo del factorial de un numero
def factorial(numero):#5! = 5*4*3*2*1
    valor = 1 # variable acumuladora
    for n in range(1,numero+1):#1,2,3,4,5
        valor = valor * n
    return valor

#print("el factorial es:",factorial(6))

#paso 2: Una función que calcule la productoria
def productoria(lista):
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor

#print(productoria([4, 6, 7, 4, 3]))

#paso 3: Una función que permita controlar los cálculos. 
# Esta función se debe invocar de la siguiente manera:
def calcular(**parametros): #* tupla; ** diccionario 
    for clave,valor in parametros.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {factorial(valor)}")
        else:
            print(f"La productoria de {valor} es {productoria(valor)}")

#paso 4: invocacion al metodo
calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)