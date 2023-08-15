
def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()
output = rocket_parts()
output is None

def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output

any([True, False, False])
any([False, False, False])

"Uso de argumentos de función en Pytho"

"Exigencia de un argumento"

#Las entradas obligatorias se denominan argumentos para la función.

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
print(distance_from_earth("Moon"))
print(distance_from_earth("Saturn"))

"Varios argumentos necesarios"

"""Vamos a crear una función que pueda calcular cuántos días se tardan 
en llegar a un destino, dadas la distancia y una velocidad constante:"""

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))

"Funciones como argumentos"

total_days = days_to_complete(238855, 75)
print(round(total_days))

"Ejercicio"

def generate_report(main_tank, external_tank, hydrogen_tank):
     output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
print(generate_report(100, 200, 300))