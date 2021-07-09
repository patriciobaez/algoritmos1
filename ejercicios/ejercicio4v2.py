"""ADIVINANZAS"""

print("Turno de Usuario1")

PALABRA = input("Ingrese una palabra para adivinar: ")
NUM_LETRAS = len(PALABRA)

print("\n\n\nTurno de Usiario2")
ADIVINANZA_1 = int(input("Adivina cuantas letras tiene la palabra: "))
ADIVINANZA_2 = int(input("Adivina cuantas letras tiene la palabra: "))
ADIVINANZA_3 = int(input("Adivina cuantas letras tiene la palabra: "))

contador = 0

if NUM_LETRAS == ADIVINANZA_1:
    contador = contador + 1
if NUM_LETRAS == ADIVINANZA_2:
    contador = contador + 1
if NUM_LETRAS == ADIVINANZA_3:
    contador = contador + 1


if contador == 0:
    print("Vuelva prontos; esta vez no se pudo")
elif contador == 1:
    print("Muy Bien!")
else:
    print("AH, PERO SOS BUENÍSIMOOOOO")