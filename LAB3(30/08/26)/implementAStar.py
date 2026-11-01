import heapq

def a_star(graph, heuristic, start, goal):

    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], 0, start))

    cost = {start: 0}
    parent = {start: None}

    while priority_queue:

        f, g, current = heapq.heappop(priority_queue)

        print("Expanding:", current)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], g

        for neighbor, edge_cost in graph[current]:

            new_cost = g + edge_cost

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost
                parent[neighbor] = current

                f_value = new_cost + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (f_value, new_cost, neighbor)
                )

    return None


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'F': 1,
    'G': 0
}

result = a_star(graph, heuristic, 'A', 'G')

print("Path:", result[0])
print("Cost:", result[1])