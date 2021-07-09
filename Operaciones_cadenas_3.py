### Escribir una función que dada una cadena de caracteres, devuelva:

### a) La primera letra de cada palabra. Ejemplo:
### >>> primeras_letras('Universal Serial Bus')
### 'USB'

### b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Ejemplo:
### >>> primera_letra_mayus('república argentina')
### 'República Argentina'

### c) Las palabras que comiencen con la letra ‘A’ (en mayúsculas o minúsculas). Ejemplo:
### >>> comienzan_con_a('Antes de ayer')
### 'Antes ayer'


def primeras_letras(cadena: str) -> str:
    
    longitud = len(cadena)
    es_caracter_inicial = True
    cadena_primeras_letras = ""

    for i in range(longitud):
        caracter = cadena[i]
        
        ### Si se está leyendo el caracter inicial de una palabra, y no es un espacio
        ### incluirlo a la cadena de primeras letras
        if (caracter != " ") and (es_caracter_inicial):
            cadena_primeras_letras += caracter
            es_caracter_inicial = False
        ### Si es un espacio, volver verdadera la variable de caracter inicial
        elif caracter == " ":
            es_caracter_inicial = True

    return cadena_primeras_letras


def primera_letra_mayus(cadena: str) -> str:

    longitud = len(cadena)
    es_caracter_inicial = True
    cadena_primeras_mayus = ""

    for i in range(longitud):
        caracter = cadena[i]

        ### Si el primer caracter de una palabra no es espacio, se incluye su mayuscula en la 
        ### cadena de primeras mayusculas
        if (caracter != " ") and (es_caracter_inicial):
            cadena_primeras_mayus += caracter.upper()
            es_caracter_inicial = False
        ### Si el primer caracter no es un espacio y no es el caracter inicial, incluirlo en
        ### la cadena de primeras mayusculas
        elif (caracter != " ") and (not es_caracter_inicial):
            cadena_primeras_mayus += caracter
        ### Si el caracter es espacio, volver verdadera la variable de caracter inicial
        elif (caracter == " "):
            es_caracter_inicial = True
            cadena_primeras_mayus += caracter

    return cadena_primeras_mayus


def comienzan_con_a(cadena: str) -> str:

    longitud = len(cadena)
    es_caracter_inicial = True
    empieza_con_a = False
    cadena_palabras_con_a = ""

    for i in range(longitud):
        caracter = cadena[i]

        ### Si el caracter inicial es A o a, incluirlo en la cadena de palabras que empiezan con a
        if (es_caracter_inicial) and ((caracter == "A") or (caracter == "a")):
            cadena_palabras_con_a += caracter
            es_caracter_inicial = False
            empieza_con_a = True
        ### Si el caracter inicial de una palabra no es A o a, no se toma ninguna letra de la palabra
        elif (es_caracter_inicial) and not ((caracter == "A") or (caracter == "a")):
            es_caracter_inicial = False
        ### Si la palabra empieza con a, cada una de sus letras se incluye en la cadena
        elif (empieza_con_a) and (caracter != " "):
            cadena_palabras_con_a += caracter
        ### Si el caracter es espacio, vuelvo verdadera la variable de caracter inicial
        elif caracter == " ":
            es_caracter_inicial = True
            if not empieza_con_a:
                cadena_palabras_con_a += caracter
            empieza_con_a = False
    
    return cadena_palabras_con_a

cadena1 = 'Universal Serial Bus'
cadena2 = 'república argentina'
cadena3 = 'Antes de ayer'

def main() -> None:
    print(primeras_letras(cadena1))
    print(primera_letra_mayus(cadena2))
    print(comienzan_con_a(cadena3))

main()