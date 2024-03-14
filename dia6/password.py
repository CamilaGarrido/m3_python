contrasenia= input("Ingrese una contraseña (min 6 caracteres)\n")

#string.count("") 
if contrasenia.count(" ") > 0:
    print("El password no puede contener espacios")
elif contrasenia == "12345":
    print("El password es incorrecto")
elif len(contrasenia) < 6:
    print("El password es demasiado corto")
    
else:
    print("El formato de password es correcto")

#12345

"""
else:     
    #len -> contar los caracteres
    if len(contrasenia) < 6:
        print("El password es demasiado corto") 
        
        if, elif, else son condicionales, sirven para validar (condisionar lo que este ocurriendo con nuestros codigos)
"""