import heapq
import networkx as nx
import matplotlib.pyplot as plt
def ucs(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, current, path = heapq.heappop(queue)
        if current in visited:
            continue
        path = path + [current]
        visited.add(current)
        if current == goal:
            return cost, path
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return float('inf'), []
def dfs(graph, start, goal, path=[], visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    path = path + [start]
    if start == goal:
        return path
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result
    return None
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == goal:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor, _ in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None
def visualize_graph(graph, ucs_path, dfs_path, bfs_path, costs):
    G = nx.Graph()
    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    ucs_edges = [(ucs_path[i], ucs_path[i + 1]) for i in range(len(ucs_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=ucs_edges, edge_color='green', width=2, label=f"UCS Cost: {costs['ucs']}")
    if dfs_path:
        dfs_edges = [(dfs_path[i], dfs_path[i + 1]) for i in range(len(dfs_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='blue', width=2, style='dashed', label="DFS")
    if bfs_path:
        bfs_edges = [(bfs_path[i], bfs_path[i + 1]) for i in range(len(bfs_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='red', width=2, style='dotted', label="BFS")
    plt.legend()
    plt.title("Algorithm Path Visualization")
    plt.show()
graph = {'A': [('B', 1), ('C', 4)],'B': [('A', 1), ('C', 2), ('D', 6)],'C': [('A', 4), ('B', 2), ('D', 3)],'D': [('B', 6), ('C', 3)]}
start, goal = 'A', 'D'
ucs_cost, ucs_path = ucs(graph, start, goal)
dfs_path = dfs(graph, start, goal)
bfs_path = bfs(graph, start, goal)
costs = {'ucs': ucs_cost}
visualize_graph(graph, ucs_path, dfs_path, bfs_path, costs)

if ucs_path:
    print("Path to the treasure:", ucs_path)
else:
    print("No path found.")
