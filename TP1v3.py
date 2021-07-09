from random import shuffle, randint, seed
from os import system

def clear_console() -> None:
    '''
    Pre: -
    Post: Limpia la consola.
    '''
    system("cls")

def generate_shuffled_pairs_for_layout(board_size: int, list: list, same_random: int) -> list:
    '''
    Pre: Recibe el tamaño de una matriz, una lista de valores y una seed.
    Post: Retorna 1 matriz mezclada.
    '''
    seed(same_random) #Use el seed para poder mezclar de la misma forma a 2 matrices.
    shuffle(list)
    board = []
    for i in range(board_size):
        row = []
        for j in list[i*(board_size):board_size*(i+1)]:
            row.append(j)
        board.append(row)

    return board

def layout(player_board: list, board_size: int, same_random: int) -> None:
    '''
    Pre: Recibe la matriz de un jugador, el tamaño de la matriz, y una seed.
    Post: Modifica la matriz recibida, mezclandola completamente.
    '''
    list = []
    for i in range(board_size):
      list.extend(player_board[i])

    new_matrix = generate_shuffled_pairs_for_layout(board_size, list, same_random)
    print()
    player_board.clear()

    for i in range(board_size):
      player_board.append(new_matrix[i])

def toti(player_board: int, board_size: int) -> None:
    '''
    Pre: Recibe la matriz de un jugador y el tamanio del tablero.
    Post: Modifica la matriz, espejandola vertical u horizontalmente aleatoriamente.
    '''
    random = randint(1, 2)
    if random == 1:
        for i in range(board_size):
            player_board[i].reverse()

    elif random == 2:
        player_board.reverse()

def fatality(player_board: list, board_size: int) -> None:
    '''
    Pre: Recibe una matriz y su tamanio
    Post: Modifica la matriz recibida, de forma que quede como la matriz traspuesta.
    '''
    traspuesta = []
    for i in range(board_size):
        traspuesta.append([])
        for j in range(board_size):
            traspuesta[i].append(player_board[j][i])

    player_board.clear()
    player_board.extend(traspuesta)

def play_card(player_cards: list, player_updated_board: list, board_size: int, player_board: list, repeat_turn: list) -> None:
    '''
    Pre: Recibe una lista con las cartas que tiene el jugador, la matriz actual,
     la matriz original, el tamanio de la matiz y una lista con info sobre si se va a repetir el turno o no.
    Post: Ejecuta una funcion correspondiente a una carta y elinima la misma de la lista de cartas.
    '''
    print(f"Tienes estas cartas comodines: {player_cards}")
    print("A- Replay\nB- Layout\nC- Toti\nD- Fatality\nE- Ninguna")
    card = input("Ingrese la letra correspondiente al comodin que quiera usar: ")

    if card == ("a" or "A"): #Aca se revisa que el mazo del jugador contenga la carta seleccionada, la elimina del mazo y la ejecuta.
        if "replay" in player_cards:
            player_cards.remove("replay")
            repeat_turn.pop(0)
            repeat_turn.insert(0, True)

    elif card == ("b" or "B"):
        if "layout" in player_cards:
            player_cards.remove("layout")
            same_random = randint(1, 100)
            layout(player_updated_board, board_size, same_random)
            layout(player_board, board_size, same_random)

    elif card == ("c" or "C"):
        if "toti" in player_cards:
            player_cards.remove("toti")
            toti(player_updated_board, board_size)
            toti(player_board, board_size)

    elif card == ("d" or "D"):
        if "fatality" in player_cards:
            player_cards.remove("fatality")
            fatality(player_updated_board, board_size)
            fatality(player_board, board_size)

def print_player_board(board_size: int, player_updated_board: list) -> None:
    '''
    Pre: Recibe el tamanio de la matriz y la matriz actual del jugador en cuestion.
    Post: Muestra la matriz de un jugador de forma jugable.
    '''
    for i in range(board_size):
        print(f"{chr(97+i)}", player_updated_board[i])

