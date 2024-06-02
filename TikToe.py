import os

# Clearing the Screen
# os.system('cls')

board = [' ' for _ in range(9)]


def print_board():
    print('\033[93;5m\t\t\t-------------\033[0m')
    for i in range(3):
        print('\t\t\t|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
        print('\033[93;5m\t\t\t-------------\033[0m')


def check_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # for in range
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


def play_game():
    # os.system('cls')
    os.system('clear')
    print('\033[37mWel-Come to the Tic Tac Toe!\033[0m')
    print_board()
    # current_player='\033[36mx\033[0m'
    current_player = '\033[36mx'
    while True:
        position = input('\033[35mPlayer ' + current_player + ' Choose a position(1-9) : \033[0m')
        position = int(position) - 1
        if board[position] == ' ':
            board[position] = current_player
        else:
            print('\033[91mInvalid move, Please try again..\033[0m')
            continue
        # os.system('cls')
        os.system('clear')
        print_board()
        if check_win(current_player):
            print('\033[92mPlayer ', current_player, ' wins!\033[0m')
            break
        if ' ' not in board:
            print('\033[35mIt\'s a tie! \033[0m')
            break
        current_player='0' if current_player=='x' else 'x'
        # current_player='0' if current_player=='x' else 'x'
        # current_player='\033[93m0\033[0m' if current_player=='x' else '\033[36mx\033[0m'
        # current_player = '\033[93m0' if current_player == 'x' else '\033[36mx'
        print('\033[0m')


play_game()

