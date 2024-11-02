class Solution:
    def countSubStrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPalidromes(s, i,i)
            count += self.countPalidromes(s, i, i+1)
        return count

    def countPalidromes(self, s, L, R):
        res = 0
        while L >=0 and R < len(s) and s[L] == s[R]:
            res += 1
            L = L - 1
            R = R + 1
        return res