# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def recursion(L,R):
            if L > R:
                return None

            mid = (L + R ) // 2
            node = TreeNode(nums[mid])
            node.left = recursion(L, mid-1)
            node.right = recursion(mid+1, R)
            return node
        
        return recursion(0, len(nums) -1)
    

print(Solution().sortedArrayToBST([-10,-3,0,5,9]))