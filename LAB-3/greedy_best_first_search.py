import heapq
import matplotlib.pyplot as plt
import numpy as np
def greedy_best_first_search(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (grid[start[0]][start[1]], start[0], start[1]))
    visited = set()
    visited.add(start)
    parent = {}
    while open_list:
        _, x, y = heapq.heappop(open_list)
        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                heapq.heappush(open_list, (grid[nx][ny], nx, ny))
    return None
def visualize_grid(grid, path, start, goal):
    rows, cols = len(grid), len(grid[0])
    grid_image = np.ones((rows, cols, 3), dtype=float)
    grid_image[grid == 1] = [0, 0, 0]
    grid_image[start[0], start[1]] = [0, 1, 0]
    grid_image[goal[0], goal[1]] = [1, 1, 0]
    if path:
        for (x, y) in path:
            grid_image[x, y] = [0, 0, 1]
    plt.imshow(grid_image)
    plt.axis('off')
    plt.show(block=True)
grid = np.array([[0,0,1,0,0],[0,0,0,0,1],[1,0,1,0,0],[0,0,0,0,0]])
start = (0, 0)
goal = (2, 4)
path = greedy_best_first_search(grid, start, goal)
if path:
    print("Path to the treasure:", path)
    visualize_grid(grid, path, start, goal)
else:
    print("No path found.")
