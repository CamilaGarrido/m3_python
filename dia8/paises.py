# Lista de países y cantidad de usuarios
paises = ["México", "Chile", "Argentina"]
usuarios = [70, 50, 55]

# Filtrar los países con menos de 60 usuarios
# Comprensión de lista para crear una lista de tuplas
# Cada tupla contiene el país y el número de usuarios correspondiente, solo si el número de usuarios es menor que 60.
paises_con_menos_de_60_usuarios = [(pais, num_usuarios) for pais, num_usuarios in zip(paises, usuarios) if num_usuarios < 60]

# Imprimir los países con menos de 60 usuarios
# Iterar sobre la lista de tuplas y para cada tupla se imprime el país seguido por el número de usuarios, utilizando el formato de cadena f-string.
print("Países con menos de 60 usuarios:")
for pais, num_usuarios in paises_con_menos_de_60_usuarios:
    print(f"{pais}: {num_usuarios}")