
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

"argumentos de palabra clave"

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

print(arrival_time(hours=0))

"Combinación de argumentos y argumentos de palabra clave"

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Moon"))
print(arrival_time("Orbit", hours=0.13))

"Argumentos de variable"

def variable_length(*args):
    print(args)

variable_length()
()
variable_length("one", "two")
('one', 'two')
variable_length(None)
(None,)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print(sequence_time(4, 14, 18))

"Argumentos de palabra clave variable"

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

"Ejemplo"

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

"Ejercicio"

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=50, external=100, emergency=60)
