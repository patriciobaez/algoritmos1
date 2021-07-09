'''
Crear un programa que permita ingresar N números enteros positivos y luego mostrar por pantalla
la suma total de esos números y el promedio.

Una vez hecho, crear otro programa que utilice lo anterior pero que permita hacerlo 3 veces.
Es deccir, calcular 3 sumas totales y 3 promedios, una vez heho eso, verificar en que repetición se obtuvo el mejor promedio
Ejemplo:
Primera iteración: Suma total = 50, Promedio = 10.
Segunda iteración: Suma total = 50, Promedio = 5.
Tercera iteración: Suma total = 100, Promedio = 4
El mayor promedio se obtuvo en la primera iteración.
'''

mayor_promedio = 0
mayor_iteracion = 0

for i in range(1,4)
    suma = 0
    contador = 0
    numero = int(input("Ingrese un numero entero positivo: "))

    if numero <= 0:
        while numero <= 0:
            print("Numero no positivo.")
            numero = int(input("Ingrese un numero entero positivo: "))

    while numero > 0:
        contador += 1
        suma += numero
        numero = int(input("Ingrese un numero entero positivo(Ingrese 0 o un numero negativo para terminar): "))

    promedio = suma/contador
    if promedio > mayor_promedio:
        mayor_promedio = promedio
        mayor_iteracion = i
        
    print(f"La suma de los numeros da {suma}.")
    print(f"El primedio de los numeros da {promedio}.")
print(f"El mayor promedio lo obtuvo la iteracion {mayor_iteracion} y fue de {mayor_promedio}.")