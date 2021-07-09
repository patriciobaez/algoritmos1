"""ADIVINANZAS"""

print("Turno de Usuario1")

PALABRA = input("Ingrese una palabra para adivinar: ")
NUM_LETRAS = len(PALABRA)

print("\n\n\nTurno de Usiario2")
ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))

if NUM_LETRAS == ADIVINANZA:
    print("\nMuy bien!\n")
    print("Turno de Usuario1")

    PALABRA = input("Ingrese una palabra para adivinar: ")
    NUM_LETRAS = len(PALABRA)

    print("Turno de Usiario2")
    ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))

    if NUM_LETRAS == ADIVINANZA:
        print("AH, PERO SOS BUENÍSIMOOOOO")
    else:
        print("Intenta devuelta!")
        ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
        if NUM_LETRAS == ADIVINANZA:
            print("AH, PERO SOS BUENÍSIMOOOOO")
        else:
            print("Ultimo intento!")
            ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
            if NUM_LETRAS == ADIVINANZA:
                print("AH, PERO SOS BUENÍSIMOOOOO")
            else:
                print("Vuelva prontos; esta vez no se pudo")

else:
    print("Intenta devuelta!")
    ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
    if NUM_LETRAS == ADIVINANZA:
        print("\nMuy bien!\n")
        print("Turno de Usuario1")

        PALABRA = input("Ingrese una palabra para adivinar: ")
        NUM_LETRAS = len(PALABRA)

        print("Turno de Usiario2")
        ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))

        if NUM_LETRAS == ADIVINANZA:
            print("AH, PERO SOS BUENÍSIMOOOOO")
        else:
            print("Intenta devuelta!")
            ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
            if NUM_LETRAS == ADIVINANZA:
                print("AH, PERO SOS BUENÍSIMOOOOO")
            else:
                print("Ultimo intento!")
                ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
                if NUM_LETRAS == ADIVINANZA:
                    print("AH, PERO SOS BUENÍSIMOOOOO")
                else:
                    print("Vuelva prontos; esta vez no se pudo")
    else:
        print("Ultimo intento!")
        ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
        if NUM_LETRAS == ADIVINANZA:
            print("\nMuy bien!\n")
            print("Turno de Usuario1")

            PALABRA = input("Ingrese una palabra para adivinar: ")
            NUM_LETRAS = len(PALABRA)

            print("Turno de Usiario2")
            ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))

            if NUM_LETRAS == ADIVINANZA:
                print("AH, PERO SOS BUENÍSIMOOOOO")
            else:
                print("Intenta devuelta!")
                ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
                if NUM_LETRAS == ADIVINANZA:
                    print("AH, PERO SOS BUENÍSIMOOOOO")
                else:
                    print("Ultimo intento!")
                    ADIVINANZA = int(input("Adivina cuantas letras tiene la palabra: "))
                    if NUM_LETRAS == ADIVINANZA:
                        print("AH, PERO SOS BUENÍSIMOOOOO")
                    else:
                        print("Vuelva prontos; esta vez no se pudo")
        else:
            print("Vuelva prontos; esta vez no se pudo")