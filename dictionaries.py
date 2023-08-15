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

"Recuperación de todos los valores"

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')

"Ejercicio"

planet_moons = {
    'mercury' : 0,
    'venus' : 0,
    'earth' : 1,
    'mars' : 2,
    'jupiter' : 79,
    'saturn' : 82,
    'uranus' : 27,
    'neptune' : 14,
    'pluto' : 5,
    'haumea' : 2,
    'makemake' : 1,
    'eris' : 1
}

"""recupere una lista con el número de lunas y guárdela en una variable llamada lunas. 
Luego obtenga el número total de planetas y almacene ese valor 
en una variable llamada total_planets."""

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')
