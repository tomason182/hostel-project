### Property model ###

{
  "property_id": "string",
  "property_name": "string",
  "address": [{
    "street": "string",
    "city": "string",
    "postal_code": "string",
    "country_code": "string",
  }],
  "contact_info": {
    "phone_number": "string",
    "email": "string",
  },
  "room_type": "string",               # room_type_id > Vincula la propiedad con la coleccion "room_type"
  "rate_plan": "string",               # rate_plan_id > Vincula la propiedad con la coleccion "rate_plan" 

  "createdBy": "string",               # user_id del usuario que creo la propiedad
  "createdAt": "string",               # timestamp
  "updateAt": "string"                 # timestamp
}


# Descripción de la colección Property:
# Una vez el usuario crea una cuenta, carga los datos de su propiedad.
# Esta collección se vincula con las coleciones de "room_types" (tipos de habitaciones) y "rate_plans" (planes de tarifas).
# Para entender mejor room_types y rate_plan ver las colecciones correspondientes