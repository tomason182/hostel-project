### Reservations ###

{
  "reservation_id": "string",                   # Identificador unico de la reserva
  "guess_id": "string",                         # Identificador unico del huesped
  "room_id": "string",                          # Identificador unico de la habitación
  "check_in_date": "string",                    # Fecha de ingreso formato ISO 8601
  "check_out_date": "string",                   # Fecha de egreso formato ISO 8601
  "number_of_guess": "number",                  # Numero total de huespedes
  "total_price": "number",                      # Importe total a pagar
  "currency": "string",                         # Moneda del importe total (ej., USD, EUR, ARS)
  "reservation_status": "string",               # Estado de la reserva (ej., confirmada, cancelada, etc)
  "payment_status": "string",                   # Estado del pago (ej. pagado, pendiente, etc)
  "special_request": "string",                  # Requisitos especiales o notas  
  "createAt": "string",                         # Timestamp creación de la reserva
  "updateAt": "string"                          # Timestamp actualización de la reserva
}


# Ejemplo del documento
{
  "reservation_id": "res12346",
  "guess_id": "guess1234",
  "room_id": "room101",
  "check_in_date": "2024-07-28",
  "check_out_date": "2024-08-02",
  "number_of_guess": 3,
  "total_price": 150,
  "currency": "USD",
  "reservation_status": "confirmed",
  "payment_status": "pending",
  "special_request": "late check in if possible",
  "createAt": "2024-07-25T14:00:05",
  "updateAt": "2024-07-25T14:00:05"
}