### ROOM TYPE MODEL ###

{
  "room_type_id": "string",                   # identificador unico de room_type 
  "property_id": "string",                    # identificador unico de la propiedad
  "description": "string",
  "type": "string",                           # Tipo de cuarto (ej. Privado, compartido)
  "bathroom": "string",                       # Baño privado o compartido
  "maxOccupancy": "number",
  "inventory": "number"                       # Cantidad de cuartos del mismo tipo ¿?
}

# Notas:
# Una vez creada la propiedad el usuario crea el tipo de cuartos.
# El tipo de cuarto esta vinculado con la colección Property a traves de su Id.
# Una propiedad puede tener varios tipos de cuartos. Un tipo de cuarto solo una 
# propiedad? Si un USUARIO puede crear varias propiedades, tal vez
# las propiedades puedan compartir tipos de cuartos.

## Ejemplo de uso:
# El hostel "Un Buen Hostel" cuenta con 6 cuartos: 
# - Un cuarto privados, con cama doble y baño privado. 
# - Dos cuartos privado con cama doble y baño compartido.
# - Dos cuartos compartidos mixtos de 6 camas.
# - un cuarto compartido feminino de 4 camas.

# En este caso el dueño de "Un Buen Hostel" (Que ya creo su usuario y cargo su propiedad), 
# debe crear 4 tipos de cuartos.

{
  "room_type_id": "room_type_01",
  "property_id":"60c72b5a9b1d8e3f4f8f85c76",
  "description": "Cuarto Privado con baño",
  "type": "Private",
  "bathroom": "Private",
  "maxOccupancy": 2,
  "inventory": 1
}

{
  "room_type_id": "room_type_02",
  "property_id":"60c72b5a9b1d8e3f4f8f85c76",
  "description": "Cuarto Privado baño compartido",
  "type": "Private",
  "bathroom": "Share",
  "maxOccupancy": 2,
  "inventory": 2
}

{
  "room_type_id": "room_type_03",
  "property_id":"60c72b5a9b1d8e3f4f8f85c76",
  "description": "Cuarto compartido mixto 6 camas",
  "type": "Dormitory",
  "bathroom": "Share",
  "maxOccupancy": 6,
  "inventory": 2
}

{
  "room_type_id": "room_type_04",
  "property_id":"60c72b5a9b1d8e3f4f8f85c76",
  "description": "Cuarto compartido femenino 4 camas",
  "type": "Dormitory",
  "bathroom": "Share",
  "maxOccupancy": 4,
  "inventory": 1
}

# Podemos observar que no creamos una colección por cuarto, creamos una colección por tipo de cuarto.
# Tambien podemos observar que no hemos agredado la tarifa del cuarto, dado que yo contemplo agregar 
# las tarifas en la colección "ratesAndAvailabitity", pero
# este es un tema que hay que analizar.
# Otra cosa a tener en cuenta es la descripción. Esta representa el tipo de cuarto y debe ser unica. 
# Otra cosa a tener en cuenta es que a veces los hostels u hoteles le ponene nombre a los cuartos. En ese caso
# hay que ver donde se puede incorporar eso. Pero sin duda no va en esta colección.