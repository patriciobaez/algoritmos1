from random import shuffle, randint, seed

def replay():
    pass

def generate_shuffled_pairs_for_layout(board_size: int, list: list, same_random: int) -> list:
    '''
    Pre: Recibe el tamaño de la matriz, la lista de valores y una seed.
    Post: Retorna 1 matriz mezclada.
    '''
    seed(same_random) #esto es para que las dos matrices se mezclen de la misma forma
    shuffle(list)
    board = []
    for i in range(board_size):
        row = []
        for j in list[i*(board_size):board_size*(i+1)]:
            row.append(j)
        board.append(row)

    return board

def layout(player_empty_board, board_size, same_random):
    list = []

    for i in range(board_size):
      list.extend(player_empty_board[i])

    new_matrix = generate_shuffled_pairs_for_layout(board_size, list, same_random)
    print()
    player_empty_board.clear()

    for i in range(board_size):
      player_empty_board.append(new_matrix[i])

    print("SE APLICO LAYOUT")

def toti(player_empty_board, board_size):
    random = randint(1, 2)

    if random == 1:
        for i in range(board_size):
            player_empty_board[i].reverse()

    elif random == 2:
        player_empty_board.reverse()

    print("SE APLICO TOTI")

def fatality(matrix, board_size):
    traspuesta = []

    for i in range(board_size):
        traspuesta.append([])
        for j in range(board_size):
            traspuesta[i].append(matrix[j][i])

    matrix.clear()
    matrix.extend(traspuesta)
    print("SE APLICO FATALITY")

def play_card(player_cards: list, player_empty_board: list, board_size: int, player_board: list):
    '''
    Pre: Recibe una lista con las cartas que tiene el jugador y el tablero.
    Post: Pregunta que carta quiere usar y la ejecuta.
    '''
    print(f"Tienes estas cartas comodines: {player_cards}")
    print("A- Replay")
    print("B- Layout")
    print("C- Toti")
    print("D- Fatality")
    print("E- Ninguna")
    card = input("Ingrese la letra correspondiente al comodin que quiera usar: ")

    if card == ("a" or "A"):
        if "replay" in player_cards:
            player_cards.remove("replay")
            replay()

    elif card == ("b" or "B"):
        if "layout" in player_cards:
            player_cards.remove("layout")
            same_random = randint(1, 100)
            layout(player_empty_board, board_size, same_random)
            layout(player_board, board_size, same_random)

    elif card == ("c" or "C"):
        if "toti" in player_cards:
            player_cards.remove("toti")
            toti(player_empty_board, board_size)
            toti(player_board, board_size)

    elif card == ("d" or "D"):
        if "fatality" in player_cards:
            player_cards.remove("fatality")
            fatality(player_empty_board, board_size)
            fatality(player_board, board_size)

def print_player_board(board_size: int, player_empty_board: list):
    for i in range(board_size):
        print(f"{chr(97+i)}", player_empty_board[i])

def players_names_inputs() -> tuple:
    '''
    Pre: Pide los nombres.
    Post: Devuelve los nombres.
    '''
    player1 = input("Ingrese el nombre del jugador 1: ")
    player2 = input("Ingrese el nombre del jugador 2: ")
    return player1, player2

def cards_randomizer(prob_replay: int, prob_layout: int, prob_toti: int, prob_fatality: int) -> str:
    '''
    Pre: Recibe 4 probabilidades de que salga cada carta.
    Post: Devuelve una carta o ninguna.
    '''
    card = randint(1, 4)
    if card == 1:
        chance = randint(1, 100)
        if chance <= prob_replay: return "replay"

    elif card == 2:
        chance = randint(1, 100)
        if chance <= prob_layout: return "layout"

    elif card == 3:
        chance = randint(1, 100)
        if chance <= prob_toti: return "toti"

    else:
        chance = randint(1, 100)
        if chance <= prob_fatality: return "fatality"

def cards_output(game_parameters):
    '''
    Pre: 
    Post: 
    '''
    card = cards_randomizer(game_parameters[1], game_parameters[2], game_parameters[3], game_parameters[4], )
    print("A continuacion podrias recibir una carta la cual podes usar al finalizar tu turno o guardarla para mas adelante.")

    if card == None:
        print("No te toco ninguna carta en este turno. Mal año.\n")

    elif card == "replay":
        print("Te toco la carta Replay. Permite hacer un intento más durante el turno.\n")

    elif card == "layout":
        print("Te toco la carta Layout. Redistribuye todas las fichas del tablero del jugador que la tiene de manera aleatoria.\n")

    elif card == "toti":
        print("Te toco la carta Toti. Espeja el tablero del jugador que la tiene de forma azarosa, puede ser horizontal o vertical.\n")

    elif card == "fatality":
        print("Te toco la carta Fatality. Traspone el tablero del jugador que la usa.\n")
    
    return card

def clear_console(): # "LIMPIA LA CONSOLA"
    for i in range(100):
        print("\n")

