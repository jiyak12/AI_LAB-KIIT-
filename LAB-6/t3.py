import heapq
import time
from typing import Tuple, List, Optional
def misplaced_tiles(state: Tuple[int]) -> int:
    return sum(1 for i, tile in enumerate(state) if tile != 0 and tile != i + 1)
def manhattan_distance(state: Tuple[int]) -> int:
    distance = 0
    for index, tile in enumerate(state):
        if tile != 0:
            goal_index = tile - 1
            current_row, current_col = index // 4, index % 4
            goal_row, goal_col = goal_index // 4, goal_index % 4
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance
def get_neighbors(state: Tuple[int]) -> List[Tuple[int]]:
    neighbors = []
    size = 4
    zero_index = state.index(0)
    row, col = zero_index // size, zero_index % size
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < size and 0 <= new_col < size:
            new_index = new_row * size + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))
    return neighbors
def a_star_search(start: Tuple[int], goal: Tuple[int], heuristic) -> Optional[Tuple[List[Tuple[int]], int]]:
    frontier = []
    heapq.heappush(frontier, (heuristic(start), 0, start, [start]))
    explored = set()
    nodes_explored = 0
    while frontier:
        priority, cost, current, path = heapq.heappop(frontier)
        nodes_explored += 1
        if current == goal:
            return path, nodes_explored
        explored.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in explored:
                new_cost = cost + 1
                new_priority = new_cost + heuristic(neighbor)
                heapq.heappush(frontier, (new_priority, new_cost, neighbor, path + [neighbor]))
    return None, nodes_explored
def compare_heuristics(start_state: Tuple[int], goal_state: Tuple[int]):
    heuristics = {
        "Misplaced Tiles": misplaced_tiles,
        "Manhattan Distance": manhattan_distance
    }
    results = {}
    for name, heuristic in heuristics.items():
        start_time = time.time()
        path, nodes_explored = a_star_search(start_state, goal_state, heuristic)
        end_time = time.time()
        solution_depth = len(path) - 1 if path is not None else -1
        results[name] = {
            "Solution Depth": solution_depth,
            "Nodes Explored": nodes_explored,
            "Time Taken": end_time - start_time
        }
    print("\nPerformance Comparison:")
    for heuristic_name, result in results.items():
        print(f"{heuristic_name}:")
        print(f"  Solution Depth: {result['Solution Depth']}")
        print(f"  Nodes Explored: {result['Nodes Explored']}")
        print(f"  Time Taken: {result['Time Taken']:.6f} seconds\n")
if __name__ == "__main__":
    start_state = (
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 0, 15
    )
    goal_state = (
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 0
    )
    compare_heuristics(start_state, goal_state)
