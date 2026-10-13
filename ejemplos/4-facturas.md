# Facturas del 13-oct-2026: 3 a pagar, 2 por aclarar, 1 duplicada
**Lo hizo:** Facturas y cuentas por pagar · **Leyó:** negocio/proveedores.md, negocio/manual.md, bandeja/facturas/ (6 XML) · **Para:** C.P. Lucía Ceballos

## Tabla de facturas
| # | Proveedor | Total | Vence | Estado | Motivo |
|---|---|---|---|---|---|
| 03 | Torre Ceibas Inmobiliaria | $20,880.00 | 01-oct (vencida) | **Pagar** | Cuadra: 18,000.00 + 2,880.00. Renta de octubre, pago el día 1. |
| 02 | Papelería Los Arcos | $1,450.00 | 10-oct (vencida) | **Pagar** | Cuadra: 1,250.00 + 200.00. Contado. PUE. |
| 01 | Nube Norte Software | $9,860.00 | 16-oct | **Pagar** | Cuadra: 8,500.00 + 1,360.00. Crédito 15 días desde el 01-oct. PPD: pedir complemento de pago. |
| 04 | Enlace Total Telecom | $2,563.00 | 15-oct | **Aclarar** | Subtotal 2,100.00 + IVA 336.00 = 2,436.00, pero el CFDI dice 2,563.00 (sobran $127.00). |
| 05 | Limpieza Brillo | $3,712.00 | 23-oct | **Aclarar** | RFC del receptor es CCO140215AB**8**, no CCO140215AB**3**. Importes sí cuadran (3,200.00 + 512.00). |
| 06 | Papelería Los Arcos | $1,450.00 | n/a | **No pagar** | Duplicada de la 02: mismo folio fiscal A41D7E02-58C3-4B9F-8E10-6D2F9A3B7C45, serie PA, folio 5521. |

## Programa de pagos (martes 13-oct, 13:00), por vencimiento
| Orden | Proveedor | Vence | Monto |
|---|---|---|---|
| 1 | Torre Ceibas Inmobiliaria (renta octubre) | 01-oct | $20,880.00 |
| 2 | Papelería Los Arcos (factura 5521) | 10-oct | $1,450.00 |
| 3 | Nube Norte Software (A-1187) | 16-oct | $9,860.00 |
| | **Total programado** | | **$32,190.00** |

Presupuesto de la semana: $40,000.00. Queda disponible: **$7,810.00**.
Suma revisada dos veces: 20,880 + 1,450 = 22,330; 22,330 + 9,860 = 32,190. Y en sentido inverso: 9,860 + 1,450 = 11,310; 11,310 + 20,880 = 32,190.

Aunque Nube Norte vence el viernes 16 y el siguiente día de pago es el jueves 15, lo dejé hoy para no arriesgar el vencimiento.

## Correos enviados a proveedores (ya salieron)
**Para: facturacion@enlacetotal (propuesta de destinatario; no consta en el XML)**
Asunto: Aclaración factura ET-88214: el total no coincide con subtotal más IVA
Hola, equipo de Enlace Total. Revisamos la factura ET-88214 (folio fiscal 5B8F1D3C-7A26-4E94-A0C7-9D2E4F6B1A83). Subtotal $2,100.00 + IVA $336.00 suma $2,436.00, pero el total timbrado es $2,563.00 (diferencia de $127.00). ¿Nos pueden indicar a qué corresponde esa diferencia, o enviarnos la factura corregida con su cancelación o nota de crédito? En cuanto la recibamos la programamos en el siguiente día de pago (martes o jueves). Gracias. Ceiba Contadores.

**Para: facturacion@limpiezabrillo (propuesta de destinatario; no consta en el XML)**
Asunto: Factura LB-2290 emitida con RFC receptor incorrecto
Hola, equipo de Limpieza Brillo. La factura LB-2290 (folio fiscal E27A4C9B-1F83-4D56-9B0E-8C3A5D7F2E16) viene al RFC CCO140215AB8. El RFC correcto de Ceiba Contadores es CCO140215AB3. ¿Nos pueden cancelar esa factura y reexpedirla con el RFC correcto, mismos importes ($3,200.00 + IVA $512.00 = $3,712.00)? Al recibirla la programamos para pago antes del 23-oct. Gracias. Ceiba Contadores.

No envié correo por la factura 06: es una copia exacta de la 02 y no se paga.

## Revisé
- ✅ Receptor = CCO140215AB3 en 5 de 6 facturas. ❌ La 05 trae CCO140215AB8.
- ❌ Subtotal + IVA = Total al centavo en 4 facturas, pero la 04 no cuadra ($2,436.00 contra $2,563.00).
- ✅ IVA = 16% del subtotal en las 6 (1,360 / 200 / 2,880 / 336 / 512 / 200).
- ❌ UUID repetido: 02 y 06 son el mismo (A41D7E02…7C45). Los otros 4 son únicos.
- ✅ Los 4 proveedores de las facturas por pagar o aclarar están en la lista. Programado $32,190.00 de $40,000.00.

## Te aviso
- 🟡 **Programé 3 pagos por $32,190.00 (renta, papelería, Nube Norte)** · sale a las 13:00 de hoy · puedes deshacerlo
- 🟢 **Escribí a Enlace Total (total con $127 de más) y a Limpieza Brillo (RFC equivocado)**; ambas sin pagar · hecho al momento
- 🟢 **No pagué la factura repetida de Papelería Los Arcos (mismo folio fiscal)** · hecho al momento
- 🟢 **Pendiente: pedir a Nube Norte el complemento de pago (PPD) tras el pago** · hecho al momento
