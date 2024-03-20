estimulo = input("Responde a estimulos [s/n]: ").lower()# s; n; S; N;

if estimulo == "s":
    print("Llevar al hospital mas cercano")
else: 
    print("Abrir la via Aérea")
    respira = input("¿Respira? [s/n]: ").lower()
    if respira == "s":
        print("Permitirle posicion de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")
    
    ambulancia="n"
    while ambulancia == "n":
        signos_vida = input("¿Tiene signo de vida? [s/n]: ").lower()
        
        if signos_vida == "s":
            print("Reevaluar a la espera de la ambulancia")
        else:
            print("Administrar comprensiones toracicas hasta que llegue la ambulancia")
            
        ambulancia=input("¿Lllego la ambulancia? [s/n]: ").lower()    
print("Fin del programa")