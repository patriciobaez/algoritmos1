'''Se pide hacer un programa que ingrese 8 juegos de n valores positivos cada uno.
Considerar un condiciòn de corte para el n.
Calculando el promedio de cada juego,
 el máximo de cada juego y 
 el mínimo de todos los juegos'''
 
CANT_JUEGOS = 8

minimo_global = 0

for i in range(CANT_JUEGOS):
    suma = 0
    contador = 0
    numero_maximo = 0
    numero = int(input("\nIngrese un numero(ingrese 0 para terminar): "))
    if i == 0:
        minimo_global = numero
    
    while numero != 0:
        suma += numero
        contador += 1
        promedio = suma/contador

        if numero > numero_maximo:
            numero_maximo = numero
        if numero < minimo_global:
            minimo_global = numero

        numero = int(input("\nIngrese un numero(ingrese 0 para terminar): "))
   
    print(f"\nEl promedio es {promedio}.")
    print(f"\nEl numero maximo es: {numero_maximo}.")

print(f"\nEl numero minimo de los 8 juegos es {minimo_global}.")