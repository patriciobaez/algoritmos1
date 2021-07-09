"""
3) Se pide realizar una función que devuelva el número enteros más pequeño de un listado ingresado por el usuario,
 tal que la suma de los N números exceda un valor pasado por parámetro en la función.
"""
valor_que_debe_exeder = int(input("Ingrese el valor que debe exeder: "))

def numero_mas_pequenio(valor_que_debe_exeder):
    suma_de_numeros = 0
    lista_de_numeros = []
    while valor_que_debe_exeder >= suma_de_numeros:
        numero = int(input("Ingrese un numero: "))
        suma_de_numeros += numero
        lista_de_numeros.append(numero)
    menor_numero = min(lista_de_numeros)
     
    return menor_numero

menor_numero = numero_mas_pequenio(valor_que_debe_exeder)
print(menor_numero)