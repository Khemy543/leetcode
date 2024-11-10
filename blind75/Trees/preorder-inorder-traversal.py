# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # first value of preorder is the root node
        root = TreeNode(preorder[0])
        
        # find the index of the root in the inorder list
        mid = inorder.index(preorder[0])

        # all value to the left of mid in the inorder form the left subtree
        # mid+1 is the number of value you should get from the preoder to form your left node starting from index 0
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root