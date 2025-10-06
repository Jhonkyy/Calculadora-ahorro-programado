# Calculadora de Ahorro Programado 
Este es un programa en Python que calcula el ahorro programado para alcanzar una meta financiera.
Permite al usuario ingresar una meta de ahorro y el tiempo en meses para alcanzarla.
El programa calcula el monto a ahorrar mensualmente y muestra un resumen de los resultados.

## ¿Como funciona?
 * __Prerequisitos:__ tener python instalado en una version 3.13 o superior y tener el proyecto descargado.
 * __Ejecucion:__ 
Para ejecuturar la interfaz por consola estando desde el directorio main ingrese el siguiente comando
````bash
py src/view/interfaz.py
````

## Estructura del proyecto
```bash
Calculadora-ahorro-programado/
│── src/                   # Código fuente
│   │── model/             # Modelo
│   │   │── ahorro.py      # Funciones de cálculo de ahorro
│   │── view/              # Interfaz de usuario
│       │── interfaz.py    # Interfaz de consola (CLI)
│── test/                  # Pruebas unitarias
│   │── test_ahorro.py
│── README.md              # Documentación
````
## ¿Como correr las pruebas?
Para ejecuturar la interfaz por consola estando desde el directorio main ingrese el siguiente comando:
````bash
py test/test_ahorro.py
````


## Autores
Andre Rivas Garcia
