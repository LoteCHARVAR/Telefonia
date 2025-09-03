from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def informacion(request):
    pagina = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiénes Somos - Teleconecta</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: #f4f8fb;
            color: #333;
        }

        header {
            background-color: #0077cc;
            color: white;
            padding: 2rem;
            text-align: center;
        }

        main {
            padding: 2rem;
            max-width: 900px;
            margin: auto;
        }

        h1 {
            margin-bottom: 1rem;
        }

        p {
            line-height: 1.6;
            margin-bottom: 1.5rem;
        }

        .btn-volver {
            display: inline-block;
            padding: 0.8rem 1.5rem;
            background-color: #0077cc;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }

        .btn-volver:hover {
            background-color: #005fa3;
        }

        footer {
            text-align: center;
            padding: 1rem;
            margin-top: 3rem;
            background-color: #e0e0e0;
            color: #666;
        }
    </style>
</head>
<body>

    <header>
        <h1>Quiénes Somos</h1>
    </header>

    <main>
        <h2>Sobre Teleconecta</h2>
        <p>
            En <strong>Teleconecta</strong>, somos una empresa líder en soluciones de telefonía y conectividad en todo el país.
            Desde nuestra fundación en 2010, trabajamos incansablemente para conectar a las personas, acercando
            la tecnología con un servicio confiable, rápido y accesible.
        </p>

        <p>
            Nuestro equipo está compuesto por profesionales apasionados por la innovación, comprometidos con la excelencia
            en atención al cliente y la mejora continua de nuestros servicios. Ya sea para empresas o particulares,
            brindamos soluciones adaptadas a cada necesidad.
        </p>

        <p>
            Gracias por confiar en nosotros.
        </p>

        <a href="/" class="btn-volver">← Volver a la Página Principal</a>
    </main>

    <footer>
        © 2025 Teleconecta. Todos los derechos reservados.
    </footer>

</body>
</html>

"""
    return HttpResponse(pagina)