
#archivo = open("cadenas.txt", "r")

with open("cadenas.txt", "r") as archivo:
    for linea in archivo:
        print(linea[0])