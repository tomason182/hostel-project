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

El primer paso que un USUARIO realiza en la aplicación es el registro. La colección "User" almacena los datos del registro del usuario.
Una vez el USUARIO se ha registrado puede crear propiedades y otros USUARIOS para que gestionen su propiedad. Esta ultimá caracteristica se logra a traves del modelo "Access Control"

```
# @ Collection User
# @ many-to-many User > Property

{
  "user_id": "string",              # Identificador para el usuario
  "username": "string",             # usuario, posiblemente email (único)
  "hashed_password": "string",      # Almacenamos el password hasheado
  "first_name": "string",
  "last_name": "string",
  "contact_details": {              # Información de contacto
    "email": "string",
    "phone_number": "string",
  },
  "role": "string",                 # Role del usuario (ej., admin, receptionist)
  "createAt": "string",
  "updateAt": "string"
}
```
