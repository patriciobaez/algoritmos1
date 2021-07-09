def ordenar_cadena(numeros: str) -> None:

    numeros_repetidos = list()

    numeros = sorted(numeros)

    numeros_unicos = set(numeros)

    for numero in numeros_unicos:

        contador = numeros.count(numero)

        if contador > 1:

            numero_formateado = int(numero)

            if numero_formateado % 2 == 1:
                numeros_repetidos.append(numero_formateado - 1)

            else:
                numeros_repetidos.append(numero_formateado)

    numeros_repetidos.sort()

    numeros_formateados = [int(i) for i in numeros]

    numeros_formateados += numeros_repetidos

    print(numeros_formateados)


def main() -> None:

    ordenar_cadena('275217')


main()