"Seguimientos"

"""def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()"""

"""Los seguimientos casi siempre incluyen la información siguiente:

Todas las rutas de acceso de archivo implicadas, para cada llamada a cada función.
Los números de línea asociados a cada ruta de acceso de archivo.
Los nombres de las funciones, métodos o clases implicados en la generación de una excepción.
El nombre de la excepción que se ha producido.
"""

"Prueba y excepción de los bloques"

try:
     open('config.txt')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")