# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # to remove negatives
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #compute max path sum WITH split
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # return max sum WITHOUT split
            return node.val +  max(leftMax, rightMax)
        
        dfs(root)
        return res
