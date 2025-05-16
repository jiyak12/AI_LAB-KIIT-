from collections import deque

def bfs(grid, start, goals):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()

        # Check if current position is a goal
        if current in goals:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return reversed path

        # Explore neighbors
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in visited):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None  # No path found

# Sample 1
grid1 = [[0, 1, 1, 1, 0, 1],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1]]
start1 = (0, 0)
goals1 = {(2, 1), (0, 4)}

path1 = bfs(grid1, start1, goals1)
print("BFS Path for Sample 1:", path1)

# Sample 2
grid2 = [[1, 1, 1, 1, 0, 1],
          [1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 0],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1]]
start2 = (0, 0)
goals2 = {(1, 2), (5, 4), (2, 4), (0, 5)}

path2 = bfs(grid2, start2, goals2)
print("BFS Path for Sample 2:", path2)
