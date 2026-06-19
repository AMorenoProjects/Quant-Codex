---
status: activo
contenido_clave: ""
consulta: ""
---

-> **0. Índice RAG (Retrieval-Augmented Generation)**

### Fase 1: Fundamentos Matemáticos y Estadísticos

El análisis cuantitativo requiere una base matemática sólida para modelar el comportamiento del mercado.

- **Álgebra Lineal:** Operaciones con matrices, vectores, valores y vectores propios. Fundamental para la optimización de portafolios.
    
- **Cálculo:** Cálculo diferencial e integral, cálculo estocástico (Lema de Itô), optimización matemática.
    
- **Probabilidad y Estadística:** Distribuciones de probabilidad, valor esperado, varianza, pruebas de hipótesis, inferencia bayesiana y cadenas de Markov.
    

### Fase 2: Programación y Gestión de Datos

La capacidad de manipular grandes volúmenes de datos históricos de forma eficiente es crítica.
"Los que quieren salir caro"
- **Python:** Dominio de estructuras de datos y Programación Orientada a Objetos.
    
- **Librerías de Datos:** NumPy (cálculo numérico), Pandas (manipulación de datos tabulares), SciPy (matemáticas avanzadas).
    
- **Análisis de Series Temporales:** Conceptos de estacionariedad, ruido blanco, modelos ARIMA y GARCH, cointegración.
    
- **Bases de Datos:** SQL para datos estructurados, manejo de archivos Parquet/HDF5 para series temporales de alta frecuencia.
    

### Fase 3: Conocimiento Financiero y Microestructura del Mercado

Comprender las reglas del juego y los instrumentos disponibles.

- **Instrumentos Financieros:** Acciones, bonos, divisas (Forex) y derivados (Opciones y Futuros). Modelo de Black-Scholes.
    
- **Microestructura del Mercado:** Funcionamiento del _Limit Order Book_ (LOB), _bid-ask spread_, liquidez, impacto en el mercado (_market impact_) y tipos de órdenes algorítmicas (TWAP, VWAP).
    
- **Teoría de Portafolios:** Frontera eficiente de Markowitz, CAPM.
    
- **Métricas de Rendimiento:** Ratio de Sharpe, Ratio de Sortino, _Maximum Drawdown_ (MDD).
    

### Fase 4: Modelado de Estrategias y Generación de Alpha

El diseño y evaluación teórica de las estrategias comerciales.

- **Familias de Estrategias:** Reversión a la media (_Mean Reversion_), seguimiento de tendencia (_Momentum_), [QT - 12.Cointegración](maths/cointegracion.md) (_StatArb_), arbitraje de volatilidad.

- **Backtesting Riguroso:** Simulación de estrategias sobre datos históricos.

- **Prevención de Errores Comunes:**
    
    - _Look-ahead bias:_ Usar información futura en el pasado.
    - _Survivorship bias:_ Ignorar activos deslistados.
    - _Overfitting:_ Ajustar demasiado el modelo al ruido histórico.
        
- **Costes de Fricción:** Inclusión obligatoria de comisiones y _slippage_ en los modelos.
    

### Fase 5: Machine Learning Aplicado (Avanzado)

Integración de algoritmos predictivos modernos.

- **Aprendizaje Supervisado:** Regresión lineal/logística, Random Forests, Support Vector Machines (SVM) para clasificación de señales.
    
- **Deep Learning:** Redes Neuronales Recurrentes (RNN), LSTMs y Transformers para el análisis de series temporales complejas.
    
- **NLP (Procesamiento de Lenguaje Natural):** Análisis de sentimiento en noticias financieras y reportes de ganancias usando modelos de lenguaje.
    

### Fase 6: Infraestructura, Gestión de Riesgo y Ejecución

El paso de la teoría a operar con capital real en el mercado.

- **Gestión de Riesgos:** Cálculo del _Value at Risk_ (VaR) y _Expected Shortfall_ (ES), dimensionamiento de posiciones (Criterio de Kelly), correlación entre activos.
    
