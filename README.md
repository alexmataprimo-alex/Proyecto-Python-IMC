# Proyecto M3 - Simulación de Máquina de Galton

Simulación en Python del recorrido de 3,000 canicas a través de un tablero de 12 niveles de obstáculos y visualización de resultados mediante un histograma con `matplotlib`.

## Lógica de la Máquina de Galton
La Máquina de Galton consiste en una rejilla vertical de filas de clavos donde caen canicas desde la parte mas alta:
- En cada nivel, la canica choca con un obstáculo y se desvía hacia la **izquierda** o hacia la **derecha**.
- contar los movimientos hacia la derecha determina en qué contenedor inferior cae cada canica.
- Al repetir el proceso muchas  veces , los resultados tienden a concentrarse en los contenedores centrales, formando una distribución acampanada similar a la distribución binomial/normal.

## Estructura del proyecto
- `ALEJANDRO_MATA_proyectoM3.py`: contiene las funciones `simular_canica`, `ejecutar_simulacion_masiva`, `graficar_resultados` y `main`.
- `README.md`: documentación general del proyecto y reflexión técnica.

## Ejecución
Desde la carpeta del proyecto en terminal:

```powershell
py ALEJANDRO_MATA_proyectoM3.py