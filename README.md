# 5 agentes de IA listos para trabajar

Este kit trae los **5 agentes de IA con mayor aplicación inmediata** para un negocio o un despacho. Se instalan en **Claude Code** y trabajan en paralelo con tus archivos. Cada uno te deja su trabajo terminado y te dice qué te toca decidir.

| # | Agente | Qué hace | Resultado real de un caso parecido |
|---|---|---|---|
| 1 | `atencion` | Responde a clientes 24/7 con tus precios y tus políticas, y te pasa solo lo que te toca decidir | Anthropic + Intercom: 50.8 % de los casos resueltos solos y 1,700 h ahorradas |
| 2 | `prospectos` | Califica prospectos A/B/C y redacta el mensaje para agendar a los mejores | Asana: +22 % de pipeline y 0 chats perdidos |
| 3 | `seguimiento` | Convierte las notas de una llamada en un correo de seguimiento, una propuesta y el renglón del CRM | Vendasta: USD 1 M recuperado y 282 días de trabajo al año |
| 4 | `facturas` | Revisa facturas CFDI (RFC, sumas, IVA, duplicados) y arma el programa de pagos | Fugro: de 2 min a 35 s por factura |
| 5 | `investigador` | Investiga en internet y entrega un informe de una página con fuentes | Dunaway: −90 % de tiempo de investigación |

Las cifras vienen del reporte *El poder de los agentes de IA* (aiLearning, octubre 2026): 91 casos analizados y 20 cifras verificadas en su fuente.

El ejemplo es **Ceiba Contadores**, un despacho contable **ficticio**. Todos sus datos (clientes, RFC, facturas, precios) son de ejemplo.

---

## Instalar (10 minutos)

**Necesitas:** una cuenta de Claude (Pro o Max) y una terminal (Terminal en Mac, PowerShell en Windows).

1. **Instala Claude Code**
   - Mac o Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows (PowerShell): `irm https://claude.ai/install.ps1 | iex`

2. **Descarga el kit**
   ```
   git clone https://github.com/jeshuasalazar/agentes-ia-kit.git
   cd agentes-ia-kit
   ```
   ¿No tienes git? En GitHub usa **Code → Download ZIP**, descomprímelo, renombra la carpeta `agentes-ia-kit-main` a `agentes-ia-kit` y entra a ella.

3. **Ábrelo en Claude Code**
   ```
   claude
   ```
   La primera vez inicia sesión con tu cuenta y acepta **"Confío en esta carpeta"**. Sin ese paso no se aplican los permisos del kit.

## Usar

**Los 5 a la vez:** escribe `/arranca`. En menos de un minuto cada agente deja su entrega en `salidas/`.

**Uno por uno:** pídelo con tus palabras, por ejemplo:
```
Usa a facturas para revisar las facturas de bandeja/facturas
Usa a atencion para responder este mensaje: "¿cuánto cobran por llevar mi contabilidad?"
```

**Ver al equipo trabajar en un tablero** (Mac): `bash demo.sh`. Se abre el tablero en Chrome y Claude Code arranca en la terminal; ahí escribe `/arranca`.
Con `bash demo.sh respaldo` el tablero repite una corrida grabada y no necesita internet.

Escribe `/agents` para ver a tu equipo y editar a cualquiera de sus integrantes.

## Hazlo tuyo: contrata en 3 preguntas

Cada agente es un archivo de texto en `.claude/agents/`. Contesta lo mismo que preguntarías al contratar a una persona:

1. **¿Qué va a hacer?** Va en `description`: el puesto y cuándo se le llama.
2. **¿Cómo lo hace bien?** Su método paso a paso, en la sección "Cómo lo hace bien".
3. **¿Qué nunca puede hacer?** Sus límites, en la sección "Nunca".

Y siempre: **tú diriges, sin frenar a nadie.** Los agentes usan la **autoridad al momento** de `negocio/manual.md`:
- 🟢 **Hecho al momento:** lo que está dentro de tu manual sale en el acto (el cliente que escribe a las 9:00 tiene respuesta a las 9:00) y solo te avisa.
- 🟡 **En marcha:** lo programado, como pagos que cuadran al centavo, sale solo; lo deshaces con un toque.
- 🔴 **Un toque:** solo las excepciones (descuentos, casos fuera de lo normal) te llegan como un sí o no. Si no contestas en 30 min, se aplica la opción segura.

Cada entrega termina con **"Te aviso"**: los avisos que te llegarían al celular. En el tablero los ves bajar en vivo (tecla **N**: el celular).

Para adaptarlo a tu negocio:
1. Reemplaza `CLAUDE.md` (el manual) y la carpeta `negocio/` con tus precios, políticas, agenda y proveedores.
2. Pon en `bandeja/` lo que te llega en un día normal.
3. Ajusta las 3 preguntas de cada agente a tu forma de trabajar.

**Para usar los agentes en todos tus proyectos**, cópialos a tu carpeta personal:
`mkdir -p ~/.claude/agents && cp .claude/agents/*.md ~/.claude/agents/`

## El semáforo de permisos (`.claude/settings.json`)

- 🟢 **Puede solo:** leer el negocio y escribir en `salidas/`. El investigador es el único con internet, porque así lo dice la lista `tools` de su puesto.
- 🟡 **Te pregunta:** antes de editar el manual, editar a los agentes o ejecutar comandos.
- 🔴 **Nunca:** modificar `negocio/`, `bandeja/` o `crm/`, borrar archivos o leer secretos (`.env`).

## Qué hay en la carpeta

```
CLAUDE.md              el manual del negocio (lo leen todos)
.claude/agents/        los 5 puestos: atencion, prospectos, seguimiento, facturas, investigador
.claude/commands/      /arranca: los 5 en paralelo
.claude/settings.json  el semáforo de permisos
negocio/               precios, políticas, agenda, proveedores, documentos
bandeja/               lo que llegó hoy (WhatsApp, prospectos, llamada, facturas CFDI, encargo)
crm/                   el CRM de ejemplo (CSV)
salidas/               aquí dejan su trabajo
ejemplos/              una corrida real de los 5, para que veas el resultado esperado
herramientas/          el tablero (Python sin dependencias)
```

## Costo y tiempo medidos

En una corrida real de `/arranca` (13-oct-2026) los 5 agentes trabajaron en paralelo y terminaron en **55 segundos**. Costó unos **US$0.87** (≈ $16 MXN) por uso de API: cuatro agentes trabajan sin internet y el investigador hace de 2 a 4 búsquedas. Con un plan Pro o Max, este uso entra en tu plan.

## Cuidado

- Los agentes **proponen**: no envían, no pagan y no modifican tus sistemas. Así empieza un equipo sano.
- Revisa siempre las cifras del investigador en su fuente antes de citarlas.
- Si usas datos reales de clientes, revisa la LFPDPPP y cómo trata Anthropic tus datos en tu plan.

---

Hecho por Jeshua Salazar · aiLearning, la plataforma de aprendizaje de IA hecha en México · [ailearning.mx](https://ailearning.mx) · Licencia MIT
