from collections import deque

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def get_neighbors(state):
    neighbors = []

    zero_pos = state.index(0)
    row = zero_pos // 3
    col = zero_pos % 3

    # Up
    if row > 0:
        new_state = list(state)
        new_state[zero_pos], new_state[zero_pos - 3] = \
            new_state[zero_pos - 3], new_state[zero_pos]
        neighbors.append(tuple(new_state))

    # Down
    if row < 2:
        new_state = list(state)
        new_state[zero_pos], new_state[zero_pos + 3] = \
            new_state[zero_pos + 3], new_state[zero_pos]
        neighbors.append(tuple(new_state))

    # Left
    if col > 0:
        new_state = list(state)
        new_state[zero_pos], new_state[zero_pos - 1] = \
            new_state[zero_pos - 1], new_state[zero_pos]
        neighbors.append(tuple(new_state))

    # Right
    if col < 2:
        new_state = list(state)
        new_state[zero_pos], new_state[zero_pos + 1] = \
            new_state[zero_pos + 1], new_state[zero_pos]
        neighbors.append(tuple(new_state))

    return neighbors


def bfs(start, goal):
    queue = deque([start])
    visited = {start}

    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        for neighbor in get_neighbors(current):

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current

    return None


# Initial state
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

# Goal state
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution = bfs(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step in solution:
        print_puzzle(step)
else:
    print("No solution found.")






