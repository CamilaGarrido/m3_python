from string import Template

# Template principal del HTML
main_template = Template("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="Camila Garrido" content="Prueba Modulo 3 Python">
    <meta name="description" content="Fundamentos de programacion en Python">
    <meta name="keywords" content="Programacion,API,HTML">
    <title>Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

        <style>
            .container {
                text-align: center;
                padding-top: 30px; /* Ajusta el valor de arriba del titulo */
            }
            .card {
                margin-bottom: 30px; /* valor del margen */
            }
            .card-img-top {
                height: 540px; /* Altura*/
            }
            body {
                background-color:#D8C3A5; /* Color de fondo para toda la página */
            }
        </style>
    </head>

<body>
<body>
    <div class="container text-center">
        <h1>Aves de Chile</h1>
        <br>
        <div class="row">
            $content
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>                   
""")

# Template para cada tarjeta de ave
card_template = Template("""
<div class="col-12 col-sm-6 mb-3 mb-sm-0">
    <div class="card">
        <img src="$url_img"
            class="card-img-top" alt="$titulo_esp" width="200">
        <div class="card-body">
            <h5 class="card-title">$titulo_esp</h5>
            <p class="card-text">$titulo_en</p>
        </div>
    </div>
</div>
""")
