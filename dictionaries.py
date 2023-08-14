"Dictionaries"

"""Los diccionarios de Python permiten trabajar con conjuntos de datos relacionados. 
Un diccionario es una colección de pares clave-valor"""

# Python usa llaves ({ }) y dos puntos (:) para indicar un diccionario.

""" Puede crear un diccionario vacío y agregar valores más adelante, 
o bien rellenarlo en el momento de la creación."""

planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet.get('name'))

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# Diferencias entre get y []

"""wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError """

"Update para modificar valores dentro de un objeto del diccionario"

planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

# No output: name is now set to Makemake.

planet['name'] = 'Jupiter'
planet['moons'] = 79

# No output: name is now set to Makemake.