from os import system 
import suma
import resta as r
from input import captura_de_datos


print("Calculadora básica\n")
#opcion = input("Que operacion desea realizar? 1)")

print("Seleccione opcion a realizar")
print("1.-Sumar")
print("2.-Restar")
print("0.-Salir")
opcion = int( input ("> "))

system('cls')#para windows
if opcion == 1:
    x , y = captura_de_datos()
    suma.sumar(x,y)
    
elif opcion == 2:
    x , y = captura_de_datos()
    r.restar(x,y)
    
elif opcion == 0:
    print("Hasta luego, regrese pronto")
else:
    exit()
    print("Opcion invalida")





