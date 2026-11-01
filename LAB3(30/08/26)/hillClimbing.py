def hill_climbing(values, start):

    current = start

    while True:

        print("Current:", current,
              "Value:", values[current])

        neighbors = []

        if current - 1 in values:
            neighbors.append(current - 1)

        if current + 1 in values:
            neighbors.append(current + 1)

        if not neighbors:
            break

        best_neighbor = max(
            neighbors,
            key=lambda x: values[x]
        )

        if values[best_neighbor] <= values[current]:
            break

        current = best_neighbor

    return current


values = {
    0: 2,
    1: 5,
    2: 8,
    3: 12,
    4: 10,
    5: 7
}

result = hill_climbing(values, 0)

print("Final state:", result)
print("Maximum value:", values[result])