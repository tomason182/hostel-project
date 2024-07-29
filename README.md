# hostel-project

Diseño inicial de la estructura de la base de datos.

El siguiente documento tiene como objetivo determinar la estructura y funcionamiento basico del CRM para hostels.

Tabla de contenidos

1. User Model
2. Property Model
3. Access_control Model
4. Room_types
5. Rate_plan
6. Products
7. rate_and_availability
8. Guest
9. reservation

---

User Model

El primer paso que un USUARIO realiza en la aplicación es el registro.
La colección "User" almacena los datos del registro del usuario.
Una vez el USUARIO se ha registrado, puede crear propiedades y otros USUARIOS para que gestionen su propiedad. Esta ultimá caracteristica se logra a traves del modelo "Access Control".
Un USUARIO puede tener muchas PROPIEDADES y una PROPIEDAD varios USUARIOS.

```
# @ Collection User
# @ many-to-many:  User > Property

{
  "user_id": ObjectId(),            # Identificador para el usuario
  "username": "string",             # usuario, posiblemente email (único)
  "hashed_password": "string",      # Almacenamos el password hasheado
  "first_name": "string",
  "last_name": "string",
  "contact_details": {              # Información de contacto
    "email": "string",
    "phone_number": "string",
  },
  "createAt": "string",
  "updateAt": "string"
}
```

Property Model

Una vez el USUARIO se ha registrado, tiene acceso a agregar una propiedad.
La colección Property, almacena datos generales de la propiedad. Esta colección se vincula con las colecciónes "room_type" y "rate_plan" respectivamente.
Una propiedad puede tener uno o varios "room_type". Un "room_type" esta asociado a una sola propiedad. Por lo tanto su relación es One-to-Many.
De la misma forma, una propiedad puede tener uno o varios "rate_plan" y cada "rate_plan" esta asociado a una sola propiedad. Por lo tanto su relación tambien es "One-to-many"

La colección Property guarda un enlace al documento "User" del creador de la propiedad. De esa forma diferenciamos al USUARIO creador de los posibles USUARIOS a los que se le otorgen acceso a la misma.

```
# @ Collection Property
# @ One-to-Many: Property > room_type
# @ One-to-Many: Property > rate_plan
{
  "property_id": ObjectId(),
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

  "createdBy": User[1..*],               # user_id
  "createdAt": "string",                 # timestamp
  "updateAt": "string"                   # timestamp
}
```

Access Control Model

Permite al administrador (creador) de una propiedad, agregrar otros USUARIOS con diferentes roles.
Esta colección se vincula con "User" y "Property"
Una propiedad tiene un solo access control, y un access control una sola propiedad. Por lo tanto su relacion es One-to-One
Un access control tiene varios USUARIOS, un USUARIO podria tener varios access control. Su relacion es One-to-Many.

```
# @ Coleccion Access_control
# @ one-to-many User > Access_control
# @ one-to-one Property > Access_control

{
  "access_id": ObjectId(),
  "property_id": Property[1],                  # Id de la propiedad
  "user_id": User[1..*],
  "role": "string",                           # rol que se le asigna al usuario
  "createAt": "string",
  "updateAt": "string"
}
```

Room Type

Una vez creada la propiedad el usuario agrega los tipos de cuartos que su propiedad mantiene. Los tipos de cuartos se almacenan en la colección "Room Type". Los tipos de cuartos se vinculan exclusivamente con la propiedad.
Una Propiedad puede tener varios tipos de cuartos y un tipo de cuarto una sola propiedad. Su relación es One-to-Many

```
# @ Collection Room-Type
# @ One-to-Many: Property > Room-Type

{
  "room_type_id": ObjectId(),             # Unique Id
  "property_id": Property[1..*],              # Id unico de la propiedad
  "description": "string",
  "type": "string",                       # Tipo de cuarto (ej. Privado, compartido)
  "bathroom": "string",                   # Baño privado o compartido
  "maxOccupancy": "number",               # Ocupación maxima del cuarto
  "inventory": "number"                   # Cantidad de cuartos del mismo tipo
}
```

Rate Plan

Conjunto de condicones que van a modificar el precio base de un tipo de cuarto.
Se manejaran 4 tipos de planes de tarifa:

- Standard pricing (por defecto)
- Derived pricing: Permite modificar el precio en base al porcentaje de ocupación del hospedaje. El usuario establece usuario establece el nivel de ocupación del hostel a partir del cual se reduce o aumenta la tarifa un porcentaje especifico (\*).
  -Occupancy-based pricing (OBP): Permite modificar el precio en base a la cantidad de pasajeros en una reserva. Útil para camas en cuarto compartido o cantidad de habitaciones privadas completas alquiladas en una misma reserva (\*\*).
- Length of stay pricing (LOS): Modifica el precio en base a la duración de la estadia.

```
{
  "rate_plan_id": ObjectId(),
  "property_id": Property[1..*],
  "plan_type": "enum",                            # Standard, LOS, OBP, etc
  "plan_name": "string",
  "conditions: {                                  # Condiciones especificas del plan
    "derived": {
      "occupancy_threshold: "number",             # Nivel de ocupación del hostel
      "price_adjustment": "number"                # Porcentaje de ajuste del precio
    },
    "obp": {
      "passanger_threshold": "number"             # Cantidad de pasajero en una reserva
      "price_adjustment": "number"
    },
    "los": {
      "min_stay_length": "number",
      "price_adjustment": "number"
    },
    "breakfast": {
      "isIncluded": "boolean",
      "price_adjustment": "number"
    }
  }
  "base_rate": "number",
  "currency": "string"
  "valid_from": "string"                          # Fecha inicio del plan (Vigencia)
  "valid_to": "string"                            # Fecha fin del plan
  "day_of_week": ["string"]                       # Dias de semana en los que aplica
  "exception": ["string"]                         # Fechas excluidas del plan
  "createAt": "string"
  "updateAt": "string"
}
```

(\*) Ejemplos: Con un nivel de ocupación superior al 80% el usuario pude establecer que la tarifa se incremente un 5% del precio standard. Por el contrario un nivel de ocupación del 20% la tarifa decrementa un 5%.
(\*\*) Ejemplos: Un reserva individual $10 usd/noche, dos personas $18/noche, cuatro personas $15/noche.

Product

La colección "Product" combina el tipo de cuarto y el plan de tarifas para crear, junto con algunas restricciones, un producto (habitación) único de la propiedad.

```
{
  "product_id": "ObjectID()",
  "property_id": "Property[1]",
  "room_type": "RoomType[1]",
  "rate_plan": "RatePlan[1..*]",
  "name": "string",
  "description": "string",
  "custom_occupancy": "number",                     # La ocupación maxima viene establecida por "room_type", pero el usuario puede modificarla indivdualmente.
}
```
