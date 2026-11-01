def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(board):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c]:
            if board[a] != " ":
                return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(board, is_maximizing):

    result = check_winner(board)

    # Terminal states
    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "Draw":
        return 0

    # Computer's turn
    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    # Human's turn
    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def best_move(board):
    best_score = -float("inf")
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Main game
board = [" "] * 9

print("Tic-Tac-Toe")
print("You are X")
print("Computer is O")

while True:

    print_board(board)

    # Human move
    position = int(input("Enter your position (1-9): ")) - 1

    if position < 0 or position >= 9 or board[position] != " ":
        print("Invalid move!")
        continue

    board[position] = "X"

    result = check_winner(board)

    if result is not None:
        print_board(board)

        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")

        break

    # Computer move
    computer_move = best_move(board)
    board[computer_move] = "O"

    print("Computer chose:", computer_move + 1)

    result = check_winner(board)

    if result is not None:
        print_board(board)

        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")

        break
    

