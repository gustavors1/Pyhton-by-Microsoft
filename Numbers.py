"Numbers"

from math import ceil, floor

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

"Valor absoluto"
print(39 - 16)
print(16 - 39)

"abs para convertir negativo en absoluto"
print(abs(39 - 16))
print(abs(16 - 39))

print(round(14.5)) #Redondeo

"""Se puede redondear siempre hacia arriba al número entero más cercano si usa ceil,
o hacia abajo si usa floor."""

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

"Ejercicio"

first_planet_input = input('Enter the distance from the sun for the first planet in KM')
second_planet_input = input('Enter the distance from the sun for the second planet in KM')

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = second_planet - first_planet
print(abs(distance_km))