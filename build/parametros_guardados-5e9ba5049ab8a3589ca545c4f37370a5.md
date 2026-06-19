#### Prueba 1
```python
import polars as pl

def strategy(bars: pl.DataFrame) -> pl.Series:
    # Parámetros del Modelo
    periodo = PARAM_periodo
    lambda1 = 2.02
    lambda2 = 2.10
    gamma0 = 1.20
    phi0 = 15.0
    zUmbral = 2.50

    # Referencias a columnas (Lazy evaluation)
    close = pl.col("close")
    high = pl.col("high")
    low = pl.col("low")

    # 1. Zy: Z-Score de Retornos Logarítmicos
    ret_log = close.log() - close.shift(1).log()
    mean_ret = ret_log.rolling_mean(window_size=periodo)
    std_ret = ret_log.rolling_std(window_size=periodo)
    zy = (
        pl.when(std_ret.is_not_null() & (std_ret != 0))
        .then((ret_log - mean_ret) / std_ret)
        .otherwise(0.0)
    )

    # 2. Rnorm: Volatilidad Normalizada (ATR simplificado / Close)
    c_prev = close.shift(1)
    tr1 = high - low
    tr2 = (high - c_prev).abs()
    tr3 = (low - c_prev).abs()
    # Identificar el True Range de forma vectorizada
    tr = pl.max_horizontal(tr1, tr2, tr3)
    atr = tr.rolling_mean(window_size=periodo)
    rnorm = atr / close

    # 3. C: Consenso Bounded 0-1 (RSI implementado en Polars / 100)
    delta = close.diff()
    up = pl.when(delta > 0).then(delta).otherwise(0.0)
    down = pl.when(delta < 0).then(-delta).otherwise(0.0)

    avg_up = up.ewm_mean(span=periodo)
    avg_down = down.ewm_mean(span=periodo)
    rs = avg_up / avg_down

    rsi = (
        pl.when((avg_up == 0) & (avg_down == 0)).then(50.0)
        .when(avg_down == 0).then(100.0)
        .otherwise(100.0 - (100.0 / (1.0 + rs)))
    )
    c = rsi / 100.0

    # 4. T: Tiempo desde el último cruce de tendencia (Media rápida vs lenta)
    sma_fast = close.rolling_mean(window_size=10)
    sma_slow = close.rolling_mean(window_size=50)
    trend = sma_fast > sma_slow
    # Crear un trigger por cada cruce para reiniciar el contador
    cross = trend.fill_null(False) != trend.shift(1).fill_null(False)
    cross_id = cross.cast(pl.Int32).cum_sum()
    # Suma acumulativa agrupada para contar las barras desde el último cruce
    t = pl.lit(1).cum_sum().over(cross_id) - 1

    # --- CÁLCULO DE LA ECUACIÓN ---
    term1 = (-lambda1 * t - lambda2 * zy).exp()
    indicatriz = pl.when(zy > zUmbral).then(1.0).otherwise(0.0)
    term2 = 1.0 + (gamma0 * zy * indicatriz)
    term3 = (-phi0 * (rnorm.pow(2))).exp()
    term4 = (0.5 - c).sign() * (1.0 - c)

    a_val = term1 * term2 * term3 * term4
    a_suav = a_val.ewm_mean(span=3)

    # --- LÓGICA DE POSICIONAMIENTO ---
    # Convertimos la métrica A en posiciones concretas {-1, 0, 1}
    position = (
        pl.when(a_suav > 0).then(1)
        .when(a_suav < 0).then(-1)
        .otherwise(0)
    )

    # Evaluar la estructura completa, extraer la columna, limpiar nulos al inicio y retornar
    return bars.select(position.alias("pos")).get_column("pos").fill_null(0).cast(pl.Int8)

```

#### Prueba 2