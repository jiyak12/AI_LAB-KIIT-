def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set()
    visited.add(start)
    nodes_explored=0
    while stack:
        (current, path) = stack.pop()
        nodes_explored+=1
        print("Nodes_explored:", nodes_explored)
        if current == end:
            return path

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            row, col = current[0] + direction[0], current[1] + direction[1]

            if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 1 and (row, col) not in visited:
                stack.append(((row, col), path + [(row, col)]))
                visited.add((row, col))

    return "No path found"
path = dfs(maze, start, end)
print("DFS Path:", path)
