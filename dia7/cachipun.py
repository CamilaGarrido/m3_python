import sys 
import random 

opcion_jugador = sys.argv[1].lower() #TIJERAS o tijeras o TiJerAs

if(opcion_jugador !="piedra" and opcion_jugador !="papel" and opcion_jugador !="tijeras" ):
    print("Argumento invalido: Debe ser piedra o papel o tijeras")
else:#ingreso valido de los parametros
    print("continua el programa")
    
if(opcion_jugador !="piedra" or opcion_jugador !="papel" or opcion_jugador !="tijeras" ): 
    print("Datos ingresados correctamente!!")

    print(f"La opcion del usuario es {opcion_jugador}")
    
    #random -> elije al azar de una lista
    opcion_maquina = random.choice(['piedra','papel','tijeras'])
    print(f"La opcion del computador es {opcion_maquina}")

    if opcion_jugador.lower() == opcion_maquina.lower():
        print("Empate")
    elif(opcion_jugador == "piedra" and opcion_maquina == "tijeras") or (opcion_jugador == "tijeras" and opcion_maquina == "papel") or (opcion_jugador == "papel" and opcion_maquina == "piedra"):
        print("Jugado gana")
    else:
        print("Perdiste!!")

else:
    print("Argumento invalido: Debe ser piedra o papel o tijeras")