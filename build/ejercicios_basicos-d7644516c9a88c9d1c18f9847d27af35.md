### Ejercicio 1: Cálculo de Retornos Simples

**Contexto:** Los modelos cuantitativos analizan la variación porcentual de los activos, no sus precios estáticos. **Datos de entrada:**

```python
import pandas as pd
precios = pd.Series([100.0, 101.5, 99.0, 102.0, 103.5])
```

**Tarea:** Escribe el código en `pandas` para calcular la serie de retornos porcentuales diarios. El primer valor de la serie resultante debe ser nulo (`NaN`).

**Respuesta**:
El retorno simple mide cuanto ha variado el precio de un activo en un periodo.
La fórmula es: 

$Retorno = \frac{Precio\_Actual - Precio\_Anterior}{Precio\_Anterior}$

O también se puede simplificar de esta forma:

$Retorno = (\frac{Precio\_Actual}{Precio\_Anterior}) - 1$

```python

import pandas as pd
precios = pd.Series([100.0, 101.5, 99.0, 102.0, 103.5])

# Desplazamos la serie un periodo para obtener el "precio anterior"
precios_anteriores = precios.shift(1)

# Aplicamos la fórmula matemática
retornos = (precios - precios_anteriores) - 1

print(retornos)

```

**Resultados**:

0         NaN
1    0.015000
2   -0.024631
3    0.030303
4    0.014706
dtype: float64


### Ejercicio 2: Microestructura (Spread y Mid-Price)

**Contexto:** Extracción de características de Nivel 1 (L1) del Libro de Órdenes. **Datos de entrada:**

Python

```
best_bid = 150.25
best_ask = 150.30
```

**Tarea:** Crea dos funciones, `get_spread(bid, ask)` y `get_mid_price(bid, ask)`. Calcula ambos valores.

**Resultado**:

```python
best_bid = 150.25
best_ask = 150.30

def get_spread(bid, ask) -> float:
    spread = ask - bid
    return spread  # Devuelve el valor calculado

def get_mid_price(bid, ask) -> float:
    mid = (bid + ask) / 2
    return mid     # Devuelve el valor calculado

# Ejecutamos las funciones, guardamos el valor que retornan en variables y las imprimimos
valor_spread = get_spread(best_bid, best_ask)
print(f"El Spread es: {valor_spread:.2f}")

valor_mid = get_mid_price(best_bid, best_ask)
print(f"El Mid-Price es: {valor_mid:.2f}")
```

**Resultados**:
El Spread es: 0.05
El Mid-Price es: 150.28

### Ejercicio 3: Desequilibrio del Libro de Órdenes (Order Book Imbalance)

**Contexto:** Cuantificar la presión direccional a corto plazo basada en el volumen en espera.

**Fórmula:**

$$Imbalance = \frac{Volumen\_Bid}{Volumen\_Bid + Volumen\_Ask}$$

**Datos de entrada:**

```
vol_bid = 4500  # Total de acciones en el Best Bid
vol_ask = 1500  # Total de acciones en el Best Ask
```

**Tarea:** Calcula el _Imbalance_. Evalúa lógicamente en tu código si el resultado indica presión de compra (valor > 0.5) o presión de venta (valor < 0.5) e imprime la dirección.

**Respuesta**:

```python
vol_bid = 4500  # Total de acciones en el Best Bid
vol_ask = 1500  # Total de acciones en el Best Ask

def imbalance(vol_bid, vol_ask) -> None:
    imbalances = vol_bid / (vol_bid + vol_ask)
    
    if imbalances > 0.5:
        print(f"Compra, el imbalance es: {imbalances:.2f}")
    else:
        print(f"Venta, el imbalance es: {imbalances:.2f}")
        
imbalance(vol_bid, vol_ask)
```

**Resultado**:
Compra, el imbalance es: 0.75

### Ejercicio 4: Ratio de Sharpe Anualizado

**Contexto:** Cálculo de la métrica estándar de rentabilidad ajustada al riesgo.

**Datos de entrada:**

```python
import numpy as np
# Retornos diarios simulados de 20 días
retornos = pd.Series([0.001, -0.002, 0.005, 0.001, -0.001, 
                      0.003, 0.004, -0.002, 0.001, 0.000, 
                      0.002, 0.001, -0.003, 0.002, 0.005, 
                      -0.001, 0.001, 0.002, 0.003, 0.001])
```

**Tarea:**

1. Calcula la media de los retornos diarios.
    
2. Calcula la desviación estándar de los retornos diarios.
    
3. Calcula el Ratio de Sharpe diario (asumiendo tasa libre de riesgo = 0).
    
4. Anualiza el Ratio de Sharpe multiplicando el resultado diario por el factor de ajuste: $\sqrt{252}$
    

Resultado:

```python
import pandas as pd
import numpy as np

# Datos de entrada
retornos = pd.Series([0.001, -0.002, 0.005, 0.001, -0.001, 
                      0.003, 0.004, -0.002, 0.001, 0.000, 
                      0.002, 0.001, -0.003, 0.002, 0.005, 
                      -0.001, 0.001, 0.002, 0.003, 0.001])

# 1. Calcular la media de los retornos diarios
media_diaria = retornos.mean()

# 2. Calcular la desviación estándar (volatilidad) de los retornos diarios
std_diaria = retornos.std()

# 3. Calcular el Ratio de Sharpe diario
# Asumiendo tasa libre de riesgo (Rf) = 0. 
# La fórmula general es: (Media - Rf) / Desviación Estándar
sharpe_diario = media_diaria / std_diaria

# 4. Anualizar el Ratio de Sharpe
# Se asumen 252 días hábiles de trading en un año.
# La volatilidad escala con la raíz cuadrada del tiempo, por eso usamos np.sqrt()
sharpe_anualizado = sharpe_diario * np.sqrt(252)

# Mostrar resultados
print(f"Media diaria: {media_diaria:.5f}")
print(f"Desviación estándar diaria: {std_diaria:.5f}")
print(f"Sharpe Ratio Diario: {sharpe_diario:.5f}")
print(f"Sharpe Ratio Anualizado: {sharpe_anualizado:.2f}")
```

### Ejercicio 5: Señal Z-Score (Reversión a la media básica)

**Contexto:** Uso de la estadística para identificar desviaciones anómalas del precio.

**Fórmula:**

$$Z = \frac{Precio\_Actual - Media}{Desviacion\_Estandar}$$

**Datos de entrada:**

Python

```
precio_actual = 105.0
media_20_dias = 100.0
std_20_dias = 2.0
```

**Tarea:** Calcula el [QT - 10.Z-Score](../maths/zscore.md). Escribe una lógica condicional que imprima "SEÑAL DE VENTA" si el [QT - 10.Z-Score](../maths/zscore.md) es mayor a 2, o "SEÑAL DE COMPRA" si es menor a -2. En caso contrario, imprime "MANTENER".
