class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLength = 0

        for i in range(len(s)):
            # check odd numbers
            L,R = i,i
            while L<=R and L >= 0 and R < len(s) and s[L] == s[R]:
                if(resLength < (R-L+1)):
                    res = s[L:R+1]
                    resLength = R-L+1
                L -= 1
                R += 1
            
            # check even numbers
            L,R = i, i+1
            while L<=R and L >= 0 and R < len(s) and s[L] == s[R]:
                if(resLength < (R-L+1)):
                    res = s[L:R+1]
                    resLength = R-L+1
                L -= 1
                R += 1

        return res