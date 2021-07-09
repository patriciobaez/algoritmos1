'''
Crear un programa que permita ingresar un número entero positivo(N) y otro número también
entero positivo (M). Luego calcular las tablas de multiplicación desde N a M

Asumir que M siempre va ser mayor a N.
Ejemplo:
Entrada del programa:
N = 2
M = 10
Salida del programa:
2 x 2 = 4
2 x 3 = 6
  .
  .
  .
2 x 10 = 20
'''

numero_n = int(input("Ingrese un numero: "))
numero_m = int(input("Ingrese un numero: "))

while numero_n <= 0 or numero_m <= 0:
    print("Ingrese los numero nuevamente: ")
    numero_n = int(input("Ingrese un numero: "))
    numero_m = int(input("Ingrese un numero: "))

numero = 0

for i in range(1,numero_m + 1):
    print(f"{numero_n} X {i} = {numero_n*i}")

