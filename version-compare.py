class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        maxLength = max(len(version1), len(version2))

        res = 0
        
        i = maxLength - 1
        
        while i >= 0:
            v1 = v2 = 0
            # compare the versions
            if i < len(version1) and int(version1[i]):
                v1 = int(version1[i])
            if i < len(version2) and int(version2[i]):
                v2 = int(version2[i])

            if v1 < v2:
                res = -1
            elif v1 > v2:
                res = 1
            i -= 1

        return res

            