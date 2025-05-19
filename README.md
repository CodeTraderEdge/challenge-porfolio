# Portfolio Optimizer

Este proyecto implementa un optimizador de portafolio en Python. Su objetivo es construir una cartera de inversión eficiente que **maximice el retorno esperado**, sujeto a un nivel de riesgo aceptable y a límites de peso por activo.

---

## ¿Qué hace?

Dado un conjunto de retornos históricos, el optimizador:

- Calcula el retorno promedio y la matriz de covarianza.
- Utiliza optimización numérica para encontrar la mejor combinación de activos.
- Respeta las restricciones definidas de riesgo y pesos.
- Devuelve un portafolio óptimo con pesos redondeados a 6 decimales.
- Si el archivo que se sube contiene una fila de datos vacia, no le agregamos 0 sino que lo que hacemos es eliminar toda la fila porque ponerle 0 afectaría de forma considerable el modelo, por lo cual lo elimino para que tengamos datos reales.

---

## Método de Optimización

Utilizamos el modelo de **Media-Varianza de Markowitz**, uno de los enfoques más clásicos y robustos en la teoría moderna de portafolio. La idea con esto es poder sacarle mayor partido a un porfolio y mientras mas datos históricos tengamos mucho mas factible son los resultados que va a arrojar para poder hacer la división del 100% del capital y generar el porfolio.

### Criterio de Optimalidad

> **Maximizar el retorno esperado del portafolio**

Este criterio se basa en la idea de que, dados ciertos límites de riesgo y de asignación, queremos que nuestra cartera rinda lo mejor posible en promedio.  
Es un enfoque simple, elegante y poderoso.

> Me gusta esta estrategia porque es intuitiva, directa y refleja una mentalidad proactiva hacia la rentabilidad.

---

## Detalles Técnicos

- **Lenguaje**: Python
- **Librerías**: `numpy`, `pandas`, `scipy.optimize`
- **Modelo**: Optimización convexa con restricciones
- **Métrica de riesgo**: Varianza del portafolio
- **Restricciones**:
  - Suma de pesos = 1
  - Riesgo ≤ `risk_level`
  - Peso individual ≤ `max_weight`
- **Salida**: Diccionario con tickers y pesos óptimos redondeados a 6 decimales

---

## Ejemplo de uso vía API con curl

Para usar el optimizador a través de la API REST, puedes enviar un request `POST` con el archivo CSV de retornos y los parámetros de riesgo y peso máximo.

Ejemplo:

```bash
curl --location 'https://challenge-porfolio-production.up.railway.app/optimize-portfolio' \
--header 'Content-Type: multipart/form-data' \
--form 'file=@returns.csv"' \
--form 'risk_level="1.0"' \
--form 'max_weight="0.15"'
```
