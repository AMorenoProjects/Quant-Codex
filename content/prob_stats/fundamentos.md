### Nivel 1: Fundamentos del Mercado y Datos (Baja Complejidad, Alta Utilidad)

Estos son los cimientos. Sin dominarlos, cualquier modelo complejo fallará por errores en la base de datos o en la comprensión de cómo opera el mercado real.

- **Microestructura de Mercado:** Tipos de órdenes (Market, Limit, Stop, Iceberg), funcionamiento del Libro de Órdenes Centralizado (LOB), _Bid-Ask Spread_, profundidad de mercado y liquidez.
	- [QT(PE) - 1. Tipos de Ordenes](../microstructure/tipos_ordenes.md)
	- [QT(PE) - 2.Libro de Ordenes](../microstructure/libro_ordenes.md)
    
- **Matemáticas Financieras:** Cálculo de retornos simples vs. logarítmicos, composición continua, ajuste por dividendos y splits.
    
- **Métricas de Desempeño:** Ratio de Sharpe, Ratio de Sortino, Maximum Drawdown (MDD), Ratio de Calmar y Win Rate.
	- [QT - 5.Sharpe Ratio](../portfolio/sharpe_ratio.md)
	- [QT - 6.Sortino Ratio](../portfolio/sortino_ratio.md)
	- [QT - 3.Drawdown](../portfolio/drawdown.md)
    
- **Higiene de Datos (Data Wrangling):** Limpieza de valores nulos, alineación de zonas horarias, manejo de datos faltantes (forward-fill, backward-fill) y remuestreo de temporalidades (ej. pasar de datos de 1 minuto a diarios).
    
- **Mecánica de Backtesting:** Costes de transacción (comisiones, _slippage_), impacto de mercado básico y la diferencia entre backtesting vectorial vs. orientado a eventos (_event-driven_).
    

### Nivel 2: Core Estadístico y Cuantitativo (Complejidad Media, Alta Utilidad)

Aquí se separan los traders discrecionales de los cuantitativos. Se trata de validar hipótesis con rigor matemático.

- **Estadística Descriptiva:** Media, varianza, asimetría (_skewness_) y curtosis de las distribuciones de retornos.
	- [QT(PE) - 3.Varianza y Desviación Típica](../prob_stats/varianza_desviacion.md)
	- [QT(PE) - 4.Probabilidad Condidional y Teorema de Bayes](../prob_stats/probabilidad_condicional_bayes.md)
	- [QT(PE) - 5.Permutaciones y Combinaciones](../prob_stats/permutaciones_combinaciones.md)
    
- **Pruebas de Hipótesis y Significación:** P-values, t-tests, y z-tests para validar si tu _Alpha_ es estadísticamente diferente de cero o producto del azar.
    
- **Sesgos Cognitivos en el Modelado:** Evitar el _Look-ahead bias_ (usar datos futuros en el pasado), _Survivorship bias_ (ignorar empresas que quebraron) y el _Overfitting_ (sobreajuste a datos históricos).
    
- **Análisis Básico de Series Temporales:** Concepto de estacionariedad y la Prueba Aumentada de Dickey-Fuller (ADF).
    
- **Correlación y Dependencia:** Correlación de Pearson, correlación de rangos de Spearman y el concepto de autocorrelación.
    

### Nivel 3: Modelado Matemático y Gestión de Riesgo (Complejidad Alta, Alta Utilidad)

Este nivel abarca la creación de estrategias robustas y la gestión del capital a nivel de cartera.

- **Teoría Moderna de Carteras (MPT):** Frontera eficiente de Markowitz y optimización de varianza media.
    
- **Modelos de Factores y Pricing:** Capital Asset Pricing Model (CAPM), extracción de Beta (rendimiento del mercado) vs. Alpha (habilidad), y los modelos de 3 y 5 factores de Fama-French.
    
- **Cointegración:** La base estadística para el _Pairs Trading_ y las estrategias de reversión a la media. Diferencia fundamental entre correlación y cointegración.
    
- **Análisis Avanzado de Series Temporales:** Modelos autorregresivos (AR, MA, ARIMA) y modelos de agrupación de volatilidad (ARCH, GARCH).
    
- **Dimensionamiento de Posiciones (Position Sizing):** Criterio de Kelly (y Kelly fraccional), paridad de riesgo (_Risk Parity_) y control de la volatilidad del portfolio.
    
- **Métricas de Riesgo Institucional:** Value at Risk (VaR) paramétrico e histórico, y Conditional VaR (Expected Shortfall).
    

### Nivel 4: Machine Learning y Derivados (Complejidad Muy Alta, Utilidad Media/Alta)

Herramientas avanzadas para extracción de señales no lineales y cobertura de riesgos complejos.

- **Machine Learning Predictivo:** Regresión Ridge/Lasso, Árboles de Decisión, Random Forest, Gradient Boosting (XGBoost/LightGBM) aplicados a clasificación de la dirección del precio.
    
- **Reducción de Dimensionalidad:** Análisis de Componentes Principales (PCA) para construir carteras o encontrar factores latentes en los rendimientos de los activos.
    
- **Validación Cruzada en Series Temporales:** _Walk-forward optimization_ y _Purged K-Fold Cross Validation_ (para evitar la filtración de datos o _data leakage_).
    
- **Pricing de Opciones (Básico/Intermedio):** Modelo Black-Scholes-Merton, comprensión de la volatilidad implícita vs. realizada, y las "Griegas" (Delta, Gamma, Theta, Vega).
    

### Nivel 5: Vanguardia, HFT y Matemáticas Estocásticas (Complejidad Extrema, Utilidad Específica/Nicho)

Conceptos utilizados por fondos _quant_ institucionales (Renaissance Technologies, Two Sigma) y firmas de HFT (Jane Street, Optiver).

- **Cálculo Estocástico:** Movimiento Browniano Geométrico, Lema de Itô y Ecuaciones Diferenciales Estocásticas (SDE) para el modelado riguroso de precios de derivados.
    
- **Microestructura Avanzada y Ejecución:** Modelos de impacto de mercado temporal y permanente, y algoritmos de ejecución óptima (VWAP, TWAP, modelo de Almgren-Chriss).
    
- **Market Making Matemático:** Modelo de Avellaneda-Stoikov para el control de inventario y la colocación óptima de cotizaciones (bid/ask).
    
- **Deep Learning y NLP:** Redes Neuronales Recurrentes (LSTM), Transformers para análisis de secuencias de precios, y Procesamiento de Lenguaje Natural (NLP) usando LLMs para extraer sentimiento o eventos de noticias financieras (_event-driven arbitrage_).