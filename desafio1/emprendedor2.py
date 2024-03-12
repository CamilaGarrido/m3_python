# Paso 1: fórmula de utilidades con usuarios normales y premium
def calcular_utilidades(precio_suscripcion_normal, num_usuarios_normal, precio_suscripcion_premium, num_usuarios_premium, gastos_totales):
    utilidades = (precio_suscripcion_normal * num_usuarios_normal + precio_suscripcion_premium * num_usuarios_premium) - gastos_totales
    return utilidades

# Paso 2: Solicitar datos al usuario
precio_suscripcion_normal = float(input("Ingrese el precio de suscripción para usuarios normales: "))
num_usuarios_normal = int(input("Ingrese el número de usuarios normales: "))
precio_suscripcion_premium = 1.5 * precio_suscripcion_normal  # Precio para usuarios premium es 50% más alto
num_usuarios_premium = int(input("Ingrese el número de usuarios premium: "))
gastos_totales = float(input("Ingrese los gastos totales: "))

# Paso 3: Verificar si los valores ingresados son válidos
if precio_suscripcion_normal <= 0 or num_usuarios_normal < 0 or precio_suscripcion_premium <= 0 or num_usuarios_premium < 0 or gastos_totales < 0:
    print("Advertencia: Los valores ingresados podrían impedir un buen funcionamiento del programa.")
    print("Por favor, asegúrese de ingresar valores válidos.")
else:
    # Paso 4: Calcular utilidades con usuarios normales y premium
    utilidades = calcular_utilidades(precio_suscripcion_normal, num_usuarios_normal, precio_suscripcion_premium, num_usuarios_premium, gastos_totales)

    # Paso 5: Mostrar el resultado
    print(f"Las utilidades del proyecto son: {utilidades}")
