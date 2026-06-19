# Gestión de Portafolios: Risk Parity

La Paridad de Riesgo (*Risk Parity*) es un enfoque de asignación de activos que busca diversificar un portafolio asignando ponderaciones basadas en el **riesgo aportado** por cada activo, en lugar de distribuir el capital de forma equitativa (1/N) o por optimización de media-varianza clásica.

## 1. Contribución de Riesgo Marginal y Total

Dada una cartera con ponderaciones $w = [w_1, w_2, \dots, w_N]^T$ y matriz de covarianza de retornos $\Sigma$, la volatilidad del portafolio $\sigma_p$ está definida por:

$$\sigma_p = \sqrt{w^T \Sigma w}$$

La **Contribución Marginal al Riesgo** (MRC) del activo $i$ se define como la derivada parcial de la volatilidad del portafolio respecto al peso de dicho activo:

$$\text{MRC}_i = \frac{\partial \sigma_p}{\partial w_i} = \frac{(\Sigma w)_i}{\sigma_p}$$

La **Contribución Total al Riesgo** (RC) del activo $i$ representa cuánto del riesgo global de la cartera es atribuible a ese activo:

$$\text{RC}_i = w_i \times \text{MRC}_i = w_i \frac{(\Sigma w)_i}{\sigma_p}$$

Por propiedad de homogeneidad de Euler, la suma de las contribuciones de riesgo individuales es igual a la volatilidad total de la cartera:

$$\sum_{i=1}^N \text{RC}_i = \sigma_p$$

## 2. El Problema de Optimización de Paridad de Riesgo

El objetivo de un portafolio de paridad de riesgo puro es igualar las contribuciones de riesgo de todos los activos, es decir, $\text{RC}_i = \frac{1}{N}\sigma_p$ para todo $i$. 

Esto se puede plantear como un problema de optimización no lineal y convexo:

$$\min_{w} \quad \frac{1}{2} w^T \Sigma w - c \sum_{i=1}^N \ln(w_i)$$

Sujeto a:
* $w_i > 0$ para todo $i$.

Donde $c > 0$ es una constante arbitraria. Tras resolver este problema, los pesos óptimos $w^*$ se normalizan de manera que sumen 1 ($\sum w_i^* = 1$). El término logarítmico $\ln(w_i)$ actúa como una barrera que penaliza pesos cercanos a cero, forzando la inclusión de todos los activos en el portafolio.

---

En los notebooks prácticos utilizaremos solucionadores convexos como `cvxpy` o algoritmos iterativos con `scipy.optimize` para construir portafolios de paridad de riesgo con activos reales.
