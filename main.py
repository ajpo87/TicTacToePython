def print_board(board):
    print("   |   |   ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("___|___|___")
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("   |   |   ")

def get_move(player, board):
    while True:
        move = input(f"{player}'s turn. Enter a position (1-9): ")
        if not move.isdigit():
            print("Invalid input. Please enter a number between 1 and 9.")
        elif int(move) < 1 or int(move) > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
        elif board[int(move)-1] != " ":
            print("Position already taken. Please choose another position.")
        else:
            return int(move)-1

def check_win(board):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for positions in win_positions:
        if board[positions[0]] == board[positions[1]] == board[positions[2]] != " ":
            return board[positions[0]]
    if " " not in board:
        return "tie"
    return None

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        move = get_move(players[turn], board)
        board[move] = players[turn]
        winner = check_win(board)
        if winner is not None:
            if winner == "tie":
                print("Tie game!")
            else:
                print(f"{winner} wins!")
            break
        turn = (turn + 1) % 2

play_game()