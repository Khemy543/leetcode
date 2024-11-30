from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        preMap = defaultdict(list)
        # dictionary with the course and an array of the prerequisits
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visited.remove(crs)
            preMap[crs] = []
            return True

        # loop through the courses and run dfs on the courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
        # using dfs

        graph = defaultdict(list)
        visited = set()
        queue = []

        # create a graph
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        
        def bfs(crs):
            if crs in visited:
                return False
            
            queue.append(crs)
            visited.add(crs)

            while queue:
                cr = queue.pop(0)
                for pr in graph[cr]:
                    if pr in visited:
                        return False
                    visited.add(pre)
                    queue.append(pre)
            return True

        return bfs(0)