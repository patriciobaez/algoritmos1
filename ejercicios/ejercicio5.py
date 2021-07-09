PALABRA = input("Ingrese una palabra: ")
LETRA = input("Ingrese la letra de desea buscar en la palabra: ")
ESTA_LA_LETRA = False

for caracter in PALABRA:
    if LETRA == caracter:
        ESTA_LA_LETRA = True
        
if ESTA_LA_LETRA == True:
    print("LA ENCONTRÉ")
else:
    print("PSS, NO 'STABA")