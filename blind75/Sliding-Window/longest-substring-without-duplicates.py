class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        maxLength = 0
        charSet = set()

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L = L + 1
            charSet.add(s[R])
            maxLength = max(maxLength, R - L + 1)
        return maxLength