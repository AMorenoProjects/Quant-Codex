
El **Libro de Órdenes** (o _Limit Order Book_ - LOB) es el registro electrónico en tiempo real de todas las órdenes de compra y venta pendientes para un activo financiero en un exchange. Es la base de la microestructura del mercado y donde se determina el precio de forma dinámica.

### Estructura Fundamental

El libro se divide en dos columnas principales que nunca se cruzan (si se cruzaran, ocurriría una ejecución inmediata):

- **Bids (Lado de Compra):** "Los que quieren entrar barato"
	- Contiene todas las órdenes limitadas de compradores. Están ordenadas de mayor a menor precio. El precio más alto se conoce como **Best Bid**.
    
- **Asks / Offers (Lado de Venta):** "Los que quieren salir caro"
	- Contiene todas las órdenes limitadas de vendedores. Están ordenadas de menor a mayor precio. El precio más bajo se conoce como **Best Ask**.
    

### Componentes Clave

1. **Precio (Price):** El nivel específico al que un participante está dispuesto a transaccionar.
    
2. **Tamaño/Volumen (Size/Volume):** La cantidad de activos disponibles en cada nivel de precio.
    
3. **Spread (Diferencial):** Es la brecha entre el mejor precio de venta y el mejor de compra.
    
    $$Spread = Best\ Ask - Best\ Bid$$
    
4. **Mid-Price (Precio Medio):** El punto medio exacto entre el spread. Los modelos cuantitativos suelen usar este valor como referencia del "valor justo" instantáneo.
    
    $$Mid-Price = \frac{Best\ Ask + Best\ Bid}{2}$$
    
5. **Profundidad (Depth):** Se refiere a la cantidad de volumen disponible en niveles de precios alejados del mejor Bid/Ask. Un mercado "profundo" puede absorber grandes órdenes sin mover el precio significativamente.
    

---

### Dinámica de Funcionamiento

El libro de órdenes se mueve mediante dos acciones principales:

- **Añadir Liquidez (Maker):** Cuando envías una orden limitada que no se ejecuta inmediatamente (por ejemplo, quieres comprar a $100 cuando el precio actual es $102), tu orden se "asienta" en el libro. Aumentas la profundidad del mercado.
    
- **Consumir Liquidez (Taker):** Cuando envías una orden a mercado o una orden limitada que cruza el spread (ej. quieres comprar "ya" al precio que sea). El motor de emparejamiento toma las órdenes del lado opuesto del libro empezando por el mejor precio hasta completar tu volumen.
    

> **Ejemplo de Ejecución:**
> 
> Si quieres comprar 500 acciones "a mercado" y en el **Best Ask** solo hay 200 acciones a $10.50, el sistema ejecutará esas 200 y luego saltará al siguiente nivel de precio (ej. $10.55) para comprar las 300 restantes. Esto es lo que causa el **slippage**.

---

### Prioridad de Ejecución (Matching Engine)

Los exchanges utilizan algoritmos para decidir qué orden se ejecuta primero cuando hay varios participantes al mismo precio. El estándar global es **Price-Time Priority (FIFO)**:

1. **Prioridad de Precio:** La orden con el mejor precio (compra más alta o venta más baja) siempre se ejecuta primero.
    
2. **Prioridad de Tiempo:** Si dos personas ofrecen el mismo precio, la orden que entró primero al sistema del exchange tiene prioridad.
    

### Niveles de Datos

Como quant, verás que la información del libro se categoriza por su granularidad:

- **Level 1 (L1):** Solo muestra el Best Bid, Best Ask y el último precio operado.
    
- **Level 2 (L2):** Muestra la profundidad (volumen) en varios niveles de precio (usualmente los 5, 10 o 20 mejores de cada lado). Es vital para detectar muros de compra/venta.
    
- **Level 3 (L3):** Proporciona información sobre cada orden individual en el libro, permitiendo ver qué instituciones están operando (si los datos no son anónimos) y el tamaño exacto de cada "ticket".
    

### El concepto de "Order Book Imbalance"

Uno de los indicadores estadísticos más usados en trading de alta frecuencia es el desequilibrio del libro. Si hay mucho más volumen en el lado del Bid que en el del Ask, existe una presión de compra latente que sugiere que el precio podría subir en los próximos milisegundos.