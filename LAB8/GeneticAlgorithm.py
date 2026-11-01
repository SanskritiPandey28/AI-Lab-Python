import random

# Reproducible results
random.seed(42)

# Problem settings
CHROMOSOME_LENGTH = 5
POPULATION_SIZE = 20
MAX_GENERATIONS = 100
ELITE_COUNT = 2

CROSSOVER_RATE = 0.80
INITIAL_MUTATION_RATE = 1 / CHROMOSOME_LENGTH
MIN_MUTATION_RATE = 0.01
MAX_MUTATION_RATE = 0.30


# Convert binary chromosome to decimal
def decode(chromosome):
    return int(chromosome, 2)


# Fitness function: maximize x^2
def fitness(chromosome):
    x = decode(chromosome)
    return x ** 2


# Generate a random chromosome
def create_chromosome():
    return "".join(
        random.choice("01")
        for _ in range(CHROMOSOME_LENGTH)
    )


# Tournament selection
def tournament_selection(population, tournament_size=3):
    contestants = random.sample(population, tournament_size)
    return max(contestants, key=fitness)


# Single-point crossover
def crossover(parent1, parent2, crossover_rate):
    if random.random() >= crossover_rate:
        return parent1, parent2

    point = random.randint(1, CHROMOSOME_LENGTH - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


# Bit-flip mutation
def mutate(chromosome, mutation_rate):
    bits = list(chromosome)

    for i in range(len(bits)):
        if random.random() < mutation_rate:
            bits[i] = "1" if bits[i] == "0" else "0"

    return "".join(bits)


# Measure population diversity
def population_diversity(population):
    return len(set(population)) / len(population)


# Improved Genetic Algorithm
def genetic_algorithm():

    population = [
        create_chromosome()
        for _ in range(POPULATION_SIZE)
    ]

    best_ever = max(population, key=fitness)
    best_fitness = fitness(best_ever)

    stalled_generations = 0
    mutation_rate = INITIAL_MUTATION_RATE

    for generation in range(1, MAX_GENERATIONS + 1):

        # Sort population by fitness
        population.sort(key=fitness, reverse=True)

        current_best = population[0]
        current_best_fitness = fitness(current_best)

        # Update the best solution
        if current_best_fitness > best_fitness:
            best_ever = current_best
            best_fitness = current_best_fitness
            stalled_generations = 0

            # Reduce mutation after improvement
            mutation_rate = max(
                MIN_MUTATION_RATE,
                mutation_rate * 0.8
            )
        else:
            stalled_generations += 1

        # Calculate population diversity
        diversity = population_diversity(population)

        print(
            f"Generation {generation:02d} | "
            f"Best x = {decode(best_ever):2d} | "
            f"Fitness = {best_fitness:4d} | "
            f"Diversity = {diversity:.2f} | "
            f"Mutation = {mutation_rate:.3f}"
        )

        # Stop if the optimal solution is found
        if best_fitness == 31 ** 2:
            break

        # Increase mutation if progress stalls
        if stalled_generations >= 5:
            mutation_rate = min(
                MAX_MUTATION_RATE,
                mutation_rate * 1.5
            )
            stalled_generations = 0

        # Increase mutation when diversity is low
        if diversity < 0.35:
            mutation_rate = min(
                MAX_MUTATION_RATE,
                mutation_rate * 1.25
            )

        # Elitism: preserve the best solutions
        new_population = population[:ELITE_COUNT]

        # Generate the next generation
        while len(new_population) < POPULATION_SIZE:

            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)

            child1, child2 = crossover(
                parent1,
                parent2,
                CROSSOVER_RATE
            )

            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population

    print("\nFinal Result")
    print("Best chromosome:", best_ever)
    print("Best x:", decode(best_ever))
    print("Maximum fitness:", best_fitness)
    print("Generations used:", generation)


# Run the algorithm
if __name__ == "__main__":
    genetic_algorithm()