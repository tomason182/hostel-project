### Guess ###
# Modelo de la colección referida a huespedes / pasajeros

{
  "guess_id": "string",                   # Identificador del huesped
  "first_name": "string",                 # Datos relacionados con el huesped...
  "last_name": "string",                  
  "email": "string",                      
  "phone_number": "string",
  "address": {
    "street": "string",
    "city": "string",
    "country": "string",
    "postal_code": "string"
  },
  "gender": "string",
  "nationality": "string",
  "passport_number": "string",
  "loyalty_program": {                      # Programa de lealtad. No es útil ahora pero se lo puede tener en cuenta
    "membership_number": "string",          # para el futuro, donde el viajero va sumando puntos si utiliza la pagina para
    "points": "number",                     # reservar y asi optiene descuentos, promociones, etc
  },
  "created_At": "string",
  "updated_At": "string"
}


# Ejemplo del documento
{
  "guess_id": "guest6789",
  "first_name": "Esteban",
  "last_name": "Quito",
  "email": "esteban@mail.com",
  "phone_number": "+5491154653357",
  "address": {
    "street": "av. San Martin 123",
    "city": "Buenos Aires",
    "country": "Argentina",
    "postal_code": "B1675"
  },
  "gender": "male",
  "nationality": "Argentina",
  "passport_number": "AR123456789",
  "loyalty_program": {
    "membership_number": "LP789456",
    "points": 1500,
  },
  "created_At": "2024-07-25T14:00:00Z",
  "updated_At": "2024-07-25T14:00:00Z"
}