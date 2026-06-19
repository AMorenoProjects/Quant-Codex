# Valoración de Derivados: El Modelo Black-Scholes

El modelo de Black-Scholes-Merton (1973) revolucionó el mercado financiero al proporcionar una solución analítica cerrada para valorar opciones europeas bajo el supuesto de no arbitraje y mercados continuos.

## 1. La Ecuación Diferencial Parcial (PDE)

Asumiendo que el precio del activo subyacente $S_t$ sigue un movimiento browniano geométrico (GBM):

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

Donde $\mu$ es el rendimiento esperado y $\sigma$ es la volatilidad constante. Mediante la construcción de una cartera de cobertura dinámica (delta hedging) perfectamente libre de riesgo, se deriva la célebre **PDE de Black-Scholes**:

$$\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV = 0$$

Donde:
* $V(S, t)$ es el valor de la opción.
* $r$ es la tasa de interés libre de riesgo.
* $\sigma$ es la volatilidad del subyacente.

## 2. Solución Analítica para Opciones Europeas (Fórmula de BSM)

Para una opción de compra europea (Call) con precio de ejercicio $K$ y fecha de vencimiento $T$, la solución a la PDE con la condición de frontera $V(S, T) = \max(S_T - K, 0)$ es:

$$C(S_t, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)$$

Donde $N(\cdot)$ representa la función de distribución acumulada de una variable normal estándar $\mathcal{N}(0,1)$, y los coeficientes $d_1$ y $d_2$ vienen dados por:

$$d_1 = \frac{\ln\left(\frac{S_t}{K}\right) + \left(r + \frac{\sigma^2}{2}\right)(T-t)}{\sigma\sqrt{T-t}}$$

$$d_2 = d_1 - \sigma\sqrt{T-t}$$

---

En las secciones prácticas implementaremos esta solución en Python y visualizaremos el comportamiento de las "Griegas" (sensibilidades del precio de la opción ante cambios en los parámetros).
