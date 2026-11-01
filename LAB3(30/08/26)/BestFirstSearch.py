import heapq

def best_first_search(graph, heuristic, start, goal):

    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while priority_queue:

        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        print("Expanding:", current)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in graph[current]:

            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
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

path = best_first_search(graph, heuristic, 'A', 'G')

print("Path:", path)