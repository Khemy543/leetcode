class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            if n % 2 == 1:
                count += 1
            # bit shift by one
            n = n >> 1
        return count