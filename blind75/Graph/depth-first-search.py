class Solution:
    visited = [] # used to store visited nodes
    stack = [] # used to track visited nodes

    def depthFirstSearch(self, graph, node):
        if node not in self.visited:
            print(node, end=" ")
            self.visited.append(node)
            self.stack.append(node)
            
            frontiers = graph[node]
            for frontier in frontiers:
                self.depthFirstSearch(graph, frontier)


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

Solution().depthFirstSearch(graph, '5')