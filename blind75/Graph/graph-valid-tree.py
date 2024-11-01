from typing import List
from collections import defaultdict

# a valid tree has not loop and all nodes are connected


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        graph = defaultdict(list)
        visited = []
        
        # create a graph remember the edges are undirected that means both ways
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # use the previous value to check where the node is coming from
        def bfs(node, prev):
            if node in visited:
                return False
            
            visited.append(node)

            for frontier in graph[node]:
                 # if frontier equal to previous it is a normal bfs pattern
                 if frontier == prev:
                     continue
                 if not bfs(frontier, node):
                     return False
            return True

        return bfs(0, -1) and n == len(visited)
        
