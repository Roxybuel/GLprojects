import random

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def check_win(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


def make_a_move(player, position):
    if board[position - 1] == "-":
        board[position - 1] = player
    else:
        print("ERROR! Position already filled :(")
        main()


def get_computer_move():
    while True:
        position = random.randint(0, 8)
        if board[position - 1] != "X" and board[position - 1] != "O":
            return position


def main():
    while True:
        print_board()
        player_position = int(input("Enter a position(1-9): "))
        make_a_move("X", player_position)
        if check_win("X"):
            print("You win!")
            break
        computer_position = get_computer_move()
        make_a_move("O", computer_position)
        if check_win("O"):
            print("Computer wins!")
            print_board()
            break
        if "-" not in board:
            print("Tie game!")
            print_board()
            break


main()
