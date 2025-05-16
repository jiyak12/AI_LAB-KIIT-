import heapq

class AStarPathfinder:
    def __init__(self, grid, start, goals, weighted=False):
        self.grid = grid
        self.start = start
        self.goals = goals
        self.weighted = weighted
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up

    def heuristic(self, node, goal):
        """Manhattan Distance heuristic"""
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def get_neighbors(self, node):
        """Returns valid neighbors that are not obstacles"""
        neighbors = []
        for d in self.directions:
            new_x, new_y = node[0] + d[0], node[1] + d[1]
            if 0 <= new_x < self.rows and 0 <= new_y < self.cols and self.grid[new_x][new_y] == 1:
                neighbors.append((new_x, new_y))
        return neighbors

    def a_star(self):
        """A* algorithm implementation"""
        open_list = []
        heapq.heappush(open_list, (0, self.start, [self.start], 0))  # (priority, node, path, cost)
        visited = set()

        while open_list:
            priority, current, path, cost = heapq.heappop(open_list)

            if current in self.goals:
                self.goals.remove(current)  # Mark goal as reached
                if not self.goals:  # If all goals are reached, return path
                    return path, cost

            visited.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    # Ensure goals exist before calling min()
                    if self.goals:
                        priority = cost + 1 + min(self.heuristic(neighbor, g[:2]) for g in self.goals)
                    else:
                        priority = cost + 1  # No goals left

                    heapq.heappush(open_list, (priority, neighbor, path + [neighbor], cost + 1))

        return None, float('inf')  # If no path is found

# --- Sample Test Cases ---
test_cases = [
    {
        "grid": [[0, 1, 1, 1, 1, 0, 1],
                 [1, 1, 1, 0, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1, 1]],
        "start": (0, 0),
        "goals": [(2, 1), (0, 4)],
        "exit": (3, 4)
    },
    {
        "grid": [[1, 1, 1, 1, 1, 0, 1],
                 [1, 1, 1, 0, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 0, 1, 0],
                 [1, 1, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 0, 1, 1]],
        "start": (0, 0),
        "goals": [(1, 2), (5, 4), (2, 4)],
        "exit": (5, 5)
    }
]

# Running A* for each test case
for i, case in enumerate(test_cases):
    print(f"\n--- Shortest Path Analysis for Sample {i + 1} ---")
    pathfinder = AStarPathfinder(case["grid"], case["start"], case["goals"].copy(), weighted=False)
    path, cost = pathfinder.a_star()

    if path:
        print(f"Path Traveled: {path[:10]}... (truncated)" if len(path) > 10 else f"Path Traveled: {path}")
        print(f"Total Path Cost: {cost}")
    else:
        print("No path found.")
