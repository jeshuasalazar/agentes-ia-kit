# Facturas de la semana y programa de pagos
**Lo hizo:** Facturas y cuentas por pagar · **Leyó:** negocio/proveedores.md, negocio/manual.md, bandeja/facturas/ (6 XML) · **Para:** C.P. Lucía Ceballos

Hoy: martes 13-oct-2026. Se paga martes y jueves. Receptor correcto: CCO140215AB3.

## Revisión de las 6 facturas
| # | Proveedor | Total | Vence | Estado | Motivo |
|---|---|---|---|---|---|
| 01 | Nube Norte Software (A-1187, PPD) | $9,860.00 | 16-oct (15 días desde 01-oct) | 🟡 Pagar | Cuadra: 8,500.00 + 1,360.00 = 9,860.00. Al pagar, pedir complemento de pago (PPD). |
| 02 | Papelería Los Arcos (PA-5521, PUE) | $1,450.00 | 10-oct (contado; ya venció) | 🟡 Pagar | Cuadra: 1,250.00 + 200.00 = 1,450.00. Pagar hoy. |
| 03 | Torre Ceibas, renta oct. (R-0310, PUE) | $20,880.00 | 01-oct (se paga el día 1; ya venció) | 🟡 Pagar | Cuadra: 18,000.00 + 2,880.00 = 20,880.00. No hay registro de que ya se pagó; confirma que no esté pagada. |
| 04 | Enlace Total Telecom (ET-88214, PPD) | $2,563.00 | 15-oct (10 días desde 05-oct) | 🔴 Aclarar | No cuadra: 2,100.00 + 336.00 = 2,436.00, pero el Total dice 2,563.00. Diferencia de $127.00. |
| 05 | Limpieza Brillo (LB-2290, PPD) | $3,712.00 | 23-oct (15 días desde 08-oct) | 🔴 Aclarar | RFC del receptor equivocado: dice CCO140215AB8 y el nuestro es CCO140215AB3. Los importes sí cuadran (3,200.00 + 512.00). |
| 06 | Papelería Los Arcos (PA-5521) | $1,450.00 | n/a | 🔴 No pagar | Duplicada de la 02: mismo UUID A41D7E02-58C3-4B9F-8E10-6D2F9A3B7C45, mismo folio, fecha e importe. |

## Programa de pagos (ordenado por vencimiento)
| Orden | Proveedor | Fecha de pago | Monto |
|---|---|---|---|
| 1 | Torre Ceibas (renta oct.), venció 01-oct | Hoy mar 13-oct | $20,880.00 |
| 2 | Papelería Los Arcos (02), venció 10-oct | Hoy mar 13-oct | $1,450.00 |
| 3 | Nube Norte Software, vence 16-oct | Jue 15-oct (último día de pago antes del vencimiento) | $9,860.00 |
| | **Total a pagar** | | **$32,190.00** |

- Presupuesto de la semana: $40,000.00. Queda libre: $7,810.00. Estás dentro del presupuesto.
- Las dos facturas pendientes (04 y 05) no se incluyen. Si Enlace Total corrige a $2,436.00, el total sería $34,626.00, todavía dentro del presupuesto. La 04 vence el 15-oct, así que hay que resolverla antes del jueves.
- No se paga la 06 (duplicada).
- Sumas revisadas dos veces: 20,880 + 1,450 = 22,330; 22,330 + 9,860 = 32,190.

## Correos a proveedores (cortos)

**Para: Enlace Total Telecom** · Asunto: Aclaración factura ET-88214
Hola, revisamos su factura ET-88214 (UUID 5B8F1D3C-7A26-4E94-A0C7-9D2E4F6B1A83). El subtotal es $2,100.00 y el IVA $336.00, que suman $2,436.00, pero el total marca $2,563.00 (diferencia de $127.00). ¿Nos pueden confirmar el importe correcto y enviar la factura corregida, o la nota de crédito si aplica? Vence el 15-oct y queremos pagarla a tiempo. Gracias.
Ceiba Contadores

**Para: Limpieza Brillo** · Asunto: Corrección de RFC, factura LB-2290
Hola, su factura LB-2290 (UUID E27A4C9B-1F83-4D56-9B0E-8C3A5D7F2E16) viene a nombre del RFC CCO140215AB8. El RFC correcto de Ceiba Contadores es CCO140215AB3. ¿Nos pueden cancelar y reemitir la factura con el RFC correcto, con los mismos importes ($3,712.00)? Vence el 23-oct. Gracias.
Ceiba Contadores

## Revisé
- ✅ Receptor vs. RFC del despacho en las 6 facturas: ❌ la 05 trae CCO140215AB8.
- ✅ Subtotal + IVA = Total al centavo: ❌ la 04 tiene una diferencia de $127.00. Las otras 5 cuadran.
- ✅ IVA = 16% del subtotal: cuadra en las 6. En la 04 el IVA está bien y el error está en el total.
- ✅ UUID repetido: ❌ la 06 repite el UUID de la 02. Los otros 5 son distintos.
- ✅ Vencimientos con el crédito de cada proveedor. ❌ La renta (03) y la papelería (02) ya están vencidas. No tengo registro de pagos anteriores, así que no puedo confirmar que la renta no se haya pagado el 01-oct.

## Tú decides
- 🔴 **Confirmar que la renta de octubre ($20,880.00) no está pagada** · Si ya se pagó, la quito del programa · Si no respondes: no se paga nunca.
- 🟡 **Pagar renta, papelería (hoy) y Nube Norte (jueves 15): $32,190.00** · sale a las 13:00 si no dices nada
- 🟡 **Correos de aclaración a Enlace Total y Limpieza Brillo** · salen a las 13:00 si no dices nada
- 🟢 **Marqué la factura 06 como duplicada, no pagar** · hecho
