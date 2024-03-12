# Paso 1: Solicitar datos adicionales al usuario
precio_suscripcion = float(input("Ingrese el precio de suscripción: "))
num_usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales: "))
utilidades_anterior = float(input("Ingrese las utilidades del año anterior: "))

# Paso 2: Verificar si los valores ingresados son válidos
if precio_suscripcion <= 0 or num_usuarios < 0 or gastos_totales < 0 or utilidades_anterior < 0:
    print("Advertencia: Los valores ingresados podrían impedir un buen funcionamiento del programa.")
    print("Por favor, asegúrese de ingresar valores válidos.")
else:
# Paso 3: Calcular las utilidades actuales
    utilidades_actuales = precio_suscripcion * num_usuarios - gastos_totales

# Paso 4: Calcular la razón entre las utilidades actuales y las del año anterior
    razon_utilidades = utilidades_actuales / utilidades_anterior

# Paso 5: Mostrar el resultado
    print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")