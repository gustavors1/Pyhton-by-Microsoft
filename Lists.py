"Listas"

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

"Modificar a través de un índice"

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

"Longitud de la lista len()"

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

"Agregar valores .append"

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

"Eliminar valores .pop()"

planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

"Índices negativos"

# un índice de -1 devuelve el último elemento de una lista. Un índice de -2 devuelve el penúltimo.

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

"Búsqueda de valor a través de index"

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index +1 , "planet from the sun")

mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")

"Alamencanmiento de números en listas"

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650 # in kilograms, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")

""" Uso de min() y max()
La función max() devuelve el número más grande y min() devuelve el más pequeño."""

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

""" Segmentación de listas

Puede recuperar una parte de una lista mediante una segmentación. 
Una segmentación usa corchetes, pero en lugar de un solo elemento, 
tiene los índices inicial y final. Cuando se usa una segmentación, 
se crea una lista que comienza en el índice inicial 
y termina antes del índice final (y no lo incluye)."""

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

planets_after_earth = planets[3:] #Dejarlo vació significa ir hasta el final
print(planets_after_earth)

"Combinación de listas"

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

"Ordenación con .sort()"

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

"Ordenación inversa .sort(reverse=True)"

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

"Ejercicio"

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

user_planet = input("Please enter the name of the planet (with a capital letter to start)")
planet_index = planets.index(user_planet)
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])

print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])
