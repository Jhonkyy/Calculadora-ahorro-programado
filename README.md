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

Instalar la librería principal:
```bash
pip install psycopg2