
def minimax(tree, node, is_max):
    # Base case: terminal node
    if isinstance(tree[node], int):
        return tree[node]

    values = [
        minimax(tree, child, not is_max)
        for child in tree[node]
    ]

    if is_max:
        return max(values)
    else:
        return min(values)


# Game tree representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}

# A is the MAX player's current state
optimal_value = minimax(tree, 'A', True)

print("Optimal utility value:", optimal_value)

# Determine the best move from the root
best_move = None
best_value = float('-inf')

for child in tree['A']:
    value = minimax(tree, child, False)

    if value > best_value:
        best_value = value
        best_move = child

print("Optimal move:", best_move)
