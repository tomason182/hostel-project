# hostel-project

Diseño inicial de la estructura de la base de datos.
Es IMPORTANTE seguir el orden detallado debajo al momento de leer los archivos, para entender mejor la estructura

1. User Model: Almacena cada uno de los usuarios que se registran en la app
2. Property Model: El usuario registrado crea una propiedad.
3. Access_control Model (Ver dentro de User): El usuario crea otros usuarios con distintos roles
4. Room_types: Tipos de cuarto. Se vincula con Property.
5. Rate_plan: NO DEFINIDO TODAVIA
6. rate_and_availiability: Almacena las tarifas y disponibilidad (Hay que corregir)
7. Guest: Almacena los pasajeros
8. reservation: Destinada a los datos referidos a la reservas
