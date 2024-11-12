from collections import defaultdict
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill:int) -> List[int]:
        graph = defaultdict(list)

        for child, parent in zip(pid, ppid):
            graph[parent].append(child)

        res = []
        queue = [kill]

        while queue:
            node = queue.pop(0)
            res.append(node)

            if node in graph:
                queue.extend(graph[node])
        
        return res



print(Solution().killProcess([1,3,10,5], [3,0,5,3], kill=5))