class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build(self,inorder: list[int]) -> Node:
        if not inorder:
            return

        mid = len(inorder) // 2
        root = Node(inorder[mid])
        root.left = self.build(inorder[:mid])
        root.right = self.build(inorder[mid+1: ])
        return root