- **Conexión a Mercados:** Integración con APIs de brokers (ej. Interactive Brokers, Alpaca, Binance) mediante REST y WebSockets.
    
- **Infraestructura de Ejecución:** Servidores en la nube (AWS, GCP), contenedores (Docker).
    
- **Baja Latencia (Opcional):** Transición a lenguajes compilados como C++ o Rust para estrategias de alta frecuencia (HFT), optimización de hardware y red.
    

---

## Ecosistema de Herramientas

|**Categoría**|**Herramientas Principales**|**Propósito**|
|---|---|---|
|**Lenguajes**|Python, C++, Rust|Investigación (Python) y Ejecución HFT (C++/Rust).|
|**Backtesting**|VectorBT, Backtrader, Zipline|Simulación vectorizada y basada en eventos.|
|**Plataformas Cloud**|QuantConnect, QuantRocket|Entornos integrados de datos y backtesting.|
|**Machine Learning**|Scikit-learn, PyTorch, TensorFlow|Creación de modelos predictivos de precios o volatilidad.|

## Biblioteca

---

[QT(PE) - 0. Fundamentos](prob_stats/fundamentos.md)
[QT(PE) - 1. Tipos de Ordenes](microstructure/tipos_ordenes.md)
[QT(PE) - 2.Libro de Ordenes](microstructure/libro_ordenes.md)
[QT(PE) - 3.Varianza y Desviación Típica](prob_stats/varianza_desviacion.md)
[QT(PE) - 4.Probabilidad Condidional y Teorema de Bayes](prob_stats/probabilidad_condicional_bayes.md)
[QT(PE) - 5.Permutaciones y Combinaciones](prob_stats/permutaciones_combinaciones.md)
[QT(PE) - 6.Modelos Probabilisticos](prob_stats/modelos_probabilisticos.md)
[QT(PE) - 7.Valor Esperado](prob_stats/valor_esperado.md)
[QT(PE) - 8.Variable Aleatoria](prob_stats/variable_aleatoria.md)
[QT(PE) - 9.Múltiples Variables Aleatorias](prob_stats/multiples_variables.md)
[QT(PE) - 10.Covarianza y Correlación](prob_stats/covarianza_correlacion.md)
[QT(PE) - 11.Ley de los Grandes Números y Teorema del Límite Central](prob_stats/ley_grandes_numeros_tlc.md)
[QT(PE) - 12.Intervalos de Confianza](prob_stats/intervalos_confianza.md)
[QT(PE) - 13.Modelos Lineales y Vecinos Más Cercanos](ml/modelos_lineales_knn.md)

---

[QT - 1.Analista de Sistemas Financieros](analista_financiero.md)
[QT - 2.Simulaciones de Montecarlo](strategies/montecarlo.md)
[QT - 3.Drawdown](portfolio/drawdown.md)
[QT - 4.Backtesting](strategies/backtesting.md)
[QT - 5.Sharpe Ratio](portfolio/sharpe_ratio.md)
[QT - 6.Sortino Ratio](portfolio/sortino_ratio.md)
[QT - 7.Arbitraje Estadístico - Trading de Pares (Pairs Trading)](strategies/pairs_trading.md)
[QT - 8.Trading de Alta Frecuencia (HFT)](microstructure/hft.md)
[QT - 9.Calmar Ratio](portfolio/calmar_ratio.md)
[QT - 10.Z-Score](maths/zscore.md)
[QT - 11. Análisis de series Temporales](maths/analisis_series_temporales.md)
[QT - 12.Cointegración](maths/cointegracion.md)
[QT - 13.Teselación de Voronoi](maths/voronoi.md)

---

[QT(Ej) - 1. Calcula el Maximum Drawdown](exercises/calcula_max_drawdown.md)
[QT(Ej) - 2. 5 Ejercicios Básicos](exercises/ejercicios_basicos.md)

---