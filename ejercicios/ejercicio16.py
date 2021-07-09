"""
5) Escribir un programa que primero solicite una palabra al usuario y luego le permita al usuario ingresar 5 palabras. El sistema deberá
 calcular cuántas y cuáles palabras de las 5 ingresadas pueden escribirse exactamente con las letras de la palabra ingresada al principio
  (utilizando todas las letras y sin repetir ninguna).
Ej: Palabra inicial: CASO
5 palabras: MAMA, CLASE, SACO, COSA, PEPE
EL sistema deberá devolver 2 palabras (SACO y COSA).
"""

def palabras_coincidentes():
    palabra_parametro = palabra_principal()
    lista_letras_parametro = []
    for i in palabra_parametro:
        lista_letras_parametro.append(i)

    lista_letras_parametro.sort()
    lista_de_palabras = input("Ingrese 5 palabras separadas por 1 espacio: ").split(" ")
    lista_de_palabras.sort()
    contador = 0
    palabras_que_coinciden = []
    lista_de_letras = []
    for palabra in lista_de_palabras:
        letras = []
        for letra in palabra:
            letras.append(letra)
        letras.sort()
        lista_de_letras.append(letras)
    num_palabra = -1
    for i in lista_de_letras:
        num_palabra += 1
        if i == lista_letras_parametro:
            palabras_que_coinciden.append(lista_de_palabras[num_palabra])
            contador += 1
    
    return palabras_que_coinciden, contador
 
def palabra_principal():
    return input("Ingrese una palabra: ")

def main():
    info = palabras_coincidentes()
    print(f"Pueden escribirse exactamente con las letras de la palabra ingresada {info[1]} palabras de las 5 ingrresadas.\nSon las palabras: {info[0]}")

main()