import heapq
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
GRID_SIZE = (10, 10)
OBSTACLES = [(2, 2), (2, 3), (2, 5), (3, 4), (4, 3)]
START = (0, 0)
GOAL = (7, 7)
def create_grid(grid_size, obstacles):
    grid = np.zeros(grid_size)
    for obs in obstacles:
        grid[obs] = 1
    return grid
def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])
def euclidean_distance(current, goal):
    return math.sqrt((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2)
def get_neighbors(position, grid, allow_diagonal):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if allow_diagonal:
        moves += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = []
    for move in moves:
        neighbor = (position[0] + move[0], position[1] + move[1])
        if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1] and grid[neighbor] == 0:
            neighbors.append(neighbor)
    return neighbors
def a_star_search(grid, start, goal, heuristic, allow_diagonal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for neighbor in get_neighbors(current, grid, allow_diagonal):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None
def bfs(grid, start, goal, allow_diagonal):
    queue = deque([start])
    came_from = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for neighbor in get_neighbors(current, grid, allow_diagonal):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)
    return None
def reconstruct_path(came_from, current):
  path = [current]
  while current in came_from:
    current = came_from[current]
    path.append(current)
  path.reverse()
  return path
def visualize(grid, path, title):
    plt.imshow(grid, cmap='gray_r')
    if path:
        x, y = zip(*path)
        plt.plot(y, x, color='red', linewidth=2, label='Path')
    plt.scatter(*zip(*OBSTACLES), color='black', label='Obstacles')
    plt.scatter(START[1], START[0], color='green', label='Start')
    plt.scatter(GOAL[1], GOAL[0], color='blue', label='Goal')
    plt.title(title)
    plt.legend()
    plt.show()
grid = create_grid(GRID_SIZE, OBSTACLES)
path_manhattan = a_star_search(grid, START, GOAL, manhattan_distance, allow_diagonal=False)
visualize(grid, path_manhattan, "A* with Manhattan Distance")
path_euclidean = a_star_search(grid, START, GOAL, euclidean_distance, allow_diagonal=True)
visualize(grid, path_euclidean, "A* with Euclidean Distance")
path_bfs = bfs(grid, START, GOAL, allow_diagonal=False)
visualize(grid, path_bfs, "BFS")
