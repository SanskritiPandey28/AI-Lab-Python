
import math
import time

EMPTY = " "
HUMAN = "X"
AI = "O"

# Center and corners first: a useful move ordering
MOVE_ORDER = [4, 0, 2, 6, 8, 1, 3, 5, 7]

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and (
            board[a] == board[b] == board[c]
        ):
            return board[a]

    return None


def terminal_score(board, depth):
    result = winner(board)

    if result == AI:
        return 10 - depth
    if result == HUMAN:
        return depth - 10
    if EMPTY not in board:
        return 0

    return None


def print_board(board):
    for row in range(3):
        print(" | ".join(board[row * 3:row * 3 + 3]))
        if row < 2:
            print("--+---+--")


def minimax(
    board, depth, maximizing, max_depth,
    use_pruning, alpha=-math.inf, beta=math.inf,
    stats=None
):
    if stats is None:
        stats = {"nodes": 0}

    stats["nodes"] += 1

    score = terminal_score(board, depth)

    if score is not None:
        return score

    if depth >= max_depth:
        # Neutral heuristic for non-terminal cutoff states.
        # This is a simple baseline, not a strong evaluator.
        return 0

    if maximizing:
        best = -math.inf

        for move in MOVE_ORDER:
            if board[move] == EMPTY:
                board[move] = AI

                value = minimax(
                    board, depth + 1, False, max_depth,
                    use_pruning, alpha, beta, stats
                )

                board[move] = EMPTY
                best = max(best, value)

                if use_pruning:
                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break

        return best

    else:
        best = math.inf

        for move in MOVE_ORDER:
            if board[move] == EMPTY:
                board[move] = HUMAN

                value = minimax(
                    board, depth + 1, True, max_depth,
                    use_pruning, alpha, beta, stats
                )

                board[move] = EMPTY
                best = min(best, value)

                if use_pruning:
                    beta = min(beta, best)

                    if beta <= alpha:
                        break

        return best


def best_move(board, max_depth=9, use_pruning=True):
    best_score = -math.inf
    selected_move = None
    stats = {"nodes": 0}

    for move in MOVE_ORDER:
        if board[move] == EMPTY:
            board[move] = AI

            score = minimax(
                board, 1, False, max_depth,
                use_pruning, stats=stats
            )

            board[move] = EMPTY

            if score > best_score:
                best_score = score
                selected_move = move

    return selected_move, best_score, stats["nodes"]


def compare_search_methods(board, depth=9):
    for pruning in (False, True):
        start = time.perf_counter()

        move, score, nodes = best_move(
            board, depth, pruning
        )

        elapsed = time.perf_counter() - start

        print(
            "Alpha-Beta:", pruning,
            "| Best move (1-9):", move + 1 if move is not None else None,
            "| Score:", score,
            "| Nodes:", nodes,
            "| Time:", round(elapsed, 6), "seconds"
        )


def play():
    board = [EMPTY] * 9

    print("Positions are numbered 1 to 9.")
    print_board([str(i) for i in range(1, 10)])

    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue

        if move not in range(9) or board[move] != EMPTY:
            print("Invalid move.")
            continue

        board[move] = HUMAN

        if winner(board) == HUMAN:
            print_board(board)
            print("You win!")
            break

        if EMPTY not in board:
            print_board(board)
            print("Draw!")
            break

        move, _, _ = best_move(board)

        if move is not None:
            board[move] = AI

        print_board(board)

        if winner(board) == AI:
            print("AI wins!")
            break

        if EMPTY not in board:
            print("Draw!")
            break


if __name__ == "__main__":
    # Compare the methods on an empty board.
    print("Search comparison:")
    compare_search_methods([EMPTY] * 9, depth=9)

    print("\nStart the game:")
    play()
