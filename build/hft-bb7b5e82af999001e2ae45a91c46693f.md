
El Trading de Alta Frecuencia (HFT, por sus siglas en inglés) es una subcategoría especializada del trading cuantitativo y algorítmico. Se define por la ejecución de un gran número de órdenes a velocidades extremadamente altas, medidas en microsegundos o nanosegundos.

### Características Principales del HFT

- **Velocidad de ejecución:** Es la ventaja competitiva principal. En HFT, la infraestructura tecnológica es a menudo más importante que la complejidad matemática del modelo predictivo.
    
- **Alta tasa de cancelación (Order-to-Trade Ratio):** Los sistemas HFT envían y cancelan miles de órdenes por cada orden que realmente se ejecuta. Ajustan sus cotizaciones constantemente basándose en la microestructura del mercado sin intención real de ejecutar la mayoría de ellas.
    
- **Inventario plano (Flat Positions):** Los operadores de HFT buscan terminar la sesión de negociación con una exposición neta de cero. Cierran todas sus posiciones antes del final del día para no asumir ningún riesgo de mercado _overnight_.
    
- **Márgenes minúsculos, volumen masivo:** La ganancia por operación es fraccional (a menudo fracciones de centavo). La rentabilidad del negocio depende exclusivamente de ejecutar millones de operaciones diarias.
    

### Infraestructura Tecnológica

Para lograr latencias cercanas a cero, las firmas de HFT emplean tecnología de vanguardia:

- **Colocation (Colocación):** Consiste en alquilar espacio para ubicar sus propios servidores físicamente en el mismo centro de datos que el motor de emparejamiento (_matching engine_) del exchange (por ejemplo, en las instalaciones de Nasdaq o CME). Esto minimiza la distancia física que deben recorrer los datos.
    
- **Hardware Especializado (FPGA y ASIC):** Utilizan _Field-Programmable Gate Arrays_ (FPGA) para "quemar" la lógica de trading directamente en los chips de hardware en lugar de ejecutarla mediante software tradicional (sistemas operativos, kernels), eliminando microsegundos críticos de procesamiento.
    
- **Redes de Microondas y Láser:** Para conectar centros financieros distantes (como Chicago y Nueva York o Londres y Frankfurt), utilizan torres de transmisión por microondas. Las ondas electromagnéticas viajan a través de la atmósfera más rápido que la luz a través de los cables de fibra óptica.
    

### Estrategias Core de HFT

1. **Market Making (Creación de Mercado de Alta Frecuencia):** Proporcionan liquidez publicando constantemente órdenes límite de compra (_bid_) y venta (_ask_). El algoritmo ajusta los precios en microsegundos según el flujo del mercado y obtiene su beneficio capturando el _spread_ (la diferencia entre el precio de compra y venta).
    
2. **Arbitraje de Latencia:** Explotan micro-discrepancias de precios del mismo activo cotizado en diferentes bolsas. Si una bolsa actualiza el precio de una acción un milisegundo antes que otra, el algoritmo compra en el mercado rezagado y vende en el actualizado casi simultáneamente sin riesgo direccional.
    
3. **[QT - 12.Cointegración](../maths/cointegracion.md) de Microestructura:** Analizan la profundidad del libro de órdenes (_order book imbalance_) y el flujo de cinta (_tape flow_) para predecir movimientos direccionales a cortísimo plazo (fracciones de segundo) provocados por la llegada de grandes órdenes institucionales.
    
4. **Ignition & Spoofing (Prácticas Manipulativas):** Aunque el _spoofing_ es ilegal, históricamente algunos algoritmos colocaban grandes bloques de órdenes falsas en un lado del libro para crear la ilusión de presión de compra/venta, engañando a otros algoritmos para que movieran el precio a un nivel donde el manipulador tenía su orden real esperándolos.
    

### Impacto en el Mercado

El ecosistema HFT cambia la dinámica tradicional de la bolsa. Proporciona una liquidez inmensa en condiciones normales y reduce significativamente los _spreads_, lo que abarata los costes de transacción para el inversor minorista e institucional. Sin embargo, se le critica por generar "liquidez fantasma" (las órdenes desaparecen en cuanto hay volatilidad real, ya que los algoritmos se apagan para protegerse) y por amplificar el riesgo de eventos sistémicos rápidos, como el _Flash Crash_ de mayo de 2010.