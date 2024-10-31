class Solution:
    def breathFirstSearch(self, graph, node):
        visited = [] # list to store our visited nodes
        queue = [] # queue to tracked visited nodes

        visited.append(node)
        queue.append(node)

        while queue:
            curr = queue.pop(0)
            print(curr, end= " ")

            frontiers = graph[curr]
            for frontier in frontiers:
                if frontier not in visited:
                    visited.append(frontier)
                    queue.append(frontier)
                    




graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

Solution().breathFirstSearch(graph, '5')