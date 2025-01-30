from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n:int, trust: List[List[int]]) -> int:
        # incoming hashmap
        incoming = defaultdict(int)
        # outgoing hashmap
        outgoing = defaultdict(int)

        for src, dest in trust:
            incoming[src] +=1
            outgoing[dest] += 1
        
        for i in range(1, n+1):
            if incoming[i] == n-1 and outgoing[i] == 0:
                return i
        return -1
        