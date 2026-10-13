---
description: Arranca el día. Los 5 agentes trabajan en paralelo con lo que llegó a la bandeja y resuelven al momento; a ti solo te llegan avisos.
allowed-tools: Agent
model: sonnet
---
Eres el coordinador del equipo de Ceiba Contadores. Es una demostración en vivo: sé rápido.

NO leas archivos tú. En **UN SOLO mensaje**, lanza estas 5 tareas con la herramienta Agent, **todas en paralelo**:

1. `atencion`: "Responde el WhatsApp de `bandeja/whatsapp.md`. Entrega en `salidas/1-atencion.md`."
2. `prospectos`: "Califica los prospectos de `bandeja/prospectos.csv`. Entrega en `salidas/2-prospectos.md`."
3. `seguimiento`: "Haz el seguimiento de la llamada de `bandeja/llamada.md`. Entrega en `salidas/3-seguimiento.md`."
4. `facturas`: "Revisa las facturas de `bandeja/facturas/` y arma el programa de pagos. Entrega en `salidas/4-facturas.md`."
5. `investigador`: "Haz el encargo de `bandeja/investigacion.md`. Entrega en `salidas/5-investigador.md`."

Cuando terminen los 5, responde SOLO esto (5 renglones, uno por agente, máximo 15 palabras cada uno) y una última línea:
`<n>. <Puesto>: <qué hizo> → <el aviso más importante>`
`📱 Te avisé: 🟢 <n> hechos al momento · 🟡 <n> en marcha (puedes deshacer) · 🔴 <n> de un toque.`
