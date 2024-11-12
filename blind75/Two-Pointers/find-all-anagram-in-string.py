from typing import List


class Solution:
    def findAnagrams(self, s:str, p:str) -> List[int]:
        if len(p) > len(s): return []

        pCount, sCount = {}, {}

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []

        L = 0
        for R in range(len(p), len(s)):
            sCount[s[R]] = 1 + sCount.get(s[R], 0)
            sCount[s[L]] -= 1

            if(sCount[s[L]]) == 0:
                sCount.pop(s[L])
            
            L += 1
            
            if sCount == pCount:
                res.append(L)
        return res