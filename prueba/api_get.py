# Paso 1: Importar los módulos.
import requests  # Para realizar solicitudes HTTP.
import json      # Para trabajar con datos json.

#Paso 2: Definir la función para hacer una solicitud GET a una URL y obtener los datos json.
def request_get(url):
    response = requests.get(url) # Realizar la solicitud GET a la URL
    if response.status_code == 200:# Verificar si la solicitud fue exitosa.
        return json.loads(response.text)  # Si la solicitud fue exitosa, convertir el texto de la respuesta a un diccionario json.
    else:
        print("Error en la solicitud:", response.status_code)# Si la solicitud no fue exitosa, imprimir un mensaje de error con el código de estado HTTP
        return None       

# Paso 3: Función principal para probar la solicitud GET
if __name__ == "__main__":
    url = "https://aves.ninjas.cl/api/birds"    # URL a la que se realizará la solicitud GET.
    response = request_get(url)# Realizar la solicitud GET y almacenar la respuesta.

    if response is not None:# Verificar si se obtuvieron datos de la solicitud.
        print("Obtención correcta")  # Si se obtuvieron datos, imprimir un mensaje de éxito y los datos json.
        print(response)
    else:
        print("Error en la solicitud")# Si no se obtuvieron datos, imprimir un mensaje de error.