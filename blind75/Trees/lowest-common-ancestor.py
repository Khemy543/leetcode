# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p or root.val == q:
            return root.val
        
        if p.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(p.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root.val