def reveal_board_elements(player_name: str, other_player_updated_board: list, other_player_board: list, board_size: int) -> tuple:
    '''
    Pre: Recibe el nombre del jugador, la matriz del contrincante actualizada, la matriz del contrincante completa y el tamanio de la matriz.
    Post: Devuelve una tupla con: la primera letra ingresada, el primer numero ingresado, la segunda letra ingresada y el segundo numero ingresado.
    '''
    print(f"\n{player_name}, ingrese la coordenada de la primera ficha que quiere revelar.")
    letter1 = input("Ingrese SOLO la letra de la fila: ")
    while letter1.isalpha() == False:
        print("No ingreso una letra, intente nuevamente.")
        letter1 = input("Ingrese SOLO la letra de la fila: ")
    num1 = input("Ingrese SOLO el numero de la columna: ")
    while num1.isnumeric() == False:
        print("No ingreso un numero, intente nuevamente.")
        num1 = input("Ingrese SOLO el numero de la columna: ")
    num1 = int(num1) - 1

    other_player_updated_board[(ord(letter1.lower())-97)].pop(num1)
    other_player_updated_board[(ord(letter1.lower())-97)].insert(num1, other_player_board[(ord(letter1.lower())-97)][num1])

    print_player_board(board_size, other_player_updated_board)

    print(f"\n{player_name}, ingrese la coordenada de la segunda ficha que quiere revelar.")
    letter2 = input("Ingrese SOLO la letra de la fila: ")
    while letter2.isalpha() == False:
        print("No ingreso una letra, intente nuevamente.")
        letter2 = input("Ingrese SOLO la letra de la fila: ")
    num2 = input("Ingrese SOLO el numero de la columna: ")
    while num2.isnumeric() == False:
        print("No ingreso un numero, intente nuevamente.")
        num2 = input("Ingrese SOLO el numero de la columna: ")
    num2 = int(num2) - 1

    while letter1 == letter2 and num1 == num2:
        print(f"\n{player_name}, ingrese la coordenada de la segunda ficha que quiere revelar(Debe ser diferente a la primera coordenada ingresada).")
        letter2 = input("Ingrese SOLO la letra de la fila: ")
        num2 = (int(input("Ingrese SOLO el numero de la columna: ")) - 1)

    other_player_updated_board[(ord(letter2.lower())-97)].pop(num2)
    other_player_updated_board[(ord(letter2.lower())-97)].insert(num2, other_player_board[(ord(letter2.lower())-97)][num2])

    return letter1, num1, letter2, num2 

def player_name_inputs() -> tuple:
    '''
    Pre: -
    Post: Devuelve una tupla con el nombre del jugador 1 y el nombre del jugador 2.
    '''
    player1 = input("Ingrese el nombre del jugador 1: ")
    player2 = input("Ingrese el nombre del jugador 2: ")
    return player1, player2

def cards_randomizer(prob_replay: int, prob_layout: int, prob_toti: int, prob_fatality: int) -> str:
    '''
    Pre: Recibe 4 probabilidades de que salga cada carta.
    Post: Devuelve una variable(str) con el nombre de la carta que salio o None
    '''
    card = randint(1, 4)
    chance = randint(1, 100)
    new_card = ""
    if card == 1:
        if chance <= prob_replay: new_card = "replay"
    elif card == 2:
        if chance <= prob_layout: new_card = "layout"
    elif card == 3:
        if chance <= prob_toti: new_card = "toti"
    elif card == 4:
        if chance <= prob_fatality: new_card = "fatality"

    return new_card

def cards_output(game_parameters: tuple) -> str:
    '''
    Pre: Recive una tupla con los parametros del juego.
    Post: Devuelve una variable(str).
    '''
    card = cards_randomizer(game_parameters[1], game_parameters[2], game_parameters[3], game_parameters[4], )
    print("A continuacion podrias recibir una carta la cual podes usar al finalizar tu turno o guardarla para mas adelante.")

    if card == "":
        print("No te toco ninguna carta en este turno. Mal año.\n")

    elif card == "replay":
        print("Te toco la carta Replay. Permite hacer un intento más durante el turno.\n(CUIDADO! Si usas esta carta cuando ya te corespondia otro turno la perdes)\n")

    elif card == "layout":
        print("Te toco la carta Layout. Redistribuye todas las fichas del tablero del jugador que la tiene de manera aleatoria.\n")

    elif card == "toti":
        print("Te toco la carta Toti. Espeja el tablero del jugador que la tiene de forma azarosa, puede ser horizontal o vertical.\n")

    elif card == "fatality":
        print("Te toco la carta Fatality. Traspone el tablero del jugador que la usa.\n")
    
    return card

