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
  "room_type": ObjectId(),               # room_type_id
  "rate_plan": ObjectId(),               # rate_plan_id

  "createdBy": ObjectId(),               # user_id
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
  "property_id": ObjectId(),                    # Id de la propiedad
  "user_id": ObjectId(),
  "role": "string",                           # rol que se le asigna al usuario
  "createAt": "string",
  "updateAt": "string"
}
```
