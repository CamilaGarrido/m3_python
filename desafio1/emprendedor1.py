# Paso 1: fórmula de utilidades
def calcular_utilidades(precio_suscripcion, num_usuarios, gastos_totales):
    utilidades = precio_suscripcion * num_usuarios - gastos_totales
    return utilidades

# Paso 2: Solicitar los datos al usuario
precio_suscripcion = float(input("Ingrese el precio de suscripción: "))
num_usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales: "))

# Paso 3: Verificar si los valores ingresados son válidos
if precio_suscripcion <= 0 or num_usuarios < 0 or gastos_totales < 0:
    print("Advertencia: Los valores ingresados podrían impedir un buen funcionamiento del programa.")
    print("Por favor, asegúrese de ingresar valores válidos.")
else:
    # Paso 4: Calcular las utilidades
    utilidades = calcular_utilidades(precio_suscripcion, num_usuarios, gastos_totales)

    # Paso 5: Mostrar el resultado
    print(f"Las utilidades del proyecto son: {utilidades}")