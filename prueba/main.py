import templates
from api_get import request_get

url = "https://aves.ninjas.cl/api/birds" 
response = request_get(url)

if response is not None:
    contenido_html = ""

    for dicc in response:
        contenido_html += templates.card_template.substitute(
            titulo_esp=dicc["name"]["spanish"],
            titulo_en=dicc["name"]["english"],
            url_img=dicc["images"]["full"]
        )

    html_final = templates.main_template.substitute(content=contenido_html)

    file_name = "aves_chile.html"  # Nombre de archivo.

    with open(file_name, "w") as file:
        file.write(html_final)
    print("Archivo HTML generado correctamente.")
else:
    print("No se pudo obtener datos de la API.")