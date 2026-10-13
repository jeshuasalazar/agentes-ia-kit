# Guía paso a paso · Instala tus 5 agentes de IA

Tiempo: 30 minutos la primera vez. No necesitas saber programar.
Al terminar tendrás 5 agentes trabajando en tu computadora: **atención al cliente, prospectos, seguimiento comercial, facturas e investigación**. Después podrás adaptarlos a tu negocio con 3 preguntas.

---

## Paso 0 · Lo que necesitas

- Una computadora con Mac, Windows o Linux.
- Una cuenta de **Claude Pro o Max** en [claude.ai](https://claude.ai). Los agentes usan tu plan y no pagas aparte.
- 30 minutos sin interrupciones.

## Paso 1 · Abre la terminal

- **Mac:** presiona ⌘ + Espacio, escribe **Terminal** y presiona Enter.
- **Windows:** abre el menú Inicio, escribe **PowerShell** y ábrelo.

La terminal es una ventana donde escribes instrucciones. Copia y pega cada comando de esta guía y presiona Enter.

## Paso 2 · Instala Claude Code

- **Mac o Linux**
  ```
  curl -fsSL https://claude.ai/install.sh | bash
  ```
- **Windows (PowerShell)**
  ```
  irm https://claude.ai/install.ps1 | iex
  ```

Cierra la terminal y vuelve a abrirla. Para comprobar que quedó instalado, escribe:
```
claude --version
```
Debe aparecer un número de versión.

## Paso 3 · Descarga el kit

**Opción A, la más fácil:**
1. Entra a **github.com/jeshuasalazar/agentes-ia-kit**.
2. Haz clic en el botón verde **Code → Download ZIP**.
3. Descomprime el archivo. La carpeta se llama `agentes-ia-kit-main`: **renómbrala a `agentes-ia-kit`** y muévela a tus Documentos.

**Opción B, con git:**
```
cd ~/Documents
git clone https://github.com/jeshuasalazar/agentes-ia-kit.git
```

## Paso 4 · Entra a la carpeta y abre Claude Code

```
cd ~/Documents/agentes-ia-kit
claude
```
- La primera vez te pedirá iniciar sesión: elige tu cuenta de Claude y autoriza en el navegador.
- Después aparece **"¿Confías en los archivos de esta carpeta?"**. Elige **Sí**. Con eso se activan los permisos del kit, el semáforo.

## Paso 5 · Conoce a tu equipo

Escribe:
```
/agents
```
Verás a los 5: `atencion`, `prospectos`, `seguimiento`, `facturas` e `investigador`. Presiona Esc para salir.

## Paso 6 · Ponlos a trabajar

Escribe:
```
/arranca
```
Los 5 trabajan **al mismo tiempo** con lo que hay en la carpeta `bandeja/`: un WhatsApp, 8 prospectos, las notas de una llamada, 6 facturas y un encargo de investigación. En menos de un minuto cada uno deja su trabajo en `salidas/`.

Abre la carpeta `salidas/`. Cada archivo termina con **"Te aviso"**: lo que el agente ya hizo (🟢), lo que está en marcha (🟡) y, solo si hay una excepción, la pregunta de sí o no que te toca (🔴). Nadie se quedó esperando tu revisión.

> **Tablero visual (opcional, Mac):** sal con `/exit` y escribe `bash demo.sh`. Se abre el tablero en Chrome y Claude Code arranca. Escribe `/arranca` y mira a los 5 trabajar.

## Paso 7 · Úsalos uno por uno

Habla con ellos como con tu equipo:
```
Usa a atencion para responder este mensaje: "Hola, ¿cuánto cobran por la contabilidad de una persona física?"
```
```
Usa a facturas para revisar las facturas de bandeja/facturas
```
```
Usa a investigador para preparar un informe de una página sobre la facturación electrónica en restaurantes
```

## Paso 8 · Hazlos tuyos: contrata en 3 preguntas

Los agentes de ejemplo trabajan para **Ceiba Contadores**, un despacho ficticio. Para que trabajen para ti:

1. **El manual (`CLAUDE.md`).** Pide en Claude Code: *"Ayúdame a reescribir CLAUDE.md para mi negocio: [quién eres, qué vendes, cómo hablas]"*.
2. **Los datos (`negocio/`).** Reemplaza precios, políticas, agenda y proveedores con los tuyos. Pueden ser archivos de texto sencillos.
3. **Los puestos (`.claude/agents/`).** Abre cada agente y contesta las 3 preguntas:
   - **¿Qué va a hacer?** El puesto, en `description`.
   - **¿Cómo lo hace bien?** Tu método, paso a paso.
   - **¿Qué nunca puede hacer?** Sus límites: lo que siempre pasa por ti.
4. **La bandeja (`bandeja/`).** Pon ahí lo que te llega en un día normal y vuelve a escribir `/arranca`.

Regla de oro: **tú diriges.** Que te escalen solo las excepciones, como un descuento, un pago o algo que no está en el manual.

## Paso 9 · Llévalos a todos tus proyectos (opcional)

Para que los 5 estén disponibles en cualquier carpeta:
```
mkdir -p ~/.claude/agents && cp .claude/agents/*.md ~/.claude/agents/
```

---

## Si algo falla

| Problema | Solución |
|---|---|
| `claude: command not found` | Cierra y vuelve a abrir la terminal. Si sigue igual, repite el paso 2. |
| Me pide permiso a cada rato | No aceptaste "Confío en esta carpeta". Sal con `/exit`, vuelve a escribir `claude` y acéptalo. |
| `/arranca` no aparece | Asegúrate de estar dentro de la carpeta `agentes-ia-kit` (paso 4). |
| El investigador tarda | Es el único que busca en internet. Normalmente termina en menos de un minuto. |
| Quiero empezar de cero | Borra los archivos de `salidas/` y vuelve a escribir `/arranca`. |

## Tu primera semana

| Día | Qué haces | Tiempo |
|---|---|---|
| Lunes | Instala el kit y corre `/arranca` con el ejemplo | 30 min |
| Martes | Reescribe `CLAUDE.md` con tu negocio | 30 min |
| Miércoles | Elige **un** agente (el que más te duela) y pon tus datos | 20 min |
| Jueves | Úsalo con un caso real y anota cuánto tiempo te ahorró | 15 min |
| Viernes | Ajusta sus 3 preguntas con lo que aprendiste | 15 min |

Mide horas ahorradas durante 30 días. Si funciona, suma el siguiente agente.
