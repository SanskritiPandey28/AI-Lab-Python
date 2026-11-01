def is_safe(board, row, col):
    # Check same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < 8:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row):
    # All 8 queens are placed
    if row == 8:
        return True

    # Try every column
    for col in range(8):

        if is_safe(board, row, col):
            # Place queen
            board[row] = col

            # Move to next row
            if solve_queens(board, row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


def print_board(board):
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# -1 means no queen placed
board = [-1] * 8

if solve_queens(board, 0):
    print("Solution found:")
    print_board(board)
else:
    print("No solution found.")