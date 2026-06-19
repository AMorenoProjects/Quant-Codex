El trading de pares es una estrategia fundamental en la arquitectura de fondos cuantitativos. Su objetivo principal es aislar el riesgo sistémico (el movimiento general del mercado) para operar exclusivamente la ineficiencia matemática entre dos activos.

A continuación, se detalla la mecánica técnica y matemática detrás de los conceptos mencionados.

### 1. Neutralidad de Mercado (Market Neutrality)

Cuando el texto menciona que la estrategia busca ganancias "independientemente de si el mercado en general sube o baja", se refiere a la neutralización de la exposición o **Beta ($\beta$)**.

Si tienes una posición larga (comprada) en el Activo A por 10.000$ y una posición corta (vendida) en el Activo B por 10.000$, tu exposición neta al mercado es cercana a cero. Si ocurre un _crash_ financiero global y ambos activos caen un 10%, perderás dinero en la posición larga, pero ganarás exactamente lo mismo en la posición corta. El capital está protegido de la dirección del mercado; el único riesgo que asumes es que la relación de precios entre A y B se rompa permanentemente.

### 2. Detección de la Anomalía: El Spread y el Z-Score

El "diferencial" no suele ser una simple resta de precios, ya que los activos pueden tener volatilidades distintas. Se calcula utilizando un ratio de cobertura (_Hedge Ratio_), típicamente derivado de una regresión lineal (Mínimos Cuadrados Ordinarios).

La ecuación base del spread en el instante temporal $t$ es:

$$Spread_t = P_{A,t} - \beta P_{B,t}$$

Donde $P_{A,t}$ y $P_{B,t}$ son los precios de los activos y $\beta$ es el ratio de cobertura.

Para estandarizar este spread y saber cuándo la divergencia es estadísticamente operables, los algoritmos lo convierten en un **[QT - 10.Z-Score](../maths/zscore.md)**. El [QT - 10.Z-Score](../maths/zscore.md) mide a cuántas desviaciones estándar ($\sigma$) se encuentra el spread actual de su media histórica ($\mu$):

$$Z_t = \frac{Spread_t - \mu}{\sigma}$$

- Si el [QT - 10.Z-Score](../maths/zscore.md) llega a **+2.0**, significa que el Activo A está inusualmente caro respecto al B. El motor lanza la señal: Vender A (Corto) / Comprar B (Largo).
    
- Si el [QT - 10.Z-Score](../maths/zscore.md) llega a **-2.0**, el Activo A está inusualmente barato. Señal: Comprar A (Largo) / Vender B (Corto).
    
- Cuando el [QT - 10.Z-Score](../maths/zscore.md) vuelve a **0** (la media), se cierran ambas posiciones, capturando la ganancia generada por la convergencia.
    

### 3. El Falso Amigo: Correlación vs. Cointegración

Esta es la trampa principal en el diseño de estrategias.

- **Correlación:** Mide similitud de trayectorias a corto plazo. Ejemplo: Dos coches que viajan a 100 km/h en la misma autopista. Están altamente correlacionados hoy. Pero si uno va a Madrid y el otro a Barcelona, mañana estarán a cientos de kilómetros de distancia. Si operas esto, la divergencia te liquidará la cuenta.
    
- **Cointegración:** Es un ancla matemática a largo plazo. La analogía clásica en econometría es **el borracho y su perro atado con una correa**. Ambos caminan de forma errática y aleatoria (_random walk_). No puedes predecir hacia dónde dará el siguiente paso el borracho ni el perro (baja correlación a corto plazo). Sin embargo, como están unidos por una correa, la distancia máxima entre ellos está limitada. Invariablemente, la tensión de la correa obligará al perro a volver hacia el dueño, o al dueño hacia el perro (reversión a la media). La cointegración es esa correa.
    

### 4. Filtros Dinámicos (Kalman Filter)

El texto menciona que los coeficientes deben actualizarse en tiempo real. Los mercados no son estáticos (no son estacionarios). Un ratio de cobertura ($\beta$) calculado con datos de 2022 probablemente no funcione en 2026.

En lugar de recalcular el modelo completo cada mes en lotes (_batch processing_), se utilizan algoritmos recursivos como el **Filtro de Kalman**. Este algoritmo toma cada nuevo precio que llega del mercado (tick o barra) y ajusta ligeramente el ratio de cobertura y la media esperada en microsegundos, adaptando la "correa" de la analogía a las condiciones actuales de volatilidad sin requerir un recálculo masivo en el histórico.