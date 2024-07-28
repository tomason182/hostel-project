### USER MODEL ###

# @ Collection User
# @ many-to-many User > Property

{
  "user_id": "string",              # Identificador para el usuario
  "username": "string",             # usuario, posiblemente email (tambien unico)
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

# Notas de User Model: 
# Es el primer paso que un usuario realiza en la app. 
# Una vez registrado,  el usuario puede crear una propiedad ("Property model")
# Una vez creada la propiedad el usuario puede crear otros usuarios con otros roles que administren la propiedad.
# Relacion many-to-many: Una propiedad puede tener varios usuarios y un usuario puede tener varias propiedades


### ACCESS CONTROL MODEL ###

# @ Coleccion Access_control
# @ one-to-many User > Access_control
# @ one-to-one Property > Access_control

{
  "access_id": "string",
  "property_id": "string",                    # Id de la propiedad. Una propiedad tiene un solo un access_control y un access_control tiene sola una propiedad. 
  "user_id": "string",                        # Un access_control se vincula con varios usuarios, un usuario tiene solo un access_control.
  "role": "string",                           # Es el rol que se le asigna al usuario. Lo asigna el creador de la propiedad
  "createAt": "string",
  "updateAt": "string"
}

# Notas sobre Access Control.
# Permite al administrador de una propiedad crear usuarios con otros roles de menor gerarquia.
# Se vincula con la coleccion User y Property.
