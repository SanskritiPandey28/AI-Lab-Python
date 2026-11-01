
import random


def fitness(board):
    n = len(board)
    attacking_pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1

    total_pairs = n * (n - 1) // 2
    return total_pairs - attacking_pairs


def tournament_selection(population, fitness_values, k=3):
    candidates = random.sample(
        range(len(population)),
        min(k, len(population))
    )

    winner = max(
        candidates,
        key=lambda i: fitness_values[i]
    )

    return population[winner][:]


def crossover(parent1, parent2):
    n = len(parent1)

    if n < 2:
        return parent1[:]

    point = random.randint(1, n - 1)

    child = parent1[:point] + parent2[point:]
    return child


def mutate(board, mutation_rate):
    board = board[:]

    for i in range(len(board)):
        if random.random() < mutation_rate:
            board[i] = random.randrange(len(board))

    return board


def genetic_algorithm(
    n=8,
    population_size=100,
    mutation_rate=0.1,
    max_generations=1000
):
    if n < 1 or population_size < 2:
        raise ValueError("N must be positive and population size >= 2")

    if not 0 <= mutation_rate <= 1:
        raise ValueError("Mutation rate must be between 0 and 1")

    target_fitness = n * (n - 1) // 2

    population = [
        [random.randrange(n) for _ in range(n)]
        for _ in range(population_size)
    ]

    for generation in range(max_generations + 1):
        scores = [fitness(board) for board in population]

        best_index = max(
            range(len(population)),
            key=lambda i: scores[i]
        )

        best_board = population[best_index][:]

        if scores[best_index] == target_fitness:
            return best_board, generation, True

        if generation == max_generations:
            break

        # Elitism: preserve the best chromosome
        new_population = [best_board]

        while len(new_population) < population_size:
            parent1 = tournament_selection(population, scores)
            parent2 = tournament_selection(population, scores)

            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)

            new_population.append(child)

        population = new_population

    return best_board, max_generations, False


def print_board(board):
    n = len(board)

    for row in range(n):
        print(" ".join(
            "Q" if board[col] == row else "."
            for col in range(n)
        ))


if __name__ == "__main__":
    random.seed(42)

    n = 8
    board, generations, solved = genetic_algorithm(
        n=n,
        population_size=100,
        mutation_rate=0.1,
        max_generations=1000
    )

    print("N =", n)
    print("Generations:", generations)
    print("Solved:", solved)
    print("Fitness:", fitness(board))
    print("Board:")
    print_board(board)
