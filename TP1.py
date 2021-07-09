import random

def p1_board() -> list:
    player1_board4x4 = [["banana", "manzana", "banana", "sandia"],
                 ["durazno", "sandia", "melon", "kiwi"],
                  ["kiwi", "mandarina", "naranja", "durazno"],
                  ["naranja", "mandarina", "melon", "manzana"]]

    random.shuffle(player1_board4x4)
    random.shuffle(player1_board4x4[0])
    random.shuffle(player1_board4x4[1])
    random.shuffle(player1_board4x4[2])
    random.shuffle(player1_board4x4[3])

    player1_board8x8 = [["lechuga", "rucula", "zanahoria", "zapallo", "durazno", "banana", "manzana", "pera"],
                 ["brocoli", "rucula", "cebolla", "lechuga", "mandarina", "kiwi", "kiwi", "naranja"],
                  ["morron", "zanahoria", "brocoli", "calabaza", "sandia", "pera", "palta", "pepino"],
                  ["cebolla", "zapallo", "calabaza", "morron", "chaucha", "pomelo", "apio", "mandarina"],
                   ["papa", "acelga", "naranja", "tomate", "choclo", "uva", "batata", "aceituna"],
                 ["arveja", "manzana", "uva", "berenjena", "durazno", "apio", "sandia", "achicoria"],
                  ["berenjena", "achicoria", "tomate", "choclo", "frutilla", "papa", "pomelo", "aceituna"],
                  ["chaucha", "arveja", "banana", "acelga", "palta", "frutilla", "batata", "pepino"]]

    random.shuffle(player1_board8x8)
    random.shuffle(player1_board8x8[0])
    random.shuffle(player1_board8x8[1])
    random.shuffle(player1_board8x8[2])
    random.shuffle(player1_board8x8[3])
    random.shuffle(player1_board8x8[4])
    random.shuffle(player1_board8x8[5])
    random.shuffle(player1_board8x8[6])
    random.shuffle(player1_board8x8[7])

    player1_board12x12 = [["Singapur", "Nueva Zelanda", "Australia", "Suiza", "Irlanda", "Taiwán", "Reino Unido", "Estonia", "Canada", "Dinamarca", "Islandia", "Georgia"],
                 ["Mauricio", "Emiratos Arabes Unidos", "Lituania", "Paises Bajos", "Finlandia", "Luxenburgo", "Chile", "EEUU", "Suecia", "Malasia", "España", "Barhein"],
                  ["Polonia", "Tailandia", "Rumania", "Uruguay", "Jamaica", "Macedonia del Norte", "Ruanda", "Eslovenia", "Colombia", "Peru", "Botswana", "Portugal"],
                  ["Santa Lucia", "Serbia", "Hungria", "Indonesia", "Brunei Darussalam", "Kosovo", "Francia", "Arabia Saudita", "Panama", "Republica Eslovaca", "Seychelles", "San Vicente"],
                  ["Mexico", "Albania", "Barbados", "Italia", "Honduras", "Sudafrica", "Benin", "Ghana", "Trinidad y Tobago", "Papua Nueva Guinea", "Gambia", "Nigeria"],
                 ["Uganda", "China", "Uzbekistan", "Butan", "Gabon", "Senegal", "Madagascar", "Togo", "Belize", "Tonga", "Guyana", "Argentina"],
                   ["Singapur", "Nueva Zelanda", "Australia", "Suiza", "Irlanda", "Taiwán", "Reino Unido", "Estonia", "Canada", "Dinamarca", "Islandia", "Georgia"],
                 ["Mauricio", "Emiratos Arabes Unidos", "Lituania", "Paises Bajos", "Finlandia", "Luxenburgo", "Chile", "EEUU", "Suecia", "Malasia", "España", "Barhein"],
                  ["Polonia", "Tailandia", "Rumania", "Uruguay", "Jamaica", "Macedonia del Norte", "Ruanda", "Eslovenia", "Colombia", "Peru", "Botswana", "Portugal"],
                  ["Santa Lucia", "Serbia", "Hungria", "Indonesia", "Brunei Darussalam", "Kosovo", "Francia", "Arabia Saudita", "Panama", "Republica Eslovaca", "Seychelles", "San Vicente"],
                   ["Mexico", "Albania", "Barbados", "Italia", "Honduras", "Sudafrica", "Benin", "Ghana", "Trinidad y Tobago", "Papua Nueva Guinea", "Gambia", "Nigeria"],
                 ["Uganda", "China", "Uzbekistan", "Butan", "Gabon", "Senegal", "Madagascar", "Togo", "Belize", "Tonga", "Guyana", "Argentina"]]

    random.shuffle(player1_board12x12)
    random.shuffle(player1_board12x12[0])
    random.shuffle(player1_board12x12[1])
    random.shuffle(player1_board12x12[2])
    random.shuffle(player1_board12x12[3])
    random.shuffle(player1_board12x12[4])
    random.shuffle(player1_board12x12[5])
    random.shuffle(player1_board12x12[6])
    random.shuffle(player1_board12x12[7])
    random.shuffle(player1_board12x12[8])
    random.shuffle(player1_board12x12[9])
    random.shuffle(player1_board12x12[10])
    random.shuffle(player1_board12x12[11])

    return player1_board4x4

