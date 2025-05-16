import heapq
import numpy as np
from typing import List, Tuple
class PuzzleNode:
    def __init__(self, state: Tuple[int], parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    def __lt__(self, other):
        return self.f < other.f
def manhattan_distance(state: Tuple[int], goal_state: Tuple[int]) -> int:
    size = int(len(state) ** 0.5)
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = goal_state.index(tile)
        x1, y1 = divmod(i, size)
        x2, y2 = divmod(goal_index, size)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
def get_neighbors(state: Tuple[int]) -> List[Tuple[int]]:
    size = int(len(state) ** 0.5)
    zero_index = state.index(0)
    x, y = divmod(zero_index, size)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            new_index = nx * size + ny
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append(tuple(new_state))
    return moves
def reconstruct_path(node: PuzzleNode) -> List[Tuple[int]]:
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]
def a_star_search(start_state: Tuple[int], goal_state: Tuple[int], heuristic) -> List[Tuple[int]]:
    open_set = []
    start_node = PuzzleNode(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_set, start_node)
    closed_set = set()
    g_score = {start_state: 0}
    while open_set:
        current = heapq.heappop(open_set)
        if current.state == goal_state:
            return reconstruct_path(current)
        closed_set.add(current.state)
        for neighbor in get_neighbors(current.state):
            if neighbor in closed_set:
                continue
            tentative_g_score = g_score[current.state] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                h = heuristic(neighbor, goal_state)
                heapq.heappush(open_set, PuzzleNode(neighbor, current, tentative_g_score, h))
    return []
def print_solution(path: List[Tuple[int]]):
    if not path:
        print("No solution found.")
        return
    size = int(len(path[0]) ** 0.5)
    for state in path:
        print(np.array(state).reshape((size, size)))
        print()
if __name__ == "__main__":
    start_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)
    goal_state = tuple(range(1, 16)) + (0,)
    print("Solution using Manhattan Distance:")
    path_manhattan = a_star_search(start_state, goal_state, manhattan_distance)
    print_solution(path_manhattan)
