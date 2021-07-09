from random import randrange
import random
from os import system

#Definimos las probabilidades de cada carta sobre 100%.
probalbilidad_replay = [0, 10]   #10% #otro turno
probalbilidad_layout = [11, 15]  #5%  #las cartas que te quedas se dan mezclan de vuelta
probalbilidad_toti = [16, 20]    #3%  #hace efecto espejo en una columna (x o Y)
probalbilidad_fatality = [21, 24]#3%  #da vuelta las cartas ya encontradas del oponente.

class Carta():
    def __init__(self):
        self.estado = '??'
        self.nombre = ''

def calcular_transpuesta(mat):
  cantidad_filas = len(mat)
  cantidad_columnas = len(mat[0])
  matriz_transpuesta = []

  for i in range(cantidad_columnas):
    matriz_transpuesta.append([mat[0][i]])

    for j in range(cantidad_filas):
      matriz_transpuesta[i].append(mat[j][i])

    matriz_transpuesta[i].pop(0)

  return matriz_transpuesta

def tirar_dado(player, cartas_acum):
    dado = randrange(0, 100)
    if dado >= probalbilidad_replay[0] and dado <= probalbilidad_replay[1]:
        print('Replay')
        cartas_acum[0]+=1
    elif dado >= probalbilidad_layout[0] and dado <= probalbilidad_layout[1]:
        print('Layout')
        cartas_acum[1]+=1
    elif dado >= probalbilidad_toti[0] and dado <= probalbilidad_toti[1]:
        print('Toti')
        cartas_acum[2]+=1
    elif dado >= probalbilidad_fatality[0] and dado <= probalbilidad_fatality[1]:
        print('Fatality')
        cartas_acum[3]+=1
    else:
        print('Nada')
    return cartas_acum

def letra_a_numero(letra):
    letra = letra.lower()
    letras = 'abcdefghijklmn'
    return letras.find(letra)

def verificar_input(lista, tamano):
    if lista == ['']:
        return False
    elif tamano == 4:
        if lista[0].lower() in 'a-b-c-d' and str(lista[1]) in '1-2-3-4':
            return True
        return False
    elif tamano == 8:
        if lista[0].lower() in 'a-b-c-d-e-f-g-h' and str(lista[1]) in '1-2-3-4-5-6-7-8':
            return True
    elif tamano == 12:
        if lista[0].lower() in 'a-b-c-d-e-f-g-h-i-j-k-l-m-n' and str(lista[1]) in '0-1-2-3-4-5-6-7-8-9-10-11-12':
            return True
        return False
    else:
        print('ERROR FATAL')
        exit()

cantidad_de_jugadores = 0
#Con este while evitamos que el usuario elija un parametro fuera de rango.
while cantidad_de_jugadores != '2' and cantidad_de_jugadores != '3' and cantidad_de_jugadores != '4':
    system('cls')
    cantidad_de_jugadores = input('Define la cantidad de jugadores(2-4): ')
cantidad_de_jugadores = int(cantidad_de_jugadores)

jugadores = []
for i in range(cantidad_de_jugadores):
    system('cls')
    jugadores.append(input(f'Nombre del jugador N°{i+1}: '))

puntaje_de_jugadores = []
for i in range(cantidad_de_jugadores):
    puntaje_de_jugadores.append(0)

tipo_de_juego = 0
#Con este while evitamos que el usuario elija un parametro fuera de rango.
while tipo_de_juego != '1' and tipo_de_juego != '2' and tipo_de_juego != '3':
    system('cls')
    tipo_de_juego = input("Que tipo de juego desea?\n1.Corto\n2.Mediano\n3.Largo\n\n>>")
if tipo_de_juego == '1':
    casillas = 4
elif tipo_de_juego == '2':
    casillas = 8
elif tipo_de_juego == '3':
    casillas = 12

