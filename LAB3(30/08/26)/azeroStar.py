def ao_star(graph, heuristic, node, solved):

    if node not in graph or len(graph[node]) == 0:
        solved.add(node)
        return heuristic[node]

    best_cost = float('inf')
    best_option = None

    for option in graph[node]:

        cost = 0

        for child in option:
            cost += heuristic[child]

        if cost < best_cost:
            best_cost = cost
            best_option = option

    heuristic[node] = best_cost

    print("Expanding:", node)
    print("Selected:", best_option)

    for child in best_option:
        if child not in solved:
            ao_star(graph, heuristic, child, solved)

    solved.add(node)

    return heuristic[node]


graph = {
    'A': [['B'], ['C', 'D']],
    'B': [],
    'C': [],
    'D': []
}

heuristic = {
    'A': 10,
    'B': 4,
    'C': 2,
    'D': 3
}

solved = set()

cost = ao_star(graph, heuristic, 'A', solved)

print("Final cost:", cost)
print("Solved nodes:", solved)