def generate_shuffled_pairs(board_size: int, board_elements: list) -> list:
    '''
    Pre: Recibe el tamaño de la matriz y la lista de valores.
    Post: Retorna 1 matriz mezclada.
    '''
    shuffle(board_elements)
    board = []
    for i in range(board_size):
        row = []
        for j in board_elements[i*(board_size):board_size*(i+1)]:
            row.append(j)
        board.append(row)

    return board

def create_board(board_size: int) -> list:
    '''
    Pre: Recibe el tamaño de la matriz.
    Post: Retorna una matriz ordenada con elementos que se repiten 1 sola vez.
    '''
    values = int((board_size*board_size)/2)
    board_elements_list = []
    for i in range(2):
        for j in range(values):
            board_elements_list.append(j)

    board = generate_shuffled_pairs(board_size, board_elements_list)
    
    return board

def generate_pairs(board_size: int, hidden_elements: list) -> list:
    '''
    Pre: Recibe el tamaño de la matriz y la lista de valores.
    Post: Retorna una matriz vacia.
    '''
    board = []
    for i in range(board_size):
        row = []
        for j in hidden_elements[i*(board_size):board_size*(i+1)]:
            row.append(j)
        board.append(row)

    return board

def create_empty_board(board_size: int) -> list:
    '''
    Pre: Recibe el tamaño de la matriz.
    Post: Retorna una matriz "vacia".
    '''
    values = int(board_size*board_size)
    hidden_elements = []
    for i in range(values):
            hidden_elements.append("_")

    empty_board = generate_pairs(board_size, hidden_elements)

    return empty_board

def player_turn(this_player_data: list, other_player_data: list, game_parameters: tuple, repeat_turn: list) -> None:
    '''
    Pre: Recibe la informacion del jugador actual y la del otro jugador, en listas por separado. Tambien recibe
     una tupla con los parametros del juego y otra lista con informacion sobre si el jugador va a tener otro turno o no.
    Post: Modifica las matrizes de los jugadores que recibe(a traves de otras funciones) y la lista relacionada a el
     funcionamiento de los turnos
    '''
    board_size = game_parameters[0]
    player_name = this_player_data[0]
    other_player_updated_board = other_player_data[2] #Es el tablero del otro jugador, osea con la que se esta jugando en este momento.
    other_player_board = other_player_data[1]
    player_cards = this_player_data[3]
    this_player_updated_board = this_player_data[2] #Es la tabla del jugador que esta en su turno, osea con la que juega el otro jugador
    this_player_board = this_player_data[1]         # y la cual se le aplican los comodines.

    print(f"\n\n\nTURNO DE {player_name.upper()}\n")

    card = cards_output(game_parameters)      #Aca se le reparte una carta al jugador, o no.
    if card != "":
        player_cards.append(card)

    print_player_board(board_size, other_player_updated_board)
    #A continuacion el jugador elije que lugares revelar en el tablero.
    chosen_positions = reveal_board_elements(player_name, other_player_updated_board, other_player_board, board_size)
    letter1 = chosen_positions[0]
    num1 = chosen_positions[1]
    letter2 = chosen_positions[2]
    num2 = chosen_positions[3]

    print_player_board(board_size, other_player_updated_board)
    #A continuacion, si el jugador no acierta con su eleccion, se vuelven a esconder las fichas antes reveladas.
    if other_player_board[(ord(letter1.lower())-97)][int(num1)] != other_player_board[(ord(letter2.lower())-97)][int(num2)]:
        other_player_updated_board[(ord(letter1.lower())-97)].pop(num1)
        other_player_updated_board[(ord(letter1.lower())-97)].insert(num1, "_")
        other_player_updated_board[(ord(letter2.lower())-97)].pop(num2)
        other_player_updated_board[(ord(letter2.lower())-97)].insert(num2, "_")

        repeat_turn.pop(0) #Aca se cambia el valor de repeat_turn para que corte el while del turno.
        repeat_turn.insert(0, False)

        input('No acertaste, presiona la tecla "Enter" para continuar.')

    else:
        input("Bien!!!, presiona la tecla ""Enter"" para continuar.")

    if player_cards != []: play_card(player_cards, this_player_updated_board, board_size, this_player_board, repeat_turn)

def menu_options() -> None:
    '''
    Pre: -
    Post: Printea las opciones del menu.
    '''
    print("1. Empezar una partida.")
    print("2. Definir los parametros del juego.")
    print("3. Ver los puntajes de partidas anteriores.")

