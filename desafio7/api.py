import requests
import json
# Paso 1: Configuración inicial para realizar las solicitudes a la API de usuarios.
URL_BASE = "https://reqres.in/api/users" # URL de la API de usuarios.

def hacer_solicitud(metodo, endpoint, payload=None):# Función para realizar solicitudes HTTP a la API.
    url = f"{URL_BASE}/{endpoint}"
    response = requests.request(metodo, url, json=payload) # Realizar la solicitud HTTP utilizando el método especificado.
    if metodo == "DELETE": # Si el método es DELETE, solo devolver el código de estado.
        return response.status_code
    else:  
        return response.json(), response.status_code
# Paso 2: Requerimientos
# Requerimiento 1: Obtener la información de los usuarios retornada por la API.
users_data, users_status_code = hacer_solicitud("GET", "")
if users_data:
    print("Datos de los usuarios:\n", json.dumps(users_data, indent=4))
print("Código de respuesta: ", users_status_code)

# Requerimiento 2: Crear un usuario llamado Ignacio y de trabajo profesor.
created_user, created_status_code = hacer_solicitud("POST", "", {"name": "Ignacio", "job": "Profesor"})
if created_user:
    print("Usuario creado:\n", json.dumps(created_user, indent=4))
print("Código de respuesta: ", created_status_code)

# Requerimiento 3: Actualizar un usuario llamado morpheus para que tenga un campo residence igual a "zion".
updated_user, updated_status_code = hacer_solicitud("PUT", "2", {"residence": "zion"})
if updated_user:
    print("Usuario 'morpheus' actualizado:\n", json.dumps(updated_user, indent=4))
print("Código de respuesta: ", updated_status_code)

# Requerimiento 4: Eliminar un usuario llamado Tracey e imprimir el código de respuesta.
deleted_status_code = hacer_solicitud("DELETE", "3")
if deleted_status_code == 204:
    print("Usuario Tracey eliminado. Código de respuesta:", deleted_status_code)