def generate_shuffled_pairs(board_size: int, list: list) -> list:
    '''
    Pre: Recibe el tamaño de la matriz y la lista de valores.
    Post: Retorna 1 matriz mezclada.
    '''
    shuffle(list)
    board = []

    for i in range(board_size):
        row = []
        for j in list[i*(board_size):board_size*(i+1)]:
            row.append(j)
        board.append(row)

    return board

def create_board(board_size: int) -> tuple:
    '''
    Pre: Recibe el tamaño de la matriz.
    Post: Retorna una matriz.
    '''
    values = int((board_size*board_size)/2)
    list = []

    for i in range(2):
        for j in range(values):
            list.append(j)

    board = generate_shuffled_pairs(board_size, list)

    return board

def generate_pairs(board_size: int, list: list) -> list:
    '''
    Pre: Recibe el tamaño de la matriz y la lista de valores.
    Post: Retorna una tabla vacia.
    '''
    board = []

    for i in range(board_size):
        row = []
        for j in list[i*(board_size):board_size*(i+1)]:
            row.append(j)
        board.append(row)

    return board

def create_empty_board(board_size: int) -> list:
    '''
    Pre: Recibe el tamaño de la matriz.
    Post: Retorna una tabla vacia.
    '''
    values = int(board_size*board_size)
    list = []

    for i in range(values):
            list.append("__")

    empty_board = generate_pairs(board_size, list)

    return empty_board

def player1_turn(player2_board: list, board_size: int, player2_empty_board: list, players_names: tuple, game_parameters: tuple, player1_cards: list, player1_empty_board: list, player1_board: list) -> bool:
    '''
    Pre: Recibe la tabla del jugador 2, el tamanio de la tabla, la tabla del jugador 2 a llenar, los nombres de los jugadores y los parametros del juego.
    Post: Printea los valores elegidos por el jugador 1 y devuelve True o False si el jugador adivino correctamente o no.
    '''
    print(f"\nTurno de {players_names[0]}\n")

    card = cards_output(game_parameters)
    if card != None:
        player1_cards.append(card)

    print_player_board(board_size, player2_empty_board)

    print(f"\n{players_names[0]}, ingrese la coordenada de la primera ficha que quiere revelar.")
    letter1 = input("Ingrese SOLO la letra: ")
    num1 = (int(input("Ingrese SOLO el numero: ")) - 1)

    player2_empty_board[(ord(letter1.lower())-97)].pop(num1)
    player2_empty_board[(ord(letter1.lower())-97)].insert(num1, player2_board[(ord(letter1.lower())-97)][num1])

    print_player_board(board_size, player2_empty_board)

    print(f"\n{players_names[0]}, ingrese la coordenada de la segunda ficha que quiere revelar.")
    letter2 = input("Ingrese SOLO la letra: ")
    num2 = (int(input("Ingrese SOLO el numero: ")) - 1)

    player2_empty_board[(ord(letter2.lower())-97)].pop(num2)
    player2_empty_board[(ord(letter2.lower())-97)].insert(num2, player2_board[(ord(letter2.lower())-97)][num2])
    
    print_player_board(board_size, player2_empty_board)

    correct_answer = False

    if player2_board[(ord(letter1.lower())-97)][int(num1)] != player2_board[(ord(letter2.lower())-97)][int(num2)]: # Pregunta: Si el jugador ingresa la misma coordenada dos veces esa ficha va a quedar descubierta 
        player2_empty_board[(ord(letter1.lower())-97)].pop(num1)                                                   # como si fuera una de dos fichas que adivino. Lo tengo que arreglar?
        player2_empty_board[(ord(letter1.lower())-97)].insert(num1, "__")
        player2_empty_board[(ord(letter2.lower())-97)].pop(num2)
        player2_empty_board[(ord(letter2.lower())-97)].insert(num2, "__")

        input('No acertaste, presiona la tecla "Enter" para continuar.')

        #clear_console()
        correct_answer = False

    else:
        input("Bien!!!, presiona la tecla ""Enter"" para continuar.")
        #clear_console()
        correct_answer = True

    if player1_cards != []:
        play_card(player1_cards, player1_empty_board, board_size, player1_board)

    return correct_answer