def crear_tableros():
    tableros = []
    for i in range(cantidad_de_jugadores):
        tableros.append([])
        pares =[]
        print((casillas*casillas)//2)
        for m in range((casillas*casillas)//2):
            if m >= 9:
                pares.append(str(m+1))
                pares.append(str(m+1))
            else:
                pares.append('0'+str(m+1))
                pares.append('0'+str(m+1))

        for e in range(casillas):
            tableros[i].append([])
            for j in range(casillas):
                tableros[i][e].append([])
                tableros[i][e][j] = Carta()
                par = randrange(0, len(pares))
                tableros[i][e][j].nombre = pares[par]
                pares.pop(par)
    return tableros

tableros = crear_tableros()

def definir_comodines_acumulados():
    comodines_acumulados = []
    for i in range(cantidad_de_jugadores):
        comodines_acumulados.append([0, 0, 0, 0])
    return comodines_acumulados

comodines_acumulados = definir_comodines_acumulados()

def imprimir_tableros(player, X1='', Y1='', X2='', Y2=''):
    system('cls')
    print(f'Turno de: {jugadores[player]}\n')
    print(f'Comodines acumulados.\nReplay:   {comodines_acumulados[player][0]}\nLayout:   {comodines_acumulados[player][1]}')
    print(f'Toti:     {comodines_acumulados[player][2]}\nFatality: {comodines_acumulados[player][3]}\n')
    encabezado = '       A  B  C  D  E  F  G  H  I  J  K  L\n     ------------------------------------'
    if casillas == 4:
        print(encabezado[:17],encabezado[41:59])
    if casillas == 8:
        print(encabezado[:29],encabezado[41:71])
    if casillas == 12:
        print(encabezado[:41],encabezado[41:83])

    for i in range(casillas):
        fila = ''
        for e in range(casillas):
            if i == Y1 and X1 == e:
                fila = fila + ' ' + str(tableros[player][i][e].nombre)
            elif i == Y2 and X2 == e:
                fila = fila + ' ' + str(tableros[player][i][e].nombre)
            else:
                fila = fila + ' ' + str(tableros[player][i][e].estado)

        if i >= 9:
            print(i+1, '|', fila)
        else:
            print(i+1,' |', fila)

def verificar_cartas(player):
    completo = True
    for i in range(len(tableros[player])):
        for e in range(len(tableros[player][i])):
            if tableros[player][i][e].estado == '??':
                completo = False

    return completo

def mezclar_de_nuevo(player):
    mazo = []
    for i in range(len(tableros[player])):
        for e in range(len(tableros[player][i])):
            if tableros[player][i][e].estado == '??':
                mazo.append(tableros[player][i][e].nombre)

    for i in range(len(tableros[player])):
        for e in range(len(tableros[player][i])):
            if tableros[player][i][e].estado == '??':
                maz = randrange(0, len(mazo))
                tableros[player][i][e].nombre = mazo[maz]
                mazo.pop(maz)

def ronda(player):
    main = True
    while main == True:
        bucle = True

        imprimir_tableros(player)
        input('Enter para tirar el dado...')
        tirar_dado(player, comodines_acumulados[player])
        input('\n\nEnter para continuar...')

        while bucle == True:
            imprimir_tableros(player)
            carta1 = input('Escribe las coordenadas de la primera carta(A-1): ').split('-')
            if verificar_input(carta1, casillas) == True:
                bucle = False
            else:
                print('Hubo un error con las coordenadas, verfique que estan bien escritas.')
                input('Enter para continuar...')

        bucle = True
        while bucle == True:
            imprimir_tableros(player, letra_a_numero(carta1[0]), int(carta1[1])-1)
            carta2 = input('Escribe las coordenadas de la segunda carta(B-1): ').split('-')
            if carta1 == carta2:
                print('No podes elegir la misma carta.')
                input('Enter para continuar...')
            elif verificar_input(carta2, casillas) == True:
                bucle = False
            else:
                print('Hubo un error con las coordenadas, verfique que estan bien escritas.')
                input('Enter para continuar...')

        imprimir_tableros(player, letra_a_numero(carta1[0]), int(carta1[1])-1, letra_a_numero(carta2[0]), int(carta2[1])-1)


        if tableros[player][int(carta1[1])-1][letra_a_numero(carta1[0])].nombre == tableros[player][int(carta2[1])-1][letra_a_numero(carta2[0])].nombre:
            tableros[player][int(carta1[1])-1][letra_a_numero(carta1[0])].estado = tableros[player][int(carta1[1])-1][letra_a_numero(carta1[0])].nombre
            tableros[player][int(carta2[1])-1][letra_a_numero(carta2[0])].estado = tableros[player][int(carta2[1])-1][letra_a_numero(carta2[0])].nombre

            print('Bien Hecho, las cartas son iguales.')
            input('Enter para continuar...')
        else:
            print('Mala suerte, las cartas son distintas.')
            input('Enter para continuar...')

        resto_de_comodines = 0
        for i in range(len(comodines_acumulados[player])):
            resto_de_comodines += comodines_acumulados[player][i]

        if verificar_cartas(player) == True and resto_de_comodines == 0:
            print(f'Bien hecho {jugadores[player]}, has ganado. ')
            puntaje_de_jugadores[player] += 1
            print(f'{jugadores[player]} ha ganado {puntaje_de_jugadores[player]} veces')
            main = False
            return False


        else:
            bucle1 = True
            usar_comodin = ' '
            while usar_comodin != 'si' and usar_comodin != 'no':
                system('cls')
                usar_comodin = input('¿Desea usar un comodin?(si-no): ').lower()
                if usar_comodin in 'si':
                    cual = ''
                    while cual != '1' and cual != '2' and cual != '3' and cual != '4' and cual != '5':
                        system('cls')
                        cual = input('¿Que comodin quieres usar?\n1.Replay.\n2.Layout.\n3.Toti.\n4.Fatality.\n5.Cancelar.\n>>')
                        if cual == '1' and comodines_acumulados[player][0] > 0: #Replay
                            comodines_acumulados[player][0]-=1
                            main = True
                        elif cual == '2' and comodines_acumulados[player][1] > 0: #Layout
                            for i in range(len(tableros)):
                                if i != player:
                                    comodines_acumulados[player][1]-=1
                                    mezclar_de_nuevo(player)
                            main = False
                        elif cual == '3' and comodines_acumulados[player][2] > 0:#Toti
                            comodines_acumulados[player][2]-=1
                            for i in range(len(tableros)):
                                if i != player:
                                    if randrange(0, 1) == 0: # desordenar tablero en el eje Y.
                                        random.shuffle(tableros[player])

                                    else: # desordenar tablero en el eje X.
                                        tablero_transpuesto = calcular_transpuesta(tableros[player])
                                        random.shuffle(tablero_transpuesto)
                                        tableros[player] = calcular_transpuesta(tablero_transpuesto)

                            main = False

                        elif cual == '4' and comodines_acumulados[player][3] > 0:#Fatality
                            comodines_acumulados[player][3]-=1
                            for i in range(len(tableros)):
                                if i != player:
                                    for e in range(len(tableros[i])):
                                        for j in range(len(tableros[i][e])):
                                            tableros[i][e][j].estado = '??'

                            main = False
                        elif cual == '5':
                            main = False
                        else:
                            print('No tienes comodines suficientes o la opcion no es correcta.')
                            input('Enter para continuar...')
                            cual = ''

                elif usar_comodin in 'no':
                    bucle1 = False
                    main   = False

jugar = 'si'
while jugar == 'si':
    principal = True
    while principal != False:
        for i in range(len(jugadores)):
            if principal != False:
                principal = ronda(i)
                print(f'depuracion: {principal}')
            else:
                print('juego terminado')


    jugar = ' '
    while jugar != 'si' and jugar != 'no':
        system('cls')
        jugar  = input('¿Quieres seguir jugando?(si-no): ')
    tableros = crear_tableros()
    comodines_acumulados = definir_comodines_acumulados()

system('cls')
print('Los puntajes finales son:')
for i in range(cantidad_de_jugadores):
    print(f'{jugadores[i]}: {puntaje_de_jugadores[i]}')