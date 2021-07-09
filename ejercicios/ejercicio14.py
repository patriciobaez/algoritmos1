'''
Se solicita crear una función en la cual reciba un texto(string) como parámetro,
y que devuelva un diccionario con las palabras como clave y como valor la cantidad de veces que 
se repite dicha palabra, a modo de ejemplo, dado el siguiente texto:
    Auto Casa Avion Auto casa casa
la función deberá devolver el siguiente diccionario:
    {"Auto":2, "Casa":1, "Avion":1, "casa":2}

Una vez se haya implementado la función, se solicita crear otra función que en vez de contar 
cada palabra, cuente cada letra, es decir que del texto anterior debe salir el sig. diccionario:
    {'A': 3, 'u': 2, 't': 2, 'o': 3, 'C': 1, 'a': 6, 's': 3, 'v': 1, 'i': 1, 'n': 1, 'c': 2}
'''

def cantidad_de_palabras(texto: str) -> dict:
    diccionario = {}
    palabras = texto.split(" ")
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return print(diccionario)

cantidad_de_palabras("Auto Casa Avion Auto casa casa")

def cantidad_de_letras(texto: str) -> dict:
    diccionario = {}
    palabras = texto.split(" ")

    for palabra in palabras:
        for letra in palabra:
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1
    return print(diccionario)

cantidad_de_letras("Auto Casa Avion Auto casa casa")