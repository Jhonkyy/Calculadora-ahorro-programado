Calculadora de Ahorro Programado 
Este es un programa en Python que permite calcular un ahorro mensual necesario para alcanzar una meta financiera en un plazo determinado. Ahora incluye persistencia en una base de datos PostgreSQL, siguiendo el patrón MVC (Modelo - Controlador - Vista) y pruebas unitarias.

---

 Características principales,
 Cálculo de ahorro programado
 Almacenamiento de los cálculos en PostgreSQL
 Gestión por ID de usuario
 Consultas por ID y usuario
 Patrón MVC
 Pruebas unitarias con Fixtures
 Archivo secret_config.py para conexión (sin exponer datos privados)

---

 Requisitos previos,
Antes de ejecutar el proyecto, debes tener instalado:

| Requisito | Versión recomendada |
|-----------|--------------------|
| Python | 3.10 o superior |
| PostgreSQL | 13 o superior |
| Librerías | psycopg2, unittest |

# Como ejecutar
instala las dependencias:
```bash
pip install -r requirements.txt
```

Corre el codigo de app.py y en el navegador entra a:
http://127.0.0.1:5000


## Autores
Jhon Fredy Asprilla
Cristian Andres Copete
