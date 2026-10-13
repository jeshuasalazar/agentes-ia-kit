# Revisión de facturas y programa de pagos (martes 13-oct-2026)
**Lo hizo:** Facturas y cuentas por pagar · **Leyó:** negocio/proveedores.md, bandeja/facturas/01 a 06 (XML) · **Para:** C.P. Lucía Ceballos

## Facturas revisadas
| # | Proveedor | Folio / UUID | Total | Vence | Estado | Motivo |
|---|---|---|---|---|---|---|
| 03 | Torre Ceibas Inmobiliaria | R-0310 / C9E3B5A7-0D14-4F62-B8A9-3E7C1D5F9024 | $20,880.00 | 01-oct (vencida) | **Pagar** | Todo cuadra: 18,000.00 + 2,880.00 = 20,880.00; IVA 16%. PUE. Renta de octubre, se paga el día 1 y ya pasó. |
| 02 | Papelería Los Arcos | PA-5521 / A41D7E02-58C3-4B9F-8E10-6D2F9A3B7C45 | $1,450.00 | 10-oct (vencida, contado) | **Pagar** | Cuadra: 1,250.00 + 200.00 = 1,450.00; IVA 16%. PUE. Es la primera vez que aparece este UUID. |
| 01 | Nube Norte Software | A-1187 / 6F2A9C14-3B7E-4D21-9A55-1C0E8B7D2F31 | $9,860.00 | 16-oct (viernes) | **Pagar (jueves 15)** | Cuadra: 8,500.00 + 1,360.00 = 9,860.00; IVA 16%. PPD: al pagar, pedir complemento de pago. Como solo pagamos martes y jueves, el último día para pagar a tiempo es el jueves 15. |
| 04 | Enlace Total Telecom | ET-88214 / 5B8F1D3C-7A26-4E94-A0C7-9D2E4F6B1A83 | $2,563.00 (según XML) | 15-oct | **Aclarar** | Subtotal 2,100.00 + IVA 336.00 = 2,436.00, pero el XML dice Total 2,563.00: diferencia de $127.00. El IVA sí es el 16%. PPD. |
| 05 | Limpieza Brillo | LB-2290 / E27A4C9B-1F83-4D56-9B0E-8C3A5D7F2E16 | $3,712.00 | 23-oct | **Aclarar** | El RFC del receptor es CCO140215AB**8**, y el del despacho es CCO140215AB**3**. Los importes sí cuadran (3,200.00 + 512.00 = 3,712.00). PPD. |
| 06 | Papelería Los Arcos | PA-5521 / A41D7E02-58C3-4B9F-8E10-6D2F9A3B7C45 | $1,450.00 | n/a | **No pagar** | Duplicada de la 02: mismo UUID, folio, fecha e importes. Se paga una sola vez. |

## Programa de pagos propuesto
Ordenado por vencimiento. Presupuesto de la semana: $40,000.00.

| Orden | Día de pago | Proveedor | Vencía | Monto |
|---|---|---|---|---|
| 1 | Martes 13-oct (hoy) | Torre Ceibas (renta octubre) | 01-oct | $20,880.00 |
| 2 | Martes 13-oct (hoy) | Papelería Los Arcos (PA-5521) | 10-oct | $1,450.00 |
| 3 | Jueves 15-oct | Nube Norte Software (A-1187) | 16-oct | $9,860.00 |
| | | **Total a pagar** | | **$32,190.00** |

- Presupuesto $40,000.00 − $32,190.00 = **$7,810.00 disponibles**.
- Pendientes de aclarar, que caben en lo disponible: Enlace Total ($2,436.00 o $2,563.00, según lo que corrija el proveedor) y Limpieza Brillo ($3,712.00). Si se pagaran las dos, el total sería de $38,338.00 (con Enlace en $2,436.00) o $38,465.00 (con Enlace en $2,563.00), y seguiría dentro del presupuesto.
- Hoy: $20,880.00 + $1,450.00 = $22,330.00. Jueves: $9,860.00.

## Correos para proveedores (borradores, no se envían sin tu aprobación)

**Enlace Total Telecom (factura ET-88214)**
> Asunto: Diferencia en el total de la factura ET-88214
> Hola, equipo de Enlace Total. Revisamos la factura ET-88214 (UUID 5B8F1D3C-7A26-4E94-A0C7-9D2E4F6B1A83). El subtotal es $2,100.00 y el IVA $336.00, que suman $2,436.00, pero el total del comprobante dice $2,563.00 (diferencia de $127.00). ¿Nos pueden confirmar el importe correcto y, si hay un error, enviarnos la factura corregida con su cancelación o una nota de crédito? Vence el 15 de octubre y queremos pagarla a tiempo. Gracias. Ceiba Contadores.

**Limpieza Brillo (factura LB-2290)**
> Asunto: RFC del receptor incorrecto en la factura LB-2290
> Hola, equipo de Limpieza Brillo. La factura LB-2290 (UUID E27A4C9B-1F83-4D56-9B0E-8C3A5D7F2E16) trae el RFC receptor CCO140215AB8. El RFC correcto de Ceiba Contadores es CCO140215AB3. ¿Nos pueden emitir de nuevo la factura con el RFC correcto y cancelar la anterior? Con la corrección programamos el pago. Gracias. Ceiba Contadores.

**Papelería Los Arcos (aviso opcional)**
> Asunto: Factura PA-5521 recibida dos veces
> Hola. Recibimos dos veces la factura PA-5521 (mismo UUID A41D7E02-58C3-4B9F-8E10-6D2F9A3B7C45). Pagaremos una sola vez; solo para que lo tengan en cuenta. Gracias. Ceiba Contadores.

## Revisé
- ✅ Receptor = CCO140215AB3 en 5 de 6 facturas. ❌ La 05 trae CCO140215AB8.
- ✅ Subtotal + IVA = Total al centavo en 5 de 6. ❌ La 04 difiere en $127.00 (2,436.00 contra 2,563.00).
- ✅ IVA = 16% del subtotal en las 6 (1,360 / 200 / 2,880 / 336 / 512 / 200).
- ✅ UUID: 5 únicos. ❌ La 06 repite el UUID de la 02 y no se paga.
- ✅ Total del programa recalculado dos veces: 20,880 + 1,450 + 9,860 = 32,190, dentro de $40,000. Los vencimientos salen del crédito de `proveedores.md` y la fecha del XML. Ninguna factura trae retenciones.

## Tú decides
- **Autorizar el programa** ($22,330.00 hoy y $9,860.00 el jueves). Recomiendo autorizarlo. La renta y la papelería ya están vencidas. Antes de pagar la renta, confirma que no se pagó ya por otro medio, porque el XML no lo indica.
- **Enviar los correos a Enlace Total y Limpieza Brillo hoy.** Recomiendo que sí. Enlace vence el jueves 15 y, si no responde, esa factura no se paga a tiempo. No pagues el total de $2,563.00 sin aclaración.
- **Nube Norte (PPD) y Enlace Total (PPD).** Recomiendo pedirles su complemento de pago al pagar.
