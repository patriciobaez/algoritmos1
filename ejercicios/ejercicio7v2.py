'''
Crear un programa que permita ingresar N números enteros positivos y luego mostrar por pantalla
la suma total de esos números y el promedio.
Una vez hecho, crear otro programa que utilice lo anterior pero que permita hacerlo 3 veces.
Es decir, calcular 3 sumas totales y 3 promedios, una vez hecho eso, verificar en que repetición se obtuvo el mejor promedio
Ejemplo:
Primera iteración: Suma total = 50, Promedio = 10.
Segunda iteración: Suma total = 50, Promedio = 5.
Tercera iteración: Suma total = 100, Promedio = 4
El mayor promedio se obtuvo en la primera iteración.
'''



promedio_maximo = 0
for i in range(3):

    n = int(input("Cuantas notas va a ingresar? "))
    suma = 0
    for i in range(n):
        nota = int(input("Ingrese la nota: "))
        suma += nota
    print("La suma da:", suma)

    promedio = suma/n
    print("El promedio da:", promedio)
    if promedio > promedio_maximo:
        promedio_maximo = promedio


print("El promedio mas alto es:", promedio_maximo)