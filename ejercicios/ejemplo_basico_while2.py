print("Ingrese un numero negativo para terminar")

numero = int(input("Ingresar un numero: "))
numero_maximo = -1

while numero >= 0:
    if numero > numero_maximo:
        numero_maximo = numero
    numero = int(input("Ingresar un numero: "))
print("El numero maximo es:", numero_maximo)