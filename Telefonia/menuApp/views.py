from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menu(request):
    pagina = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Teleconecta - Página Principal</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      background: #f4f8fb;
      color: #333;
    }

    header {
      background-color: #0077cc;
      padding: 1.5rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: white;
    }

    .logo {
      font-size: 1.8rem;
      font-weight: bold;
    }

    nav a {
      color: white;
      text-decoration: none;
      margin-left: 1.5rem;
      font-weight: 600;
      transition: color 0.3s ease;
    }

    nav a:hover {
      color: #cce6ff;
    }

    .banner {
      position: relative;
      width: 100%;
      height: 300px;
      background: url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1350&q=80') center center/cover no-repeat;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
      text-shadow: 0 0 8px rgba(0,0,0,0.7);
    }

    .banner h2 {
      font-size: 2.8rem;
      background-color: rgba(0, 119, 204, 0.7);
      padding: 1rem 2rem;
      border-radius: 8px;
      margin: 0;
    }

    main {
      max-width: 900px;
      margin: 3rem auto;
      padding: 0 1rem;
      text-align: center;
    }

    h1 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
      color: #0077cc;
    }

    p {
      font-size: 1.2rem;
      margin-bottom: 2rem;
      line-height: 1.6;
    }

    .btn {
      display: inline-block;
      background-color: #0077cc;
      color: white;
      padding: 1rem 2rem;
      border-radius: 6px;
      font-weight: 600;
      text-decoration: none;
      box-shadow: 0 3px 6px rgba(0, 119, 204, 0.4);
      transition: background-color 0.3s ease;
      margin-top: 1rem;
    }

    .btn:hover {
      background-color: #005fa3;
    }

    footer {
      text-align: center;
      padding: 1rem;
      margin-top: 4rem;
      background-color: #e0e0e0;
      color: #666;
      font-size: 0.9rem;
    }

    @media (max-width: 600px) {
      .banner {
        height: 180px;
      }

      .banner h2 {
        font-size: 1.8rem;
        padding: 0.6rem 1.2rem;
      }

      h1 {
        font-size: 2rem;
      }

      p {
        font-size: 1rem;
      }
    }
  </style>
</head>
<body>
  <header>
    <div class="logo">Teleconecta</div>
    <nav>
      <a href="informaciones/">Quiénes Somos</a>
      <a href="servicios/">Servicios</a>
      <a href="servicios/precios">Precios</a>
    </nav>
  </header>

  <section class="banner">
    <h2>Conectamos tu mundo</h2>
  </section>

  <main>
    <h1>Bienvenidos a Teleconecta</h1>
    <p>Tu mejor opción en telefonía e Internet. Conectamos a personas y empresas con la tecnología del futuro.</p>
    <a href="servicios/" class="btn">Ver nuestros servicios</a>
  </main>

  <footer>
    © 2025 Teleconecta. Todos los derechos reservados.
  </footer>
</body>
</html>


    """
    return HttpResponse(pagina)