from collections import defaultdict

# Example 2D array
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize an adjacency list for the graph
graph = defaultdict(list)

# Dimensions of the array
rows = len(array)
cols = len(array[0])

# Helper function to add edges based on adjacency
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

# Build the graph
for r in range(rows):
    for c in range(cols):
        node = (r, c)
        
        # Define adjacent positions (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            # Check if the adjacent position is within bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor = (nr, nc)
                add_edge(graph, node, neighbor)

# Print the adjacency list representation of the graph
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")
    

