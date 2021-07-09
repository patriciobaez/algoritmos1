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




for i in range(3):
    
    numero = int(input("Ingrese una nota(Para finalizar el ingreso de notas ingrese ""-1""): "))
    if numero >= 0:
        suma = 0
        contador = 0
        
        while numero >= 0:
            suma += numero
            contador += 1
            numero = int(input("Ingrese una nota(Para finalizar el ingreso de notas ingrese ""-1""): "))

        promedio_maximo = 0
        print("La suma de las notas es:", suma)
        promedio = suma/contador
        print("El promedio de las notas es:", promedio)
        if promedio > promedio_maximo:
            promedio_maximo = promedio

    else:
        print("La nota es negativa comienze devuelta.")

print("El promedio mas alto es:", promedio_maximo)