def p2_board() -> list:
    player2_board4x4 = [["banana", "manzana", "banana", "sandia"],
                 ["durazno", "sandia", "melon", "kiwi"],
                  ["kiwi", "mandarina", "naranja", "durazno"],
                  ["naranja", "mandarina", "melon", "manzana"]]

    #player2_board4x4_empty = [["*", "*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*"]]

    #random.shuffle(player2_board4x4)
    #random.shuffle(player2_board4x4[0])
    #random.shuffle(player2_board4x4[1])
    #random.shuffle(player2_board4x4[2]) 
    #random.shuffle(player2_board4x4[3])

    #
    print(player2_board4x4) #TEMPORAL

    return player2_board4x4

    player2_board8x8 = [["lechuga", "rucula", "zanahoria", "zapallo", "durazno", "banana", "manzana", "pera"],
                 ["brocoli", "rucula", "cebolla", "lechuga", "mandarina", "kiwi", "kiwi", "naranja"],
                  ["morron", "zanahoria", "brocoli", "calabaza", "sandia", "pera", "palta", "pepino"],
                  ["cebolla", "zapallo", "calabaza", "morron", "chaucha", "pomelo", "apio", "mandarina"],
                   ["papa", "acelga", "naranja", "tomate", "choclo", "uva", "batata", "aceituna"],
                 ["arveja", "manzana", "uva", "berenjena", "durazno", "apio", "sandia", "achicoria"],
                  ["berenjena", "achicoria", "tomate", "choclo", "frutilla", "papa", "pomelo", "aceituna"],
                  ["chaucha", "arveja", "banana", "acelga", "palta", "frutilla", "batata", "pepino"]]

    random.shuffle(player2_board8x8)
    random.shuffle(player2_board8x8[0])
    random.shuffle(player2_board8x8[1])
    random.shuffle(player2_board8x8[2])
    random.shuffle(player2_board8x8[3])
    random.shuffle(player2_board8x8[4])
    random.shuffle(player2_board8x8[5])
    random.shuffle(player2_board8x8[6])
    random.shuffle(player2_board8x8[7])

    player2_board12x12 = [["Singapur", "Nueva Zelanda", "Australia", "Suiza", "Irlanda", "Taiwán", "Reino Unido", "Estonia", "Canada", "Dinamarca", "Islandia", "Georgia"],
                 ["Mauricio", "Emiratos Arabes Unidos", "Lituania", "Paises Bajos", "Finlandia", "Luxenburgo", "Chile", "EEUU", "Suecia", "Malasia", "España", "Barhein"],
                  ["Polonia", "Tailandia", "Rumania", "Uruguay", "Jamaica", "Macedonia del Norte", "Ruanda", "Eslovenia", "Colombia", "Peru", "Botswana", "Portugal"],
                  ["Santa Lucia", "Serbia", "Hungria", "Indonesia", "Brunei Darussalam", "Kosovo", "Francia", "Arabia Saudita", "Panama", "Republica Eslovaca", "Seychelles", "San Vicente"],
                  ["Mexico", "Albania", "Barbados", "Italia", "Honduras", "Sudafrica", "Benin", "Ghana", "Trinidad y Tobago", "Papua Nueva Guinea", "Gambia", "Nigeria"],
                 ["Uganda", "China", "Uzbekistan", "Butan", "Gabon", "Senegal", "Madagascar", "Togo", "Belize", "Tonga", "Guyana", "Argentina"],
                   ["Singapur", "Nueva Zelanda", "Australia", "Suiza", "Irlanda", "Taiwán", "Reino Unido", "Estonia", "Canada", "Dinamarca", "Islandia", "Georgia"],
                 ["Mauricio", "Emiratos Arabes Unidos", "Lituania", "Paises Bajos", "Finlandia", "Luxenburgo", "Chile", "EEUU", "Suecia", "Malasia", "España", "Barhein"],
                  ["Polonia", "Tailandia", "Rumania", "Uruguay", "Jamaica", "Macedonia del Norte", "Ruanda", "Eslovenia", "Colombia", "Peru", "Botswana", "Portugal"],
                  ["Santa Lucia", "Serbia", "Hungria", "Indonesia", "Brunei Darussalam", "Kosovo", "Francia", "Arabia Saudita", "Panama", "Republica Eslovaca", "Seychelles", "San Vicente"],
                   ["Mexico", "Albania", "Barbados", "Italia", "Honduras", "Sudafrica", "Benin", "Ghana", "Trinidad y Tobago", "Papua Nueva Guinea", "Gambia", "Nigeria"],
                 ["Uganda", "China", "Uzbekistan", "Butan", "Gabon", "Senegal", "Madagascar", "Togo", "Belize", "Tonga", "Guyana", "Argentina"]]

    random.shuffle(player2_board12x12)
    random.shuffle(player2_board12x12[0])
    random.shuffle(player2_board12x12[1])
    random.shuffle(player2_board12x12[2])
    random.shuffle(player2_board12x12[3])
    random.shuffle(player2_board12x12[4])
    random.shuffle(player2_board12x12[5])
    random.shuffle(player2_board12x12[6])
    random.shuffle(player2_board12x12[7])
    random.shuffle(player2_board12x12[8])
    random.shuffle(player2_board12x12[9])
    random.shuffle(player2_board12x12[10])
    random.shuffle(player2_board12x12[11])

