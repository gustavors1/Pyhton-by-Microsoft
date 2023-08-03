""" Strings """

"Agregando cadenas a través de Variables"

fact = "The Moon has no atmosphere."
two_facts = fact + " No sound can be heard on the Moon."
print(two_facts)

" Se pueden usar comillas simples, dobles o triples para las cadenas"

" Texto Multilinea. Lo usamos para separar en varias lineas el texto "

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

" Métodos de Cadena"

"el método .title() devuelve la cadena en mayúsculas y se puede usar directamente con una cadena"

print("temperatures and facts about the moon".title())

" El mismo comportamiento y utilización se produce en una variable:"

heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)

" División de una cadena "

" Sin argumentos, el método separará la cadena en cada espacio. "
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures .split('\n')
print(temperatures_list)

" Búsqueda de una cadena "

print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

" Posición de una palabra específica "

"El método .find() devuelve -1 cuando no se encuentra la palabra, o bien devuelve el índice (el número que representa la posición en la cadena)"
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

""" Otra manera de buscar contenido consiste en usar el método .count(), 
que devuelve el número total de repeticiones de una palabra determinada en una cadena: """

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, 
                    while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

" Convertir cadena en minúsculas y mayúsculas. "

print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())

" Comprobación del contenido "

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

" Texto irregular "

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

" N° Negativos "

print("-60".startswith('-'))

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

"Transformar texto"

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
"Salida: False"

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())
"Salida: True"

"Agrupar elementos"

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))