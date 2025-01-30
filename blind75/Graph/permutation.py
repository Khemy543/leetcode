from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]] # create empty permutation
        for n in nums: # loop all values in nums
            new_perms = []
            for p in perms: # for every permutation in perms we insert n in every index by creating copies
                for i in range(len(p) + 1):
                    p_copy = p.copy() # create a copy of the perms so that it is not mutated
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
    

print(Solution().permute([1,2,3]))