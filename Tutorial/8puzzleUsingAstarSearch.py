
import heapq
import time

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def misplaced_tiles(state):
    return sum(
        1 for i, tile in enumerate(state)
        if tile != 0 and tile != GOAL[i]
    )


def manhattan_distance(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        current_row, current_col = divmod(i, 3)
        goal_row, goal_col = divmod(tile - 1, 3)

        distance += (
            abs(current_row - goal_row)
            + abs(current_col - goal_col)
        )

    return distance


def is_solvable(state):
    tiles = [x for x in state if x != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0


def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    neighbors = []

    moves = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr * 3 + nc
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def astar(start, heuristic):
    if not is_solvable(start):
        return None, 0

    # Priority queue entries: (f, g, state)
    pq = [(heuristic(start), 0, start)]

    best_g = {start: 0}
    parent = {start: None}
    expanded = 0

    while pq:
        f, g, state = heapq.heappop(pq)

        # Ignore outdated queue entries
        if g != best_g.get(state):
            continue

        if state == GOAL:
            path = []
            current = state

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], expanded

        expanded += 1

        for neighbor in get_neighbors(state):
            new_g = g + 1

            if new_g < best_g.get(neighbor, float("inf")):
                best_g[neighbor] = new_g
                parent[neighbor] = state

                new_f = new_g + heuristic(neighbor)
                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    return None, expanded


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


def main():
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    for name, heuristic in [
        ("Misplaced Tiles", misplaced_tiles),
        ("Manhattan Distance", manhattan_distance)
    ]:
        start_time = time.perf_counter()
        path, expanded = astar(start, heuristic)
        elapsed = time.perf_counter() - start_time

        print("\nHeuristic:", name)

        if path is None:
            print("Puzzle is unsolvable.")
            continue

        print("Solution length:", len(path) - 1)
        print("Expanded nodes:", expanded)
        print("Execution time:", round(elapsed, 6), "seconds")

        for step, state in enumerate(path):
            print("Step", step)
            print_board(state)


if __name__ == "__main__":
    main()
