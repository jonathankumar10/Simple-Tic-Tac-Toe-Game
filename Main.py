import random


# DISPLAY BOARD
def display_board(board):
    print('\n'*100)

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# PLAYER INPUTS
def player_input():
    marker = ''

    while(marker != 'X' and marker != 'O'):
        marker = input("Player1 pick a marker 'X' or 'O'").upper()
        player1 = marker

        if(player1 == 'X'):
            player2 = 'O'
        else:
            player2 = 'X'

    return (player1, player2)


# MARKER POSITIONS FOR PLAYER INPUTS
def place_marker(board, marker, position):
    board[position] = marker


# CHECKER TO SEE WINNER
def win_check(board, mark):
    if((board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark)):
        return True
    else:
        return False


# DECIDER TO SEE WHICH PLAYER GOES FIRST
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# SPACE CHECKER
def space_check(board, position):
    return board[position] == ''


# CHECKS TO SEE IF THE BOARD IS FULL
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please enter a number'))

    return position


# ASKS PLAYER TO PLAY AGAIN
def replay():
    choice = input('Play again? Enter Yes or No').lower().startswith('y')

    return choice


print('Welcome to Tic Tac Toe!!')

while True:

    # RESET THE BOARD
    the_board = ['']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go First')

    play_game = input('Ready to play?? y or n?')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # PLAYER 1'S TURN
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # PLAYER 2'S TURN
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
