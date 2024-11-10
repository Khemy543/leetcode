# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []

        def dfs(node):
            if node:
                dfs(node.left)
                results.append(node.val)
                dfs(node.right)
        dfs(root)
        return results[k - 1]
    
    def iterativeMethod(self, root: Optional[TreeNode], k:int) -> int:
        n = 0
        stack = []
        curr = root

        while curr and stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val
            curr = curr.right