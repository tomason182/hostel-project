### Rate & availability ###


## MODELO PRINCIPAL ###

# Hasta este momento el usuario: agrego los datos de su propiedad, creo tipos de cuartos y planes de tarifas y se generaron
# todos los cuartos (editables) que contiene la propiedad.
# En este momento es necesario establecer la disponibilidad y tarifa diaria de cada cuarto.
# Por lo tanto esta Colección esta vinculada directamente con cada cuarto (Product).
# La relación en este caso es One-to-One.
# De la colección "Product" obtenemos "custom_occupancy", lo que nos va a permitir determinar cuantas camas disponibles van quedando,
# y cuando el cuarto se ha reservado por completo (CUSTOM_OCCUPANCY - RESERVAS PARA EL CUARTO)

{
  "rate_and_availability_id": "ObjectID()",               # Id unica del documento. Se crea un documento unico por cuarto.
  "product_id": "string",                                 # Vincula la colección con la colección "Product"
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
  "rate_and_availability_id": "rate_availability_001",
  "product_id": "product101",                    
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



### OTROS EJEMPLOS DEL MODELO ###


## Ejemplo 1 ##
{
  "rate_and_availability_ID": "ObjectID()",
  "room_id": "string",                          # Id del dormitorio / cuarto
  "base_rate_per_night": "number",              # Tarifa base por noche 
  "currency": "string",                         # Moneda de la tarifa (ej. USD, EUR, ARS)
  "availability": [ 
    {
      "date": "string",                         # Fecha de disponibilidad ISO 8601 (e.g 2024-07-25T15:02:00)
      "is_available": "boolean",                # Status de la disponibilidad para la fecha determinada
    }
  ],
  "special_rates": [                            # Tarifas especiales
    {
      "start_date": "string",                   # Fecha de inicio de la tarifa
      "end_date": "string",                     # Fecha de final de la tarifa
      "rate_per_night": "number",               # valor de la tarifa para la fecha en cuestion
    }
  ],
  "Created_At": "string",                       # Timestamp creación del documento
  "Updated_At": "string"                        # Timestamp actualización del documento 
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
  "rate_and_availability_id": "ObjectID()", 
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