from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def servicios(request):
    pagina = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servicios - Teleconecta</title>
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
            max-width: 1000px;
            margin: auto;
        }

        h1 {
            margin-bottom: 1rem;
        }

        .servicios {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .servicio {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: transform 0.2s ease;
        }

        .servicio:hover {
            transform: translateY(-5px);
        }

        .servicio h3 {
            margin-top: 0;
            color: #0077cc;
        }

        .btn-volver {
            display: inline-block;
            margin-top: 2rem;
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
        <h1>Servicios</h1>
        <p>Soluciones de conectividad para hogares y empresas</p>
    </header>

    <main>
        <section class="servicios">
            <div class="servicio">
                <h3>Telefonía Móvil</h3>
                <p>Planes flexibles y cobertura nacional con la mejor calidad de voz y datos.</p>
            </div>

            <div class="servicio">
                <h3>Internet de Alta Velocidad</h3>
                <p>Conexiones estables y rápidas con tecnología de fibra óptica y 5G.</p>
            </div>

            <div class="servicio">
                <h3>Telefonía Fija</h3>
                <p>Soluciones de línea fija para hogares y oficinas con tarifas competitivas.</p>
            </div>

            <div class="servicio">
                <h3>Soluciones Empresariales</h3>
                <p>Planes personalizados, centralitas virtuales y soporte técnico dedicado para tu negocio.</p>
            </div>

            <div class="servicio">
                <h3>TV Digital</h3>
                <p>Disfrutá de cientos de canales en alta definición con contenido exclusivo.</p>
            </div>
        </section>

        <a href="/" class="btn-volver">← Volver a la Página Principal</a>
    </main>

    <footer>
        © 2025 Teleconecta. Todos los derechos reservados.
    </footer>

</body>
</html>
    """
    return HttpResponse(pagina)

def precios(request):
    pagina = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Precios - Teleconecta</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f4f8fb;
      margin: 0;
      padding: 0;
      color: #333;
    }

    header {
      background-color: #0077cc;
      color: white;
      padding: 2rem;
      text-align: center;
    }

    main {
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1rem;
    }

    h1 {
      margin-bottom: 1rem;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1.5rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      background-color: white;
      border-radius: 8px;
      overflow: hidden;
    }

    th, td {
      padding: 1rem;
      text-align: center;
      border-bottom: 1px solid #ddd;
    }

    th {
      background-color: #0077cc;
      color: white;
      font-weight: 600;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:hover {
      background-color: #f1f9ff;
    }

    .btn-volver {
      display: inline-block;
      margin-top: 2rem;
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
    <h1>Planes y Precios</h1>
    <p>Encuentra el plan que mejor se adapte a tus necesidades</p>
  </header>

  <main>
    <table>
      <thead>
        <tr>
          <th>Plan</th>
          <th>Minutos</th>
          <th>Datos</th>
          <th>SMS</th>
          <th>Precio Mensual</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Básico</td>
          <td>100 minutos</td>
          <td>2 GB</td>
          <td>100 SMS</td>
          <td>$10 USD</td>
        </tr>
        <tr>
          <td>Estándar</td>
          <td>300 minutos</td>
          <td>10 GB</td>
          <td>500 SMS</td>
          <td>$20 USD</td>
        </tr>
        <tr>
          <td>Premium</td>
          <td>Minutos ilimitados</td>
          <td>50 GB</td>
          <td>SMS ilimitados</td>
          <td>$40 USD</td>
        </tr>
        <tr>
          <td>Empresarial</td>
          <td>Minutos ilimitados</td>
          <td>100 GB</td>
          <td>SMS ilimitados</td>
          <td>$70 USD</td>
        </tr>
      </tbody>
    </table>

    <a href="/" class="btn-volver">← Volver a la Página Principal</a>
  </main>

  <footer>
    © 2025 Teleconecta. Todos los derechos reservados.
  </footer>
</body>
</html>

    """
    return HttpResponse(pagina)