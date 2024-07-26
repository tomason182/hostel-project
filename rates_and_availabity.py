### Rate & availability ###

# Dos modelos de ejemplo de como podria estructurarce la colección de tarifas y disponibilidad
# El primer ejemplo contempla tener una sección de "tarifas especiales" y un "tarifa base" como valor madre.
# En el segundo ejemplo incorporo la tarifa en cada uno de los items de la disponibilidad.

# ** Nota: Me acabo de dar cuenta que esto modelos no contemplan la cantidad de camas **
# ** Hay que diferenciar cuartos privados de compartidos ? como lo manejamos ?        **
# ** Cuartos privados se cierra disponibilidad cuando el cuarto se reserva            **
# ** Cuarto compartido se cierra disponibilidad cuando todas las camas se reservan    **


## Ejemplo 1 ##
{
  "room_id": "string",                    # Id del dormitorio / cuarto
  "base_rate_per_night": "number",        # Tarifa base por noche 
  "currency": "string",                   # Moneda de la tarifa (ej. USD, EUR, ARS)
  "availability": [ 
    {
      "date": "string",                   # Fecha de disponibilidad ISO 8601 (e.g 2024-07-25T15:02:00)
      "is_available": "boolean",          # Status de la disponibilidad para la fecha determinada
    }
  ],
  "special_rates": [                      # Tarifas especiales
    {
      "start_date": "string",             # Fecha de inicio de la tarifa
      "end_date": "string",               # Fecha de final de la tarifa
      "rate_per_night": "number",         # valor de la tarifa para la fecha en cuestion
    }
  ],
  "Created_At": "string",                 # Timestamp creación del documento
  "Updated_At": "string"                  # Timestamp actualización del documento 
}


# el documento - ejemplo de creación #
{
  "room_id": "room101",
  "base_rate_per_night": 12,
  "currency": "USD",
  "availability": [
    { "date": "2024-07-26", "is_available": True },
    { "date": "2024-07-26", "is_available": True },
    { "date": "2024-07-26", "is_available": True },
    { "date": "2024-07-26", "is_available": True },
    { "date": "2024-07-26", "is_available": True },
    { "date": "2024-07-26", "is_available": True },
    { "....": "..........", "............": ".." },   # Asi continua el calendario por un año / dos años ...?
  ],
  "special_rates": [
    {
      "start_date": "2024-08-23",
      "end_date": "2024-08-26",
      "rate_per_night": 15
    },
    {
      "start_date": "2024-09-12",
      "end_date": "2024-09-16",
      "rate_per_night": 18
    }
  ],
  "created_At": "2024-07-26T15:17:56",
  "update_AT": "2024-07-26T15:17:56"
}


## Ejemplo 2 ##

# Acá metemos la tarifa dentro del objeto disponibilidad

{
  "room_id": "string", 
  "currency": "string",                
  "availability": [ 
    {
      "date": "string",                
      "is_available": "boolean",
      "rate": "number"                  
    }
  ],
  "Created_At": "string",                
  "Updated_At": "string"                 
}

## Ejemplo de la creación de un documento ##

{
  "room_id": "room101",                    
  "currency": "USD",                   
  "availability": [ 
    { "date": "2024-07-26", "is_available": "true", "rate": 10 },
    { "date": "2024-07-27", "is_available": "true", "rate": 10 },
    { "date": "2024-07-28", "is_available": "true", "rate": 10 },
    { "date": "2024-07-29", "is_available": "true", "rate": 10 },
    { "date": "2024-07-30", "is_available": "true", "rate": 10 },
    { "date": "2024-07-31", "is_available": "true", "rate": 12 },
    { "date": "2024-08-01", "is_available": "true", "rate": 12 },
  ],
  "Created_At": "2024-07-26T15:26:56",              
  "Updated_At": "2024-07-26T15:26:56"               
}


## Notas: 
# la disponibilidad "availability va a quedar super extensa. Hay que almacenar disponibilidad indefinida.(minimo un año)"
# Otra posibilidad es armar rangos. Ir modificando el rango a medida que llegan reservas.

## Ejemplo 3 con rangos ##

{
  "room_id": "string",                    # Id del dormitorio / cuarto
  "base_rate_per_night": "number",        # Tarifa base por noche 
  "currency": "string",                   # Moneda de la tarifa (ej. USD, EUR, ARS)
  "availability": [ 
    {
      "from": "string",                   # Fecha inicio disponibilidad ISO 8601 (e.g 2024-07-25T15:02:00)
      "to": "string",                     # Fecha fin disponibilidad ISO 8601 (e.g 2024-07-25T15:02:00)
      "is_available": "boolean",          # Status de la disponibilidad
    }
  ],
  "special_rates": [                      # Tarifas especiales
    {
      "start_date": "string",             # Fecha de inicio de la tarifa
      "end_date": "string",               # Fecha de final de la tarifa
      "rate_per_night": "number",         # valor de la tarifa para la fecha en cuestion
    }
  ],
  "Created_At": "string",                 # Timestamp creación del documento
  "Updated_At": "string"                  # Timestamp actualización del documento 
}

# Ejemplo de la creación de un documento #

{
  "room_id": "room101",                    
  "base_rate_per_night": 10,        
  "currency": "USD",                
  "availability": [ 
    {
      "from": "2024-07-26",      
      "to": "2024-07-29",       
      "is_available": "true",
    },
    {
      "from": "2024-07-30",             
      "to": "2024-08-03",               
      "is_available": "false"           # Este rango de fechas no esta disponible (reservado, cerrado, etc)
    },
    {
      "from": "2024-08-04",
      "to": "2054-12-31",
      "is_available": True
    }

  ],
  "special_rates": [                      # Tarifas especiales
    {
      "start_date": "string",
      "end_date": "string",
      "rate_per_night": "number",
    }
  ],
  "Created_At": "string",
  "Updated_At": "string"
}


# De esta manera el documento queda menos extendido, pero hay que tener en cuenta que hay que modificar, crear y insertar rangos a medida que llegan reservas
# Supongamos que llega una reserva ** "from": "2024-08-24" "to": "2024-08-26" **

## ese proceso llevaria, desarmar el rango esablecido como "true" anteriormente, y crear tres rangos mas: 
## uno anterior a la reserva "is_available": "true"
## el de la reserva "is_available": "false"
## uno posterior a la reserva "is_available: "true"