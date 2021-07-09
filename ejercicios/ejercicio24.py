"""
3) Para celebrar el Día del Niño, en una plaza de gran extensión, se ha construido un
caminito de baldosas cuadradas de hormigón de 3 colores: blanco, gris y negro. El
caminito no tiene bifurcaciones y para que quedase más vistoso, se cuidó que las
baldosas contiguas tuvieran diferente color.
Lamentablemente el caminito ha perdido muchas de sus baldosas, ya que debieron ser
quitadas para realizar un complejo tendido de cañerías. La figura muestra el estado
actual del caminito.
Los huecos dejados por las baldosas removidas se muestran cuadriculados. Quienes
deben reconstruir el caminito desean dejarlo tal como estaba, pero no se llevó el 
registro de los colores y ubicaciones de las baldosas removidas. Por lo tanto, se decide
reconstruirlo respetando las que quedaron siguiendo la consigna original de que las
contiguas no queden del mismo color, comprando las baldosas nuevas que hagan falta.
Para ayudar en la reconstrucción se pide que escriba una función caminito(BALDOSAS)
que devuelva un posible diseño para reconstruir el caminito y que también lo escriba
por pantalla.
Su parámetro es “baldosas”: una PALABRA conteniendo caracteres ‘B’ (blanco), ‘N’
(negro), ‘G’ (gris) o ‘R’ (removido) separadas con coma “,” describiendo la vereda en su
estado actual, esperando que sustituyas las ‘R’ por las letras que describan los colores
de tu propuesta. La longitud de la palabra no es conocida.
Tu propuesta de caminito deberá ser devuelta por la función y escrita por pantalla la
palabra con la propuesta.
Ejemplo:
El parámetro BALDOSAS describe la figura y contiene: R,G,N,R,R,N,R,R,R,B,R,N
El programa deberá escribir por pantalla una línea como la siguiente BGNBGNGBGBGN
"""

baldosas = "R,G,R,R,R,N,R,R,R,B,R,N"



def caminito(baldosas):
    baldosas = baldosas.split(",")
    print(baldosas)
    for i in range(len(baldosas)):
        colores = ["B", "N", "G"]
        if baldosas[i] == "R":
            if i == 0 and baldosas[i+1] != "R":
                colores.remove(baldosas[i+1])
            elif (i+1) == len(baldosas) and baldosas[i-1] != "R":
                colores.remove(baldosas[i-1])
            else:
                if baldosas[i+1] == "R" and baldosas[i-1] == "R":
                    pass
                else:
                    if baldosas[i+1] != "R":
                        colores.remove(baldosas[i+1])
                    if baldosas[i-1] != "R":
                        colores.remove(baldosas[i-1])

            baldosas[i] = colores[0]
    print(baldosas)




caminito(baldosas)