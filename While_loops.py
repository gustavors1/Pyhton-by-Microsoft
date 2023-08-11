" Bucle While "

""" Buscar otra línea en un archivo.
Comprobar si se ha establecido alguna marca.
Comprobar si un usuario ha terminado de introducir valores.
Comprobar si algo más ha cambiado para indicar que el código puede dejar de realizar la operación. """

"""while <condition>:
    # code here

user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')"""

""" Create the variable for user input
user_input = ''
 Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done ') """

"ejercicio"

new_planets = ""
planets = []

while new_planets != "done":
    new_planets = input("Enter a new planet name or 'done' to finish: ")
    if new_planets != "done":
        planets.append(new_planets)

print("The list of planets is:")
for planet in planets:
    print(planet)


