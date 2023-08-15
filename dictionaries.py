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

"Adición y eliminación de claves"

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

"Tipos de data complejos"

"""Los diccionarios pueden almacenar cualquier tipo de valor, 
incluidos otros diccionarios. Esto le permite modelar datos complejos 
según sea necesario."""

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

"Ejercicio"

planet = {
    'name' : "Mars",
    'moons' : 2
}

print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet.update({
    'circumference (km)': {
        'polar': 6752,
        'equatorial': 6792
    }
})

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

"Recuperación de todas las claves y valores"

""" El método keys() devuelve un objeto de lista que contiene todas las claves. 
Puede usar este método para iterar por todos los elementos del diccionario. """

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

""" Determinación de la existencia de una clave en un diccionario """

""" Al actualizar un valor en un diccionario, 
Python sobrescribirá el valor existente o creará uno, si la clave no existe. 
Si quiere agregar a un valor en lugar de sobrescribirlo, 
puede comprobar si la clave existe mediante in."""

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1