def player1_turn(board : list, board_current : list) -> list:
    player2_board = board
    player2_board_current = board_current

    print("TURNO DEL JUGADOR 1\n            1                         2                         3                         4")
    print("A", player2_board_current[0])
    print("B", player2_board_current[1])
    print("C", player2_board_current[2])
    print("D", player2_board_current[3])

    print("\nJugador 1, ingrese la coordenada de la primera ficha que quiere revelar(Ej: A1 para ver la primer ficha): ")
    letter1 = input("Ingrese SOLO la letra: ")
    num1 = (int(input("Ingrese SOLO el numero: ")) - 1)
    print("\nJugador 1, ingrese la coordenada de la segunda ficha que quiere revelar(Ej: D4 para ver la ultima ficha): ")
    letter2 = input("Ingrese SOLO la letra: ")
    num2 = (int(input("Ingrese SOLO el numero: ")) - 1)

    if len(player2_board[(ord(letter1.lower())-97)][num1]) == 4: player2_board[(ord(letter1.lower())-97)][num1] = ("         ") + player2_board[(ord(letter1.lower())-97)][num1] + ("         ")
    elif len(player2_board[(ord(letter1.lower())-97)][num1]) == 5: player2_board[(ord(letter1.lower())-97)][num1] = ("        ") + player2_board[(ord(letter1.lower())-97)][num1] + ("         ")
    elif len(player2_board[(ord(letter1.lower())-97)][num1]) == 6: player2_board[(ord(letter1.lower())-97)][num1] = ("        ") + player2_board[(ord(letter1.lower())-97)][num1] + ("        ")
    elif len(player2_board[(ord(letter1.lower())-97)][num1]) == 7: player2_board[(ord(letter1.lower())-97)][num1] = ("       ") + player2_board[(ord(letter1.lower())-97)][num1] + ("        ")
    elif len(player2_board[(ord(letter1.lower())-97)][num1]) == 8: player2_board[(ord(letter1.lower())-97)][num1] = ("       ") + player2_board[(ord(letter1.lower())-97)][num1] + ("       ")
    if len(player2_board[(ord(letter2.lower())-97)][num2]) == 4: player2_board[(ord(letter2.lower())-97)][num2] = ("         ") + player2_board[(ord(letter2.lower())-97)][num2] + ("         ")
    elif len(player2_board[(ord(letter2.lower())-97)][num2]) == 5: player2_board[(ord(letter2.lower())-97)][num2] = ("        ") + player2_board[(ord(letter2.lower())-97)][num2] + ("         ")
    elif len(player2_board[(ord(letter2.lower())-97)][num2]) == 6: player2_board[(ord(letter2.lower())-97)][num2] = ("        ") + player2_board[(ord(letter2.lower())-97)][num2] + ("        ")
    elif len(player2_board[(ord(letter2.lower())-97)][num2]) == 7: player2_board[(ord(letter2.lower())-97)][num2] = ("       ") + player2_board[(ord(letter2.lower())-97)][num2] + ("        ")
    elif len(player2_board[(ord(letter2.lower())-97)][num2]) == 8: player2_board[(ord(letter2.lower())-97)][num2] = ("       ") + player2_board[(ord(letter2.lower())-97)][num2] + ("       ")

    player2_board_current[(ord(letter1.lower())-97)].pop(num1)
    player2_board_current[(ord(letter1.lower())-97)].insert(num1, player2_board[(ord(letter1.lower())-97)][num1])
    player2_board_current[(ord(letter2.lower())-97)].pop(num2)
    player2_board_current[(ord(letter2.lower())-97)].insert(num2, player2_board[(ord(letter2.lower())-97)][num2])

    print("            1                         2                         3                         4")
    print("A", player2_board_current[0], "\nB", player2_board_current[1], "\nC", player2_board_current[2], "\nD", player2_board_current[3])
    
    if player2_board[(ord(letter1.lower())-97)][int(num1)] == player2_board[(ord(letter2.lower())-97)][int(num2)]:
        return player2_board_current

