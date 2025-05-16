import heapq
def count_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts
def a_star_8queens():
    open_list = [(0, [0] * 8, 0)]
    visited_states = 0
    while open_list:
        f_score, board, g_score = heapq.heappop(open_list)
        visited_states += 1
        if count_conflicts(board) == 0:
            return board, visited_states
        for row in range(8):
            for col in range(8):
                if board[row] != col:
                    new_board = board[:]
                    new_board[row] = col
                    h_score = count_conflicts(new_board)
                    new_g_score = g_score + 1
                    new_f_score = new_g_score + h_score
                    heapq.heappush(open_list, (new_f_score, new_board, new_g_score))
    return None, visited_states
def ga_8queens():
    N = 8
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
    population = init_population(POP_SIZE, N)
    visited_states = 0
    for generation in range(MAX_GENERATIONS):
        visited_states += len(population)
        population = sorted(population, key=lambda x: fitness(x), reverse=True)
        if fitness(population[0]) == N * (N - 1) // 2:
            return population[0], visited_states
        new_population = []
        new_population.append(population[0])
        while len(new_population) < POP_SIZE:
            parent1, parent2 = select(population), select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    return None, visited_states
a_star_solution, a_star_states = a_star_8queens()
ga_solution, ga_states = ga_8queens()
print("A* Search:")
print("Solution:", a_star_solution)
print("States Explored:", a_star_states)
print("\nGenetic Algorithm:")
print("Solution:", ga_solution)
print("States Explored:", ga_states)
