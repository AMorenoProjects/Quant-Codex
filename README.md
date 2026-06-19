# Quant Codex 📔

**Quant Codex** es una base de conocimientos interactiva, un libro digital y un portafolio de estudio riguroso dedicado a las **Finanzas Cuantitativas** y el **Algorithmic Trading**. 

El proyecto recopila teoría matemática avanzada, modelos estadísticos de valoración de activos, técnicas de gestión de riesgos y código práctico de programación implementado en Python. Está construido sobre **Jupyter Book v2** (potenciado por **MyST Markdown**) y se compila de forma estática para ser alojado en GitHub Pages bajo el dominio personalizado [quantcodex.com](https://quantcodex.com).

---

## 🚀 Características Clave

* **Sintaxis Matemática Rigurosa**: Renderizado perfecto de ecuaciones en LaTeX para cálculo estocástico, optimización convexa y modelado de series temporales.
* **Flujo Automatizado (CI/CD)**: Compilación y despliegue automáticos mediante GitHub Actions en cada `git push` a la rama `main`.
* **Vinculación Obsidian Integrada**: Diseñado para traducir automáticamente wikilinks tradicionales de Obsidian (`[[Nota]]`) a enlaces HTML relativos válidos en la web.
* **Interactividad y Código**: Soporte para cuadernos de notas interactivos de Jupyter (`.ipynb`) ejecutables directamente en la web a través de plataformas en la nube (Binder/Thebe).
* **Organización Modular**: Estructurado en 8 secciones de estudio desde probabilidad elemental hasta Machine Learning y microestructura de mercado.

---

## 📂 Estructura de Secciones

El Codex está estructurado según la siguiente taxonomía de contenidos:

1. **Fundamentos Matemáticos**: Álgebra lineal avanzada y cálculo estocástico (Itô calculus).
2. **Probabilidad y Estadística**: Distribuciones continuas/discretas, Teorema de Bayes, TLC e intervalos de confianza.
3. **Valoración de Activos (Asset Pricing)**: Modelado de difusión (Black-Scholes-Merton) y ecuaciones diferenciales parciales.
4. **Microestructura del Mercado**: Funcionamiento del Limit Order Book (LOB), spreads bid-ask y sistemas de trading de alta frecuencia (HFT).
5. **Estrategias y Backtesting**: Simulación de Montecarlo, Pairs Trading y arbitraje estadístico de reversión a la media.
6. **Gestión de Portafolio y Métricas**: Teoría clásica de optimización, paridad de riesgo (Risk Parity) y métricas críticas de riesgo (Drawdown, Sharpe, Sortino, Calmar).
7. **Machine Learning Aplicado**: Modelos no paramétricos ($k$-NN), regresiones matriciales de mínimos cuadrados y la maldición de la dimensionalidad.
8. **Ejercicios Prácticos**: Retos prácticos de programación y screeners multiactivos de cointegración/Z-Score en Python.

---

## 🛠️ Instalación y Compilación Local

Si deseas previsualizar o compilar el Codex de forma local en tu máquina:

### 1. Requisitos Previos
Asegúrate de tener instalado **Python 3.10+** y `pip`.

### 2. Configurar el Entorno Virtual
Crea un entorno de desarrollo aislado e instala las dependencias necesarias:

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar el entorno
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate   # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Compilar el Libro
Para compilar la estructura de archivos a páginas web estáticas HTML ejecute:

```bash
jupyter-book build --html
```

El sitio compilado se generará en la carpeta `_build/html/`. El comando también iniciará un servidor local de desarrollo en el puerto `3000` (con live reload) para que puedas previsualizar tu Codex abriendo:
👉 `http://localhost:3000`

---

## 🤖 Flujo de Actualización Asistido por IA

Para mantener al día el Codex, el flujo de trabajo recomendado es:
1. Toma notas de tus investigaciones y lecturas directamente en tu editor o bóveda de Obsidian.
2. Proporciona tus apuntes o scripts en lenguaje natural al agente de IA.
3. El agente de IA formateará rigurosamente el código matemático en LaTeX, estructurará los scripts de Python y los integrará en la categoría correspondiente actualizando el índice.
4. Un simple `git push` actualizará la web pública automáticamente en menos de un minuto.

---
*Desarrollado y mantenido por [Alejandro Moreno](https://github.com/AMorenoProjects).*