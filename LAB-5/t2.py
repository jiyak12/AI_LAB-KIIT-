import heapq
import numpy as np
import matplotlib.pyplot as plt
def diagonal_distance(a, b):
  return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
def a_star_diagonal(grid, start, goal):
  rows, cols = len(grid), len(grid[0])
  open_list = [(0, start)]
  came_from = {}
  g_score = {start: 0}
  f_score = {start: diagonal_distance(start, goal)}
  while open_list:
    _, current = heapq.heappop(open_list)
    if current == goal:
      return reconstruct_path(came_from, current)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
      neighbor = (current[0] + dx, current[1] + dy)
      if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
        tentative_g_score = g_score[current] + (1.414 if dx != 0 and dy != 0 else 1)

        if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
          came_from[neighbor] = current
          g_score[neighbor] = tentative_g_score
          f_score[neighbor] = tentative_g_score + diagonal_distance(neighbor, goal)
          heapq.heappush(open_list, (f_score[neighbor], neighbor))
  return None
def reconstruct_path(came_from, current):
  path = [current]
  while current in came_from:
    current = came_from[current]
    path.append(current)
  path.reverse()
  return path
grid = np.array([[0, 0, 1, 0, 0],[0, 0, 0, 0, 1],[1, 0, 1, 0, 0],[0, 0, 0, 0, 0]])
start = (0, 0)
goal = (3, 4)
path = a_star_diagonal(grid, start, goal)
if path:
  plt.imshow(grid, cmap='gray')
  plt.plot([p[1] for p in path], [p[0] for p in path], marker='o', color='blue')
  plt.title('A* Search with Diagonal Distance')
  plt.show()
else:
  print("No path found.")
