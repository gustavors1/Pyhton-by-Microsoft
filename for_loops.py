" for loops "

""" l bucle for es una instrucción con cinco partes importantes:

La palabra for, seguida de un espacio.
El nombre de la variable que quiere crear para cada valor de la secuencia (number).
La palabra in, entre espacios.
El nombre de la lista (countdown, en el ejemplo anterior) u objeto iterable que quiere recorrer en bucle, seguido de dos puntos (:).
El código que quiere ejecutar para cada elemento del objeto iterable, separado por espacios en blanco anidados."""

""" countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀") """

"Ejercicio"

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input("Enter a new planet or done if done ")

for planet in planets:
    print(planet)


