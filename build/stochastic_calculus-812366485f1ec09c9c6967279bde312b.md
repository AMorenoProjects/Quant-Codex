# Cálculo Estocástico en Finanzas

El cálculo estocástico es la base matemática sobre la cual se cimienta el análisis de derivados y la teoría moderna de valoración de activos. A diferencia del cálculo clásico, las trayectorias de los precios de los activos no son diferenciables convencionalmente debido a su naturaleza aleatoria.

## 1. Movimiento Browniano (Proceso de Wiener)

Un proceso estocástico $W_t$ es un Movimiento Browniano estándar si satisface las siguientes propiedades:
1. $W_0 = 0$.
2. Las trayectorias $t \to W_t$ son continuas casi con seguridad.
3. Tiene incrementos independientes y estacionarios: para $s < t$, $W_t - W_s \sim \mathcal{N}(0, t-s)$.

La representación infinitesimal de un incremento se denota como $dW_t$, donde:
$$\mathbb{E}[dW_t] = 0$$
$$\text{Var}(dW_t) = dt$$

## 2. El Lema de Itô

El Lema de Itô es el análogo a la regla de la cadena para funciones de procesos estocásticos. Si tenemos un proceso de difusión de Itô $X_t$ gobernado por la ecuación diferencial estocástica (SDE):

$$dX_t = \mu(X_t, t)dt + \sigma(X_t, t)dW_t$$

Y sea $f(x, t)$ una función continuamente diferenciable en dos variables. Entonces $Y_t = f(X_t, t)$ es también un proceso de Itô, y su diferencial estocástica viene dada por:

$$df(X_t, t) = \left( \frac{\partial f}{\partial t} + \mu(X_t, t)\frac{\partial f}{\partial x} + \frac{1}{2}\sigma(X_t, t)^2 \frac{\partial^2 f}{\partial x^2} \right) dt + \sigma(X_t, t)\frac{\partial f}{\partial x} dW_t$$

```{note}
El término $\frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2} dt$ proviene del hecho de que $(dW_t)^2 = dt$ en el sentido del límite en media cuadrática, un fenómeno puramente estocástico conocido como variación cuadrática no nula.
```

---

En los siguientes capítulos utilizaremos el Lema de Itô para derivar la ecuación diferencial parcial de Black-Scholes-BSM.
