from collections import deque

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    nodes_explored=0
    while queue:
        (current, path) = queue.popleft()
        nodes_explored+=1
        print("Nodes_explored:", nodes_explored)
        if current == end:
            return path

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            row, col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 1 and (row, col) not in visited:
                queue.append(((row, col), path + [(row, col)]))
                visited.add((row, col))
    return "No path found"
maze = [[1, 0, 1, 1, 1],[1, 1, 0, 1, 0],[0, 1, 1, 1, 1],[0, 0, 0, 0, 1],[1, 1, 1, 1, 1]]
start = (0, 0)
end = (4, 4)
path = bfs(maze, start, end)
print("BFS Path:", path)
