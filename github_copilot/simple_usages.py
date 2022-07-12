import random
import matplotlib.pyplot as plt


# a function that returns n random integer numbers from 0 to 25
def random_numbers_0_25(n):
    return random.sample(range(0, 25), n)


def hist_random_numbers_0_25(n):
    numbers = random_numbers_0_25(n)
    plt.hist(numbers, bins=5)
    plt.show()


"""Testes em pt-br"""
# uma função que descomprima um arquivo zip
def unzip_file(file_name):
    import zipfile
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()
    return zip_ref


#contrua um jogo de tic tac toe
def tic_tac_toe():
    import numpy as np
    import matplotlib.pyplot as plt
    import random
    import time

    # define the board size
    board_size = 3

    # define the board
    board = np.zeros((board_size, board_size))

    # define the player symbols
    player_symbols = ['X', 'O']

    # define the player turn
    player_turn = 0

    # define the game status
    game_status = True

    # define the game loop
    while game_status:

        # define the board display
        board_display = np.zeros((board_size, board_size))

        # define the board display loop
        for i in range(board_size):
            for j in range(board_size):
                if board[i, j] == 0:
                    board_display[i, j] = ' '
                else:
                    board_display[i, j] = board[i, j]

        # define the board display display
        print('\n')
        for i in range(board_size):
            print(' ', end='')
            for j in range(board_size):
                print('|' + str(board_display[i, j]) + '|', end='')
            print('\n')

        # define the player turn loop
        while game_status:

            # define the player turn display
            print('Player ' + player_symbols[player_turn] + ' turn:')

            # define the player turn input
            player_input = input('Enter the row and column number separated by a space: ')

            # define the player turn input split
            player_input_split = player_input.split(' ')

            # define the player turn input split row
            player_input_split_row = int(player_input_split[0])

            # define the player turn input split column
            player_input_split_column = int(player_input_split[1])

            # define the player turn input loop
            if board[player_input_split_row, player_input_split_column] == 0:
                board[player_input_split_row, player_input_split_column] = player_symbols[player_turn]
                break
            else:
                print('Invalid input!')

# run tic tac toe
tic_tac_toe()