def player2_turn(player1_board: list, board_size: int, player1_empty_board: list, players_names: tuple, game_parameters: tuple, player2_cards: list, player2_empty_board: list, player2_board: list) -> bool:
    '''
    Pre: Recibe la tabla del jugador 1, el tamanio de la tabla, la tabla del jugador 1 a llenar, los nombres de los jugadores y los parametros del juego.
    Post: Printea los valores elegidos por el jugador 1 y devuelve True o False si el jugador adivino correctamente o no.
    '''
    print(f"\nTurno de {players_names[1]}\n")

    card = cards_output(game_parameters)
    if card != None:
        player2_cards.append(card)

    print_player_board(board_size, player1_empty_board)

    print(f"\n{players_names[1]}, ingrese la coordenada de la primera ficha que quiere revelar.")
    letter1 = input("Ingrese SOLO la letra: ")
    num1 = (int(input("Ingrese SOLO el numero: ")) - 1)

    player1_empty_board[(ord(letter1.lower())-97)].pop(num1)
    player1_empty_board[(ord(letter1.lower())-97)].insert(num1, player1_board[(ord(letter1.lower())-97)][num1])

    print_player_board(board_size, player1_empty_board)

    print(f"\n{players_names[1]}, ingrese la coordenada de la segunda ficha que quiere revelar.")
    letter2 = input("Ingrese SOLO la letra: ")
    num2 = (int(input("Ingrese SOLO el numero: ")) - 1)

    player1_empty_board[(ord(letter2.lower())-97)].pop(num2)
    player1_empty_board[(ord(letter2.lower())-97)].insert(num2, player1_board[(ord(letter2.lower())-97)][num2])

    print_player_board(board_size, player1_empty_board)

    correct_answer = True

    if player1_board[(ord(letter1.lower())-97)][int(num1)] != player1_board[(ord(letter2.lower())-97)][int(num2)]:
        player1_empty_board[(ord(letter1.lower())-97)].pop(num1)
        player1_empty_board[(ord(letter1.lower())-97)].insert(num1, "__")
        player1_empty_board[(ord(letter2.lower())-97)].pop(num2)
        player1_empty_board[(ord(letter2.lower())-97)].insert(num2, "__")

        input("No acertaste, presiona la tecla ""Enter"" para continuar.")
        #clear_console()
        correct_answer = True
    else:
        input("Bien!!!, presiona la tecla ""Enter"" para continuar.")
        #clear_console()
        correct_answer = False

    if player2_cards != []:
        play_card(player2_cards, player2_empty_board, board_size, player2_board)

    return correct_answer

def menu_options():
    print("1. Si desea comenzar una partida ingrese 1")
    print("2. Si desea definir los parametros del juego ingrese 2")
    print("3. Si desea ver los puntajes de partidas anteriores ingrese 3")

def start_menu() -> tuple:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBienvenido al Memotest!\n")
    menu_options()
    menu_choice = input("")

    while menu_choice.isnumeric() == False:
        print("No ingreso ninguna de las opciones. Por favor, intente nuevamente.")
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

    if menu_choice == 1:
        print("\nINICIA PARTIDA\n")     #estas lineas son temporales
        duration = 4
        prob_replay = 50
        prob_layout =50
        prob_toti = 50
        prob_fatality = 50

    elif menu_choice == 2:
        print("DEFINIR PARAMETROS\n")
        duration = input("Ingrese la duracion de la partida a)corta, b)media o C)larga: ")
        if duration == "corta" or "Corta" or "CORTA": duration = 4
        elif duration == "media" or "Media" or "MEDIA": duration = 8
        elif duration == "larga" or "Larga" or "LARGA": duration = 12
        
        prob_replay = int(input("Ingrese la probabilidad de que salga la carta replay de 0 a 100: "))
        prob_layout = int(input("Ingrese la probabilidad de que salga la carta layout de 0 a 100: "))
        prob_toti = int(input("Ingrese la probabilidad de que salga la carta toti de 0 a 100: "))
        prob_fatality = int(input("Ingrese la probabilidad de que salga la carta fatality de 0 a 100: "))

    else: print("PUNTAJE\n")
    return duration, prob_replay, prob_layout, prob_toti, prob_fatality

    #score = input("Quiere ver el score de las partidas anteriores(si/no): ")

def game(player1_board: list, player1_empty_board: list, player2_board: list, player2_empty_board: list, board_size: int, players_names: tuple, game_parameters: tuple):
    repeat_turn = True
    player1_cards = []
    player2_cards = []
    while player1_board != player1_empty_board or player2_board != player2_empty_board:
        while repeat_turn == True:
            repeat_turn = player1_turn(player2_board, board_size, player2_empty_board, players_names, game_parameters, player1_cards, player1_empty_board, player1_board)
        while repeat_turn == False:
            repeat_turn = player2_turn(player1_board, board_size, player1_empty_board, players_names, game_parameters, player2_cards, player2_empty_board, player2_board)
    if player1_board == player1_empty_board:
        print(f"Gano el jugador {players_names[1]}")
    elif player2_board == player2_empty_board:
        print(f"Gano el jugador {players_names[0]}")
    print("Game Over")
    main()

def main():
    game_parameters = start_menu()
    board_size = game_parameters[0]

    player1_empty_board = create_empty_board(board_size)
    player2_empty_board = create_empty_board(board_size)
    player1_board = create_board(board_size)
    player2_board = create_board(board_size)

    print("Tabla del jugador 1") #TEMPORAL
    print_player_board(board_size, player1_board) #TEMPORAL
    print("Tabla del jugador 2") #TEMPORAL
    print_player_board(board_size, player2_board) #TEMPORAL

    players_names = players_names_inputs()
    game(player1_board, player1_empty_board, player2_board, player2_empty_board, board_size, players_names, game_parameters)

main()

"""
Preguntas TP:
esta mal usar funciones con muchos parametros?

"""