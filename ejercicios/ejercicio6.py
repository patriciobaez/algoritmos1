numero = float(input("Ingrese un numero: "))
numero_maximo = numero
numero_minimo = numero
suma = numero

for i in range(9):
    numero = float(input("Ingrese un numero: "))
    suma = suma + numero
    if numero > numero_maximo:
        numero_maximo = numero
    if numero < numero_minimo:
        numero_minimo = numero

print("El promedio de los numeros ingresados es:", suma/10)
print("El numero maximo es:", numero_maximo)
print("El numero minimo es:", numero_minimo)