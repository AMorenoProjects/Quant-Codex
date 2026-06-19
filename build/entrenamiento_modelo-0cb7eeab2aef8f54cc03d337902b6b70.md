El video presenta una charla técnica a cargo de John Crepezi, quien trabaja en el equipo de asistencia de Inteligencia Artificial en Jane Street, y explica detalladamente cómo la compañía está desarrollando herramientas y modelos de lenguaje (LLMs) personalizados para optimizar el flujo de trabajo de sus desarrolladores.

A continuación, se presenta un resumen exhaustivo de los temas abordados en la presentación:

### 1. El gran desafío: OCaml y la infraestructura personalizada

La adopción de herramientas de IA comerciales (como las que usan otras empresas) resulta muy difícil para Jane Street debido a una particularidad central: **utilizan OCaml como su lenguaje de desarrollo principal**. OCaml es un lenguaje funcional muy potente pero sumamente inusual en la industria, utilizado comúnmente para la demostración de teoremas o la escritura de otros lenguajes. Sin embargo, Jane Street lo utiliza para absolutamente todo: usan transpiladores para escribir aplicaciones web y plugins de Vim en OCaml, e incluso lo usan para programar hardware (FPGA).

Esta decisión conlleva graves problemas para utilizar IA preentrenada:

- **Falta de datos:** Los modelos comerciales no son buenos programando en OCaml simplemente porque no hay suficientes datos de entrenamiento disponibles. De hecho, es muy probable que Jane Street tenga más código escrito en OCaml internamente que el resto del mundo combinado.
- **Herramientas propias:** Tienen una infraestructura altamente personalizada que incluye sistemas de compilación distribuidos propios, un sistema de revisión de código llamado "Iron", y utilizan un repositorio monolítico (monorepo) gigantesco que guardan en Mercurial en lugar de Git.
- **Editores inusuales:** El 67% de la empresa programa utilizando Emacs, en lugar de editores modernos predominantes como VS Code.

### 2. El proceso de entrenamiento: De la teoría a la realidad

Inspirados por un informe de Meta (donde detallaban cómo entrenaron un modelo para el lenguaje _Hack_, que tiene una adopción limitada similar a OCaml), decidieron entrenar sus propios modelos. Al principio pensaron que bastaría con mostrarle su código base a un modelo para que aprendiera, pero descubrieron que **la IA necesita ejemplos estructurados exactamente igual que el tipo de preguntas que se le harán**.

El objetivo que se propusieron fue que un desarrollador pudiera escribir una instrucción en su editor de texto y el modelo le devolviera un _diff_ (un bloque de diferencias de código) que pudiera abarcar múltiples archivos y hasta 100 líneas, el cual debía aplicarse limpiamente y pasar la verificación de tipos. Para lograrlo, necesitaban ejemplos formativos compuestos por tres partes: el contexto previo, la instrucción humana y el código final.

### 3. La técnica de "Workspace Snapshotting" (Captura de áreas de trabajo)

Para conseguir los datos de entrenamiento, se dieron cuenta de que no podían usar el historial de sus revisiones de código (Iron) ni sus _commits_ convencionales, ya que las descripciones eran demasiado largas y los cambios de código abarcaban cientos de líneas, sin estar aislados en tareas pequeñas.

La solución fue implementar un sistema que **toma capturas automáticas de las estaciones de trabajo de los desarrolladores cada 20 segundos**, guardando al mismo tiempo el estado de la compilación (si era exitosa "verde" o daba error "roja").

- Si detectaban un patrón de compilación _verde -> rojo -> verde_, sabían que el desarrollador acababa de hacer un cambio funcional pequeño y aislado.
- Si veían un patrón de _rojo -> verde_, significaba que el desarrollador había encontrado un error de tipado o de compilación y lo había solucionado. Capturar esto ayudó al modelo a aprender cómo recuperarse de errores. Finalmente, utilizaron otro modelo de lenguaje para redactar las descripciones de esas acciones y las resumieron hasta que parecieran instrucciones escritas por un humano.

### 4. Aprendizaje por Refuerzo y Evaluaciones (CES)

En OCaml, debido a que es un lenguaje de tipado estático, el código "bueno" es aquel que logra compilarse y pasar el verificador de tipos. Para enseñar esto, Jane Street creó el **CES (Servicio de Evaluación de Código)**. Este servicio mantiene compilaciones precalentadas y listas. Durante meses, unos "trabajadores" virtuales toman el código sugerido por la IA, lo aplican a estas bases y determinan si la compilación resulta en verde o rojo, enviando este resultado para que el modelo alinee su comportamiento y aprenda a generar código válido.

John comparte una anécdota hilarante sobre la importancia de las evaluaciones: al entrenar un modelo distinto diseñado para revisar el código de forma automática, el modelo se quedó pensando y finalmente respondió: _"Lo haré mañana"_. Esto ocurrió porque el modelo había sido entrenado usando ejemplos de humanos reales evadiendo tareas.

### 5. Integración en los editores: La arquitectura AIDE

Para que los desarrolladores usaran la herramienta en VS Code, Emacs y Neovim, no querían programar tres extensiones distintas. La solución fue crear **AIDE (AI Development Environment)**.

AIDE es una aplicación "sidecar" (que funciona en segundo plano en la máquina del desarrollador) que se encarga de crear el contexto, generar las instrucciones y leer el estado de la compilación. Esto permite:

- Actualizar la herramienta reiniciando solo el servicio en segundo plano, sin obligar a los programadores a reiniciar sus editores de texto.
- Mantener una interfaz gráfica similar a Copilot en VS Code, pero crear una experiencia totalmente distinta basada en texto (un _buffer_ de Markdown) en Emacs, adaptándose a lo que prefieren esos usuarios.
- Hacer pruebas A/B, enviando modelos distintos a la mitad de la empresa para comparar tasas de aceptación del código generado, y añadir rápidamente herramientas específicas desarrolladas por otros departamentos.

La presentación concluye mencionando que el equipo sigue innovando sobre esta sólida arquitectura, aplicando generación aumentada por recuperación (RAG) en los editores, investigando modelos de razonamiento y desarrollando flujos de trabajo con múltiples agentes de IA.