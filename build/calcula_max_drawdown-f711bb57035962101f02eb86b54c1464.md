**Contexto:** En la evaluación de riesgo de algoritmos cuantitativos, el Maximum Drawdown (MDD) cuantifica la mayor pérdida porcentual sufrida desde el pico histórico más alto del capital hasta el valle más bajo posterior, antes de que se alcance un nuevo máximo.

**Tarea:** Escribe una función en Python llamada `calculate_max_drawdown` que tome una serie temporal de precios y retorne el valor exacto del Maximum Drawdown expresado como un número decimal flotante negativo (por ejemplo, -0.125 para indicar una caída máxima del 12.5%).

```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_max_drawdown(price_series: pd.Series) -> float:
	running_max = price_series.cummax()
	
	drawdown = (price_series - running_max) / running_max
	
	max_drawdown = drawdown.min()
	
return max_drawdown
	
np.random.seed(42) daily_returns = np.random.normal(0.001, 0.02, 252) price_index = 100 * (1 + daily_returns).cumprod() 

prices = pd.Series(price_index)

mdd = calculate_max_drawdown(prices) 

print(f"El Maximum Drawdown es: {mdd:.2%}")

```