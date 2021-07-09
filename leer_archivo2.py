"""
Se les proporcionará un archivo numeros.txt, donde cada línea contiene un número de forma aleatoria. Lo que 
les pedimos es leer el archivo y calcular la suma de todos esos números y mediante un assert verificar que 
la suma sea igual a 2.613.600
"""

with open("numeros.txt", "r") as archivo:
    suma = 0
    for linea in archivo:
        suma += int(linea)

assert(suma == 2613600)