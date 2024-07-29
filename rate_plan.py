### Rate Plan Model ###

# Rate plan es un conjunto de condiciones que van a modificar el precio base de un tipo de cuarto.

{
  "rate_plan_id": "string",
  "type": "enum",                            # Standard, LOS (length of stay), NOG (number of guests)
  "plan_name": "string",
  "min_los": "number",
  "min_nos": "number",
  "breakfast": "boolean",
  "amount_of_discount": "number",

}

# Ejemplo:
# Una vez el usuario creo los tipos de cuartos, crea los planes de tarifas.
# El siguiente ejemplo muestra un plan de tarifas standard para un cuarto compartido.
# Este ejemplo podria ser un rate_plan por defecto que se cree automaticamente y se asocie a cada uno de los productos.

{
  "rate_plan_id": "ratePlan001",
  "type": "standard",
  "plan_name": "plan standard por defecto",
  "min_los": 1,
  "min_nos": 1,
  "breakfast": "false",
  "breakfast_price": 0,
  "amount_of_discount": 0
}

# Ahora supongamos que el usuario quiere agregar dos planes de tarifas para los cuartos compartidos.
# Plan 1: Descuento del 10% a los pasajeros que reserven un minimo de 7 noches.
# Plan 2: Descuento del 15% para grupos de pasajeros de 4 o mas personas.

{
  "rate_plan_id": "ratePlan002",
  "type": "los",
  "plan_name": "Cuartos compartidos con estadia minima de una semana",
  "min_los": 7,
  "min_nos": 1,
  "breakfast": 0,
  "breakfast_price": 0,
  "amount_of_discount": 0.1
}

{
  "rate_plan_id": "ratePlan003",
  "type": "nos",
  "plan_name": "Cuartos compartidos para grupos de 4 o mas",
  "min_los": 1,
  "min_nos": 4,
  "breakfast": 0,
  "breakfast_price": 0,
  "amount_of_discount": 0.15
}

# Asi sucesivamente el usuario podria crear todos los planes que quiera que despues ira asociando a los 
# productos que quiera crear. (booking permite hasta 100 planes en total).
# Podemos observar que luego, cada producto podra contar con uno o mas planes asociados.
# Tambien podemos observar que si el usuario no crea ningun plan el plan por defecto se le 
# atribuira a cada uno de los productos que el usuario cree, pero si el usuario quiere modificar la 
# duración minima de la estadia (poner minimo 2 noches), o poner desayuno, pude modificar esos campos
# en el plan generico por defecto.

