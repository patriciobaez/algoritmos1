cadena = "Qué lindo día que hace hoy"

def contar_palabras(cadena: str) -> dict:
    diccionario_de_palabras = dict()
    cadena = cadena.lower()
    for i in cadena:
        if i == "é": 
            i = "e"
        elif i == "á":
            i="a"
        elif i == "í":
            i="i"
        elif i == "ó":
            i="o"
        elif i == "ú":
            i="u"

    cadena = cadena.split()

    for i in cadena:
        if i not in diccionario_de_palabras.keys():
            diccionario_de_palabras[i] = 1
        else:
            diccionario_de_palabras[i] += 1

    return print(diccionario_de_palabras)
contar_palabras(cadena)