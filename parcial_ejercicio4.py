"""
4) Crear una función que reciba un string que contiene números y los ordene de menor a mayor; pero teniendo las
siguientes consideraciones:

 Si hay números repetidos (solo van a poder estar repetidos 1 vez):


o Los números repetidos pares irán copiados en otra lista. (Además de estar en la ordenada)
o Los números repetidos impares deberán ir en la misma lista que los anteriores (además de estar en la
ordenada), pero escritos como el número menor y par más próximo que tengan. Ejemplo: Si es 5, su
par menor más cercano es 4. 

La función debe devolver un string con los números ordenados, separados por comas y además los repetidos
ordenados al final.

Ejemplo: cadena = '275217'
>>>1, 2, 2, 5, 7, 7, 2, 6 
"""

cadena_de_numeros = '275217' 

def pares_ordenados(cadena_de_numeros: str) -> str:
    cadena_de_numeros = sorted(cadena_de_numeros)

    lista_de_numeros_ordenados = cadena_de_numeros
    lista_de_repetidos = []
    
    for i in cadena_de_numeros:
        contador = 0
        for j in cadena_de_numeros:
            if i == j:
                contador += 1
        if contador > 1:
            lista_de_repetidos.append(i)

    for i in range(0,len(lista_de_repetidos), 2):
        lista_de_repetidos.remove(lista_de_repetidos[i])
    
    for i in range(len(lista_de_repetidos)):
        lista_de_repetidos[i] = int(lista_de_repetidos[i])
        if lista_de_repetidos[i] % 2 != 0:
            lista_de_repetidos[i] = lista_de_repetidos[i] - 1
        lista_de_repetidos[i] = str(lista_de_repetidos[i])

    lista_de_numeros_ordenados.extend(lista_de_repetidos)
    numeros_ordenados = ",".join(lista_de_numeros_ordenados)

    return numeros_ordenados

def main() -> None:
    pares_ordenados(cadena_de_numeros)

main()