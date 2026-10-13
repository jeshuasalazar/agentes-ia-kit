# Seguimiento Café Altura (Héctor Gómez)
**Lo hizo:** Seguimiento comercial · **Leyó:** bandeja/llamada.md, crm/crm.csv, negocio/precios.md, negocio/politicas.md, negocio/agenda.md, negocio/manual.md · **Para:** C.P. Lucía Ceballos

## Correo listo (borrador, 117 palabras)
**Asunto:** Propuesta para Café Altura y cuándo vernos esta semana

Hola, Héctor:

Gracias por la llamada de ayer. Me quedó claro que abrieron su segunda sucursal, que hoy son 5 personas y en diciembre serán 8. También que quieren contabilidad y nómina en un solo lugar, y que el precio les importa.

Con 45 facturas al mes y 5 empleados, tu propuesta queda en **$4,400 al mes + IVA** (contabilidad y nómina), con un arranque único de **$2,500 + IVA**. Con plan anual, la declaración anual va incluida. El detalle va en el archivo adjunto.

Podemos revisarla juntos, con Marisol si quieren, en cualquiera de estos horarios:
- Miércoles 14 de octubre, 16:00
- Jueves 15 de octubre, 12:00

¿Cuál te acomoda?

Un abrazo,
C.P. Lucía Ceballos · Ceiba Contadores

## Propuesta (adjunta; precios de ejemplo, más IVA)
| Concepto | Cálculo | Importe |
|---|---|---|
| Contabilidad mensual, persona moral hasta 50 facturas (45 al mes) | tarifa fija | $3,800 (ejemplo) |
| Nómina quincenal, 5 empleados | 5 x $90 = $450, aplica el mínimo | $600 (ejemplo) |
| **Mensualidad hoy** | $3,800 + $600 | **$4,400 + IVA** |
| Arranque de cliente nuevo (pago único) | tarifa fija | $2,500 (ejemplo) |
| **Primer pago, antes de la sesión de arranque** | $4,400 + $2,500 | **$6,900 + IVA** |

Referencias:
- **Nómina con 8 empleados (diciembre):** 8 x $90 = $720, así que la mensualidad sube a $3,800 + $720 = **$4,520 + IVA**.
- **Plan anual, solo contabilidad más nómina actual:** 12 x $4,400 = $52,800 + IVA, con la declaración anual incluida. Ese beneficio vale $4,500 (ejemplo) si se compra por separado. Si la nómina sube en diciembre, el monto del plan anual **(propuesta)** hay que confirmarlo.
- **Contrato:** mínimo de 3 meses y después mes a mes, con aviso de 30 días. Las mensualidades se pagan por adelantado.
- **Igualas:** la iguala ($4,400 y $4,520) queda por debajo del límite de $6,000, así que no necesita tu aprobación previa.

## Renglón del CRM propuesto (CSV)
Aplícalo cuando apruebes el correo. Cambia la etapa a "propuesta enviada" solo si el correo ya salió.
```csv
id,empresa,contacto,etapa,valor_mensual_estimado,ultimo_contacto,siguiente_paso,fecha_siguiente_paso,notas
102,Café Altura (ficticia),Héctor Gómez,propuesta enviada,4400,2026-10-13,Reunión para revisar propuesta con Héctor y su socia Marisol (si no contesta: llamar),2026-10-15,"Persona moral 45 facturas/mes; 5 empleados (8 en dic). Contabilidad + nómina. Pregunta por declaración anual: plan anual. Le preocupa el precio; su contadora actual le cobra $1500. Tiene carta invitación SAT. Decide con Marisol. Pendiente que Lucía revise la regularización."
```

## Otros prospectos fuera de fecha
- **103 Panadería San Juan (Elena Ruiz):** su fecha era el **9-oct** y ya pasaron 4 días sin respuesta desde la propuesta del 2-oct, con valor de $3,800. Es el más urgente. Sugiero llamar hoy o mañana y mandar un correo breve. Si quieres, preparo ese mensaje.
- **101 Talleres Ibarra** y **102** (ya arreglado arriba): tenían el siguiente paso sin fecha.
- **101 Talleres Ibarra (Rodrigo Ibarra):** el paso es "Calificar" y no tiene fecha. Sugiero calificarlo a más tardar mañana, 14-oct.
- **104 Clínica Dental Salcedo:** llegó hoy y su paso "Calificar" no tiene fecha. No está atrasado, pero conviene ponerle fecha.

## Revisé
- ✅ Precios tomados de `negocio/precios.md`: $3,800 + $600 = $4,400; $4,400 + $2,500 = $6,900; 8 x $90 = $720 y $3,800 + $720 = $4,520; 12 x $4,400 = $52,800.
- ✅ Los 5 empleados dan $450, menos que el mínimo de $600, por eso se cobra $600.
- ✅ Los dos horarios (mié 14 a las 16:00 y jue 15 a las 12:00) están libres en `agenda.md`. No ofrecí el viernes 16, que está ocupado.
- ✅ El correo tiene 117 palabras y pide una sola cosa (elegir horario). No iguala el precio de la prima ni da descuentos.
- ❌ Falta un dato: no sé cuántos meses de atraso tiene Café Altura ni qué pide la carta invitación del SAT. El correo no promete nada sobre eso. Si son más de 4 meses atrasados, la regularización la decides tú.

## Tú decides
- **Carta invitación del SAT y regularización:** no la incluí en el precio porque no sé el atraso. Recomiendo preguntarlo en la reunión (pedirles que traigan la carta) y cotizar la regularización después, a $1,500 (ejemplo) por mes atrasado.
- **Arranque esta semana:** la declaración vence el sábado 17, así que el arranque tendría que ser el 14 o el 15, y eso lo decides tú. Recomiendo no prometerlo y proponer el arranque para el lunes 19, pues hay huecos a las 9:00 y las 12:00.
- **Descuento o precio especial por el costo de $1,500 de la prima:** no lo ofrecí. Recomiendo defender el valor (nómina, 2 sucursales, declaración anual incluida) y no bajar el precio, salvo que tú decidas lo contrario.
