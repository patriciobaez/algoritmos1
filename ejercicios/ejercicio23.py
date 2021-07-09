"""
5) Números escalonados: Un número es escalonado, si sus dígitos están en orden estrictamente creciente.
Por ejemplo, 359 es escalonado, 34 también, pero 5674 no es, y tampoco 5667.
Se recibe un número entero por parámetro N > 10 (lo cual se debe validar).
La salida debe decir si es un número escalonado o no lo es y a continuación indicar la cantidad de dígitos cuya secuencia
fue escalonada.
Datos de entrada:
Se recibe un parámetro con el número entero N.
Datos de salida:
El programa debe imprimir por pantalla en una línea, conteniendo un único número: la cantidad de números
escalonados que hay entre 10 y N, inclusive.
Ejemplo1: Entrada: 359 - Salida: “Es escalonado”, 3
Ejemplo2: Entrada: 24893471 - Salida: “No es escalonada”, 4
"""
def numeros_escalonados(numero_entero: int) -> None:
    numero_entero = str(numero_entero)
    cantidad_de_numero = len(numero_entero)
    secuencia_escalonada = 0
    for i in range(cantidad_de_numero):
        if numero_entero[i] < numero_entero[i+1]:
            secuencia_escalonada += 1

    if cantidad_de_numero == secuencia_escalonada:
        print(f"Es escalonado: {cantidad_de_numero}")
    else: 
        print(f"No es escalonada: {secuencia_escalonada}")
    print(secuencia_escalonada)

def main() -> None:
    repetir = True
    while repetir:
        numero_entero = input("Ingrese un numero entero mayor a 10: ")
        if numero_entero.isnumeric():
            numero_entero = int(numero_entero)
            if numero_entero > 10:
                repetir = False

    numeros_escalonados(numero_entero)

main()