class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        count = {}
        maxLength = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R],0) + 1
            maxLength = max(maxLength, count[s[R]])

            if (R - L + 1) - maxLength > k:
                count[s[L]] -= 1
                L += 1

        return R - L + 1 