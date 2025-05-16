import numpy as np
import random
import matplotlib.pyplot as plt
POP_SIZE = 100
MUTATION_RATE = 0.2
MAX_GENERATIONS = 1000
def fitness(chromosome):
    n = len(chromosome)
    non_attacking_pairs = n * (n - 1) // 2
    attacking_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(chromosome[i] - chromosome[j]) == j - i:
                attacking_pairs += 1
    return non_attacking_pairs - attacking_pairs
def init_population(size, n):
    return [random.sample(range(1, n + 1), n) for _ in range(size)]
def select(population):
    fitness_values = [fitness(ind) for ind in population]
    total_fit = sum(fitness_values)
    probabilities = [f / total_fit for f in fitness_values]
    return population[np.random.choice(len(population), p=probabilities)]
def crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    child = [None] * n
    child[start:end] = parent1[start:end]
    fill_values = [x for x in parent2 if x not in child]
    idx = 0
    for i in range(n):
        if child[i] is None:
            child[i] = fill_values[idx]
            idx += 1
    return child
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome
def genetic_algorithm(n):
    population = init_population(POP_SIZE, n)
    best_solution = None
    for generation in range(MAX_GENERATIONS):
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        if fitness(population[0]) == n * (n - 1) // 2:
            best_solution = population[0]
            break
        new_population = []
        new_population.append(population[0])
        while len(new_population) < POP_SIZE:
            parent1, parent2 = select(population), select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
        best_solution = population[0]
    return best_solution
def visualize_board(solution):
    if not solution:
        print("No solution found")
        return
    n = len(solution)
    board = np.zeros((n, n))
    for row, col in enumerate(solution):
        board[row][col - 1] = 1
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(n + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(n + 1) - 0.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=1.5)
    ax.tick_params(which="minor", size=0)
    ax.imshow(board, cmap="binary")
N = 10
solution = genetic_algorithm(N)
print("Best solution found for N =", N, ":", solution)
visualize_board(solution)
