'''
Realizar un programa que permita jugar a adivinar un número entero.
El participante A elige el número a adivinar y luego hace jugar al participante B,
el cual deberá intentar adivinarlo arriesgando números.
El programa debe guiar al participante B indicándole, en cada intento,
si el número arriesgado es mayor o menor al definido por el participante A.
El juego debe concluir al acertar el número o superar los 20 intentos.
Al acertar el número debe indicar la cantidad de intentos que fueron utilizados para lograrlo.
En caso de no haber conseguido el objetivo, debe indicarle que ha superado los 20 intentos.
'''
contador = 1

print("Turno del participante A")
numero = int(input("Ingresar numero para que adivine el participante B: "))

print("\nTurno del participante B")
intento = int(input("Ingresar un numero para adivinar: "))

while intento != numero and contador < 20:
    if intento > numero:
        print("El numero ingresado es mayor al numero buscado")

    elif intento < numero:
        print("El numero ingresado es menor al numero buscado")

    contador += 1
    intento = int(input("Ingresar un numero para adivinar: "))

if numero == intento:
    print("Acertaste en,", contador, "intentos!")

else:
    print("Perdiste malo")