def start_menu(score_board: dict) -> tuple:
    '''
    Pre: Recive un diccionario con los puntajes.
    Post: Devuelve una tupla con los parametros de la partida y con el diccionario de puntajes.
    '''
    clear_console()
    print("Bienvenido al Memotest!\n")
    menu_options()
    menu_choice = input("Ingrese el numero correspondiente: ")

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
        print("\nINICIA PARTIDA\n")
        duration = 4
        prob_replay = 50
        prob_layout =50
        prob_toti = 50
        prob_fatality = 50

    elif menu_choice == 2:
        print("DEFINIR PARAMETROS\n")
        duration = input("Ingrese el numero correspondiente con la duracion de la partida.\n1-Corta\n2-Media\n3-Larga\n: ")
        if duration == ("1"): duration = 4
        elif duration == ("2"): duration = 8
        elif duration == ("3"): duration = 12
        
        prob_replay = int(input("Ingrese la probabilidad de que salga la carta replay de 0 a 100: "))
        prob_layout = int(input("Ingrese la probabilidad de que salga la carta layout de 0 a 100: "))
        prob_toti = int(input("Ingrese la probabilidad de que salga la carta toti de 0 a 100: "))
        prob_fatality = int(input("Ingrese la probabilidad de que salga la carta fatality de 0 a 100: "))

    else:
        duration = 4
        prob_replay = 50
        prob_layout =50
        prob_toti = 50
        prob_fatality = 50
        print("PUNTAJE")
        if score_board == {}:
            print("Todavia no se jugo ninguna partida.\n")
        else:
            score_board_descending_list = list(score_board.items()) #Aca se arma una lista de tuplas a partir del diccionario
            score_board_descending_list.sort(reverse=True, key=lambda x: x[1]) #Aca se ordena esa lista por el segundo elemento de las tuplas.
            print(score_board_descending_list)

    return duration, prob_replay, prob_layout, prob_toti, prob_fatality, score_board

def game(player1_data: list, player2_data: list, game_parameters: tuple) -> None:
    '''
    Pre: Recibe 2 listas con la informacion de cada jugador y una tupla con los parametros del juego.
    Post: Actualiza los valores del diccionario(los puntajes).
    '''
    score_board = game_parameters[5]
    player1_cards = []
    player2_cards = []
    player1_data.append(player1_cards)
    player2_data.append(player2_cards)
    while  player1_data[1] != player1_data[2] and player2_data[1] != player2_data[2]: #Logica de los turnos.
        repeat_p1_turn = [True]
        repeat_p2_turn = [True]
        while repeat_p1_turn[0] == True and player2_data[1] != player2_data[2]:
            player_turn(player1_data, player2_data, game_parameters, repeat_p1_turn)

        while repeat_p2_turn[0] == True and player1_data[1] != player1_data[2] and player2_data[1] != player2_data[2]:
            player_turn(player2_data, player1_data, game_parameters, repeat_p2_turn)

    if player1_data[1] == player1_data[2]: #Aca se agregan los datos al score.
        print(f"\nGano  {player2_data[0]}!!!\n")
        if player2_data[0] in score_board: score_board[player2_data[0]] += 1
        else: score_board[player2_data[0]] = 1
        
    elif player2_data[1] == player2_data[2]: #Aca se agregan los datos al score.
        print(f"\nGano  {player1_data[0]}!!!\n")
        if player1_data[0] in score_board: score_board[player1_data[0]] += 1
        else: score_board[player1_data[0]] = 1

def main() -> None:
    score_board = {}
    play_again = True
    while play_again == True:
        stay_in_menu = True
        while stay_in_menu == True:
            game_parameters = start_menu(score_board)
            stay_in_menu = input("Que queres hacer?\n1- Volver al menu principal.\n2- Empezar el juego.\n")
            if stay_in_menu == "1": stay_in_menu = True
            else: stay_in_menu = False

        board_size = game_parameters[0]

        player1_updated_board = create_empty_board(board_size)
        player2_updated_board = create_empty_board(board_size)
        player1_board = create_board(board_size)
        player2_board = create_board(board_size)

        players_names = player_name_inputs()
        player1_data = [players_names[0], player1_board, player1_updated_board]
        player2_data = [players_names[1], player2_board, player2_updated_board]

        game(player1_data, player2_data, game_parameters)

        if input("Queres volver al menu y comenzar otra partida?\n1-Si\n2-No\nIngrese el numero correspondiente: ") == "1":
            play_again = True
        else: play_again = False

main()