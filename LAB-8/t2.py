import random
def generate_successors(state, capacities):
    successors = set()
    num_jugs = len(capacities)
    for i in range(num_jugs):
        new_state = list(state)
        new_state[i] = capacities[i]
        successors.add(tuple(new_state))
        new_state = list(state)
        new_state[i] = 0
        successors.add(tuple(new_state))
        for j in range(num_jugs):
            if i != j:  # i -> j
                new_state = list(state)
                pour_amount = min(state[i], capacities[j] - state[j])
                new_state[i] -= pour_amount
                new_state[j] += pour_amount
                successors.add(tuple(new_state))
    return successors
def evaluate_heuristic(state, m):
    return sum(abs(jug - m) for jug in state)
def hill_climbing(initial_state, capacities, m, max_iterations=100):
    current_state = initial_state
    iterations = 0
    path = [current_state]
    while iterations < max_iterations:
        successors = list(generate_successors(current_state, capacities))
        successors.sort(key=lambda s: evaluate_heuristic(s, m))
        best_successor = successors[0]
        if evaluate_heuristic(best_successor, m) >= evaluate_heuristic(current_state, m):
            current_state = tuple(random.randint(0, cap) for cap in capacities)
            path.append(current_state)
        else:
            current_state = best_successor
            path.append(current_state)
        if m in current_state:
            print("Steps taken:")
            for step in path:
                print(step)
            return current_state
        iterations += 1
    print("Failed to Find Solution")
    return "Failed to Find Solution"
def solve_n_jugs(n, capacities, target_m):
    initial_state = tuple([0] * n)
    solution = hill_climbing(initial_state, capacities, target_m)
    print(f"Final State ({n} Jugs):", solution)
# Test Case 1: Two Jugs
solve_n_jugs(2, (3, 5), 4)
# Test Case 2: Three Jugs
solve_n_jugs(3, (3, 5, 8), 4)