def player2_turn(board : list):
    print("TURNO DEL JUGADOR 2")
    print("")
    print("Jugador 2, ingrese la coordenada de la ficha que quiere revelar(Ej: A1 para ver la primer ficha): ")
    
def menu_options():
    print("1. Si desea comenzar una partida ingrese 1")
    print("2. Si desea definir los parametros del juego ingrese 2")
    print("3. Si desea ver los puntajes de partidas anteriores ingrese 3")

def start_menu():
    print("\nBienvenido al Memotest!\n\n")
    menu_options()
    menu_choice = input("")

    while menu_choice.isnumeric() == False:
        print("\nNo ingreso ninguna de las opciones. Por favor, intente nuevamente.")
        menu_options()
        menu_choice = input("")

    menu_choice = int(menu_choice)

    while menu_choice < 1 or menu_choice > 3:
        print("\nNo ingreso ninguna de las opciones. Por favor, intente nuevamente.")
        menu_options()
        menu_choice = input("")

        while menu_choice.isnumeric() == False:
            print("\nNo ingreso ninguna de las opciones. Por favor, intente nuevamente.")
            menu_options()
            menu_choice = input("")

        menu_choice = int(menu_choice)

    if menu_choice == 1: print("INICIA PARTIDA\n")     #estas lineas son temporales
    elif menu_choice == 2: print("DEFINIR PARAMETROS")
    else: print("PUNTAJE")

    #player1 = input("Ingrese el nombre del jugador 1: ")
    #player2 = input("Ingrese el nombre del jugador 2: ")
    #duration = input("Ingrese que duracion quiere para la partida: corta, media o larga: ")
    #prob_replay
    #prob_layout
    #prob_toti
    #prob_fatality

    #score = input("Quiere ver el score de las partidas anteriores(si/no): ")

def game(p2board : list):
    player2_board_empty = [['______________________', '______________________', '______________________', '______________________'], ['______________________', '______________________', '______________________', '______________________'], ['______________________', '______________________', '______________________', '______________________'], ['______________________', '______________________', '______________________', '______________________']]
    player2_board = player1_turn(p2board, player2_board_empty) 
    #print("\n            1                         2                         3                         4")
    #print("A", player2_board[0], "\nB", player2_board[1], "\nC", player2_board[2], "\nD", player2_board[3])
    while player2_board != player2_board_empty:
        player1_turn(p2board, player2_board)
    
def main():
    #player1_board = p1_board()
    player2_board_original = p2_board()
    #emptyboard = p2_board()
    start_menu()
    game(player2_board_original)

main()