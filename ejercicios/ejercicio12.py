'''
1. Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas,
 minutos y segundos.
2. Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos
 expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas,
  minutos y segundos.
'''

def conversor(hora : int, minuto : int, segundo : int) -> int:
    segundos = hora * 60 * 60 + minuto * 60 + segundo
    return segundos

def inputs() -> int:
    hora = int(input("Ingrese las horas: "))
    minuto = int(input("Ingrese los minutos: "))
    segundo = int(input("Ingrese los segundos: "))
    return conversor(hora, minuto, segundo)
    
def main() -> None:
    intervalo_1 = inputs()
    intervalo2 = inputs()

    suma = intervalo_1 + intervalo2
    print("\n\nResultado: \n")

    horas = suma/60/60
    print(f"Horas: {int(horas)}.")

    minutos = (horas % 1) * 60
    print(f"Minutos: {int(minutos)}.")

    segundos = (minutos % 1) * 60
    print(f"Segundos: {int(segundos)}.")

    print(f"La suma de los intervalos da como resultado: {int(horas)}:{int(minutos)}:{int(segundos)}.")

main()