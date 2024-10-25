class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        L = 0
        needHashMap = {}
        haveHashMap = {}
        haveCount = 0
        needCount = 0
        res = [-1, -1]
        resLength = float("infinity")

        for i in range(len(t)):
            needHashMap[t[i]] = 1 + needHashMap.get(t[i], 0)

        needCount = len(needHashMap)
        
        for R in range(len(s)):
            if s[R] in needHashMap:
                haveHashMap[s[R]] = 1 + haveHashMap.get(s[R], 0)
                if haveHashMap[s[R]] == needHashMap[s[R]]:
                    haveCount += 1

            while haveCount == needCount:
                if (R - L + 1) < resLength:
                    res = [L,R]
                    resLength = R - L+1
                
                if s[L] in haveHashMap:
                    haveHashMap[s[L]] -= 1

                    if haveHashMap[s[L]] < needHashMap[s[L]]:
                        haveCount -= 1
                L += 1
        
        return s[res[0]: res[1] + 1]
            

                
print(Solution().minWindow('ADOBECODEBANC', 'ABC'))

