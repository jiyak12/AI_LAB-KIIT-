from collections import deque
def bidirectional_bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols) or not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return "Invalid start or goal positions"
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return "Start or end is a wall"
    queue_start = deque([start])
    queue_end = deque([end])
    visited_start = {start}
    visited_end = {end}
    parent_start = {start: None}
    parent_end = {end: None}
    while queue_start and queue_end:
        current_start = queue_start.popleft()
        if current_start in visited_end:
            return reconstruct_path(parent_start, parent_end, current_start)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_start = (current_start[0] + dx, current_start[1] + dy)
            if (0 <= next_start[0] < rows and 0 <= next_start[1] < cols and
                    maze[next_start[0]][next_start[1]] == 0 and
                    next_start not in visited_start):
                visited_start.add(next_start)
                queue_start.append(next_start)
                parent_start[next_start] = current_start
        current_end = queue_end.popleft()
        if current_end in visited_start:
            return reconstruct_path(parent_start, parent_end, current_end)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_end = (current_end[0] + dx, current_end[1] + dy)
            if (0 <= next_end[0] < rows and 0 <= next_end[1] < cols and
                    maze[next_end[0]][next_end[1]] == 0 and
                    next_end not in visited_end):
                visited_end.add(next_end)
                queue_end.append(next_end)
                parent_end[next_end] = current_end
    return "No path found"
def reconstruct_path(parent_start, parent_end, intersection):
    path_start = []
    current = intersection
    while current:
        path_start.append(current)
        current = parent_start[current]
    path_start = path_start[::-1]
    path_end = []
    current = intersection
    while current:
        path_end.append(current)
        current = parent_end[current]
    path_end.pop(0)
    return path_start + path_end[::-1]
maze = [[0, 1, 0, 0, 0],[0, 1, 0, 1, 0],[0, 0, 0, 1, 0],[1, 1, 0, 0, 0],[0, 0, 0, 1, 0]]
start = (0, 0)
end = (4, 4)
path = bidirectional_bfs(maze, start, end)
if isinstance(path, list):
    print("Shortest path:", path)
else:
    print(path)
