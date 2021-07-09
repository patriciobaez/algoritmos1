"""
Un número perfecto es aquel número que es igual a la suma de todos
sus divisores positivos excepto el mismo.
El primer número perfecto es 6, ya que 1+2+3=6.
Escribir un programa que muestre todos los números perfectos
hasta un número dado por el usuario.
Ayuda:
Entre 0-10.000 hay solo 3 números perfectos.
"""

n = int(input("Ingrese un número: "))
for dividendo in range(1, n+1):
    suma_divisores = 0

    for divisor in range(1, dividendo):
        if dividendo % divisor == 0:
            suma_divisores += divisor
            
    if suma_divisores == dividendo:
        print(f"{dividendo} es número perfecto")