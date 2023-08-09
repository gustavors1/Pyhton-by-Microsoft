" Formato de Signo de porcentaje "

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

"Con varios valores"

print("""Both sides of the %s get the same amount of sunlight, 
      but only one side is seen from %s because the %s 
      rotates around its own axis when it orbits %s.""" 
      % ("Moon", "Earth", "Moon", "Earth"))

"""Método .format(, usa llaves ({}) y utiliza la asignación de variables 
para reemplazar textp)"""

mass_percentage = "1/6"
print("""On the Moon, you would weigh about {} 
      of your weight on Earth.""".format(mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} 
      you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

"Argumenos de palabras claves"

mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} 
      you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

"Cadenas f-strings"
# Usar prefijo f

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

print(round(100/6, 1))
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)

" Ejercicio "

name = "Ganymede"
planet = "Mars"
gravity = 1.43

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))