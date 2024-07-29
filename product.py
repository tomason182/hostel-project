### Product model ###

# La colección producto combina el tipo de cuarto y el plan de tarifa para crear un
# producto (habitación / cuarto) unico.
# En este modelo tambien se agregan las politicas y restricciones (cancelaciones, pagos adelantados, etc)

{
  "product_id": "ObjectID()",
  "property_id": "Property[1]",
  "room_type": "RoomType[1]",
  "rate_plan": "RatePlan[1..*]",
  "name": "string",
  "description": "string",
  "custom_occupancy": "number",                     # La ocupación maxima viene establecida por "room_type", pero tal vez el usuario quiera modificar la cantidad de ocupantes indivdualmente.
  "base_rate_per_night": "number"                   # Creo que el valor de la tarifa es mejor fijarlo en el calendario. Aca no va...
}

## EJEMPLOS ##

# En este punto el usuario ingreso los datos de su propiedad, creo los tipos de cuartos y 
# los planes de tarifas.
# Este modelo se puede crear por defecto, pero puede ser editable por el usuario.

{
  "product_id": "product001",
  "property_id": "60c72b5a9b1d8e3f4f8f85c78",
  "room_type": "room_type_003",
  "rate_plan": ["ratePlan001", "ratePlan002", "ratePlan003"],
  "name": "El refugio",                                               # Por defecto se le da un nombre "Room-001".
  "description": "Aca va la descripción del cuarto",                  # No se si este campo es necesario.
  "custom_occupancy": 3,                                              # Por defecto seria 6.
} 