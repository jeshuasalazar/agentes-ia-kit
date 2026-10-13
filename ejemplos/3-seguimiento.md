# Seguimiento a Café Altura (Héctor Gómez)
**Lo hizo:** Seguimiento comercial · **Leyó:** bandeja/llamada.md, crm/crm.csv, negocio/precios.md, negocio/politicas.md, negocio/agenda.md, negocio/manual.md · **Para:** C.P. Lucía Ceballos

## Correo listo

**Para:** Héctor Gómez (Café Altura)
**Asunto:** Tu propuesta y dos horarios para vernos esta semana

Hola, Héctor:

Gracias por la llamada de ayer. Me contaste que abrieron su segunda sucursal, que hoy son 5 en el equipo, que serán 8 en diciembre y que ya les llegó una carta invitación del SAT. Conviene ordenarlo pronto.

Para Café Altura (persona moral, unas 45 facturas al mes):
- Contabilidad mensual: $3,800 + IVA
- Nómina de 5 empleados: $600 + IVA (con 8 en diciembre: $720 + IVA)
- Arranque, un solo pago: $2,500 + IVA

Son $4,400 + IVA al mes. Con plan anual, la declaración anual va incluida.

Sé que el precio te importa. Cuando nos veamos te explico qué incluye cada parte.

¿Nos vemos el miércoles 14 a las 16:00 o el jueves 15 a las 12:00? Si Marisol puede acompañarnos, mejor.

Un abrazo,
C.P. Lucía Ceballos · Ceiba Contadores

*(Palabras del cuerpo: aprox. 125)*

## Propuesta (precios de ejemplo, más IVA)

| Concepto | Cálculo | Importe |
|---|---|---|
| Contabilidad mensual, persona moral hasta 50 facturas | tarifa de lista | $3,800 |
| Nómina quincenal, 5 empleados | 5 × $90 = $450, aplica mínimo | $600 |
| **Mensualidad hoy** | 3,800 + 600 | **$4,400** |
| Mensualidad desde diciembre (8 empleados) | 3,800 + (8 × $90 = $720) | $4,520 |
| Arranque de cliente nuevo (pago único) | tarifa de lista | $2,500 |
| **Primer pago (arranque + 1.ª mensualidad)** | 2,500 + 4,400 | **$6,900** (con IVA 16%: $8,004) |
| Plan anual (propuesta) | 12 × $3,800 + 12 × $600 = 45,600 + 7,200 | $52,800 + arranque $2,500 = $55,300 |

Notas:
- Plan anual: incluye la declaración anual, que sin plan cuesta $4,500 (persona moral).
- La nómina de diciembre en el plan anual **(propuesta)** habría que ajustarla a 8 empleados. Lo defines tú.
- Contrato mínimo de 3 meses, después mes a mes; cancelación con 30 días de aviso. Mensualidad por adelantado.
- La iguala ($4,400 y $4,520) está por debajo del límite de $6,000, no requiere tu aprobación por monto.

## Renglón del CRM propuesto (CSV)

```csv
id,empresa,contacto,etapa,valor_mensual_estimado,ultimo_contacto,siguiente_paso,fecha_siguiente_paso,notas
102,Café Altura (ficticia),Héctor Gómez,propuesta enviada,4400,2026-10-13,Reunión para cerrar (decide con su socia Marisol),2026-10-14,"Persona moral ~45 facturas; 5 empleados (8 en dic); carta invitación SAT; le preocupa precio (prima cobra $1,500); interesa plan anual por declaración incluida; sin descuento ofrecido"
```

## Otros prospectos pasados de fecha
- **103 Panadería San Juan (Elena Ruiz):** su siguiente paso "Llamar para cerrar" era el 2026-10-09, lleva 4 días vencido y 11 sin contacto (último 2026-10-02). Propuesta: llamarle hoy y fijar nueva fecha 2026-10-14.
- **101 Talleres Ibarra y 104 Clínica Dental Salcedo:** "Calificar" sin fecha. Aún no están vencidos, pero sin fecha pueden enfriarse. Propuesta: fecha 2026-10-14 para ambos.

## Revisé
- ✅ Precios tomados de `negocio/precios.md` y sumas verificadas: 3,800 + 600 = 4,400; 2,500 + 4,400 = 6,900; ×1.16 = 8,004.
- ✅ Nómina: 5 × $90 = $450 queda debajo del mínimo, se cobra $600; con 8 empleados, $720.
- ✅ Horarios (mié 14 a las 16:00, jue 15 a las 12:00) están libres en `negocio/agenda.md`. El viernes 16 está ocupado.
- ✅ Sin descuento ni igualar a la prima; solo prometí lo que dijiste: declaración anual incluida con plan anual.
- ❌ Plazo: la declaración vence el 17 y el arranque debe ser 2 días hábiles antes. El miércoles 14 cumple; el jueves 15 queda justo. El pago de arranque debe llegar antes de la sesión.

## Tú decides
- 🔴 **Arranque esta misma semana (14 o 15 oct)** · Recomiendo sí, por la carta del SAT; por ahora el correo solo ofrece reunión · Si no respondes: no se promete
- 🔴 **Descuento si Héctor lo pide por el precio de la prima** · Recomiendo no igualar; resaltar valor y plan anual · Si no respondes: precio de lista
- 🟡 **Correo a Héctor con propuesta y dos horarios** · sale a las 13:00 si no dices nada
- 🟢 **Revisé el CRM y detecté la Panadería San Juan vencida** · hecho; tú aplicas los cambios
