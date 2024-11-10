class Solution:
    def getSum(self, a: int, b: int) -> int:
        # xor a,b
        # and a,b, shift left by 1
        # do this until shift == 0
        # code this in java

        while b:
            temp = (a & b) << 1
            a = a ^ b
            b = temp